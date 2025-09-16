from decouple import config

import telebot
from telebot import types

API_TOKEN = config("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

user_data = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    msg = bot.send_message(chat_id, "سلام! خوش اومدی 👋\nاول اسم کوچیکت رو بگو:")
    bot.register_next_step_handler(msg, get_name)


def get_name(message):
    chat_id = message.chat.id
    user_data[chat_id]['name'] = message.text
    msg = bot.send_message(chat_id, f"خوش اومدی {message.text} 🌊\nساعت خواب رو بگو (مثلاً 23:30):")
    bot.register_next_step_handler(msg, get_sleep)


def get_sleep(message):
    chat_id = message.chat.id
    user_data[chat_id]['sleep'] = message.text
    msg = bot.send_message(chat_id, "حالا ساعت بیدار شدنت رو بگو (مثلاً 07:00):")
    bot.register_next_step_handler(msg, get_wake)


def get_wake(message):
    chat_id = message.chat.id
    user_data[chat_id]['wake'] = message.text
    msg = bot.send_message(chat_id, "روزانه چند بار میخوای آب بخوری؟ (عدد وارد کن)")
    bot.register_next_step_handler(msg, get_times)


def get_times(message):
    chat_id = message.chat.id
    user_data[chat_id]['times'] = message.text
    msg = bot.send_message(chat_id, "هدفت چند میلی‌لیتر در روزه؟ (مثلاً 2000):")
    bot.register_next_step_handler(msg, get_goal)


def get_goal(message):
    chat_id = message.chat.id
    user_data[chat_id]['goal'] = int(message.text)

    guide = (
        "📌 راهنمای مصرف آب روزانه:\n"
        "- مرد بالغ: حدود ۳۰۰۰ml\n"
        "- زن بالغ: حدود ۲۲۰۰ml\n"
        "- ورزشکار: بسته به فعالیت بیشتر (۵۰۰ml اضافی به ازای هر ساعت ورزش)\n"
        "- افراد با بیماری (مثل دیابت): باید با پزشک مشورت کنند\n"
    )
    bot.send_message(chat_id, guide)

    bot.send_message(chat_id, f"خیلی عالی! ✅ همه اطلاعات ذخیره شد.\nاز امروز بهت یادآوری میکنم آب بخوری 💧")

    send_reminder(chat_id)


def send_reminder(chat_id):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🥛 یک لیوان (150ml)", callback_data="drink_150")
    btn2 = types.InlineKeyboardButton("🍶 یک کاپ (250ml)", callback_data="drink_250")
    btn3 = types.InlineKeyboardButton("☕ یک فنجون (70ml)", callback_data="drink_70")
    btn4 = types.InlineKeyboardButton("⏰ الان نمیتونم", callback_data="later")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    bot.send_message(chat_id, "💧 وقتشه آب بخوری!", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if call.data.startswith("drink_"):
        ml = int(call.data.split("_")[1])
        bot.answer_callback_query(call.id, f"{ml}ml ثبت شد! ✅")
        bot.send_message(chat_id, f"👌 {ml}ml به مصرف روزانت اضافه شد.")
    elif call.data == "later":
        bot.answer_callback_query(call.id, "باشه، دوباره بهت یادآوری میکنم ⏳")
        bot.send_message(chat_id, "یادآوری بعداً تکرار میشه.")


bot.polling()
