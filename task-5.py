import requests
import sqlite3
from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

API_TOKEN = '8173788949:AAE6mclk1DxwAvvrhjCbpRWzaWt_sqxVKFs'

conn = sqlite3.connect('user_data.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS user_data 
(user_id integer, message text, timestamp timestamp)''')
conn.commit()


def get_random_joke():
    return "Жарт: Ваги зламалися коли колобок звішувався "


def get_weather(city):
    return f"Погода у Харкові  +7 градусів"


def create_menu(buttons):
    reply_keyboard = [[KeyboardButton(button)] for button in buttons]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    return markup


async def send_message(chat_id, text, reply_markup=None, parse_mode=None):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    params = {'chat_id': chat_id, 'text': text}
    if reply_markup:
        params['reply_markup'] = reply_markup.to_json()
    if parse_mode:
        params['parse_mode'] = parse_mode
    response = requests.post(url, params=params)
    return response.json()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await send_message(chat_id, 'Привіт! Я твій бот.')


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    reply_markup = create_menu(['Жарт', 'Погода', 'Налаштування'])
    await send_message(chat_id, 'Выберіть команду:', reply_markup=reply_markup)


async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    whisper_text = "\\_це бібліотека і тут дуже тихо...\\."
    await context.bot.send_message(chat_id=chat_id, text=whisper_text, parse_mode='MarkdownV2')


async def scream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    scream_text = "Буде дуже лячно!"
    await context.bot.send_message(chat_id=chat_id, text=scream_text, parse_mode='MarkdownV2')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    help_text = (
        "Доступні команди:\n"
        "/start - Запустити бота\n"
        "/menu - Відкрити меню\n"
        "/whisper - Відправити тихе повідомлення\n"
        "/scream - Відправити гучне повідомлення\n"
        "/help - Показати це повідомлення"
    )
    await send_message(chat_id, help_text)


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text.lower()

    store_user_data(chat_id, text)

    if text == 'жарт':
        joke = get_random_joke()
        await send_message(chat_id, joke)
    elif text == 'погода':
        city = 'Харків'
        weather = get_weather(city)
        await send_message(chat_id, weather)
    else:
        await send_message(chat_id, 'Я не розумію цю команду.')


def store_user_data(user_id, message):
    with conn:
        c.execute("INSERT INTO user_data VALUES (?, ?, datetime('now'))", (user_id, message))


def main():
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("whisper", whisper))
    application.add_handler(CommandHandler("scream", scream))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    application.run_polling()


if __name__ == '__main__':
    main()