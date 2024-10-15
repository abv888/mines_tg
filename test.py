import telebot
from telebot import types

bot = telebot.TeleBot('7861684872:AAF2kFgxDP1aXwNp81AuScj0-7MmcL-47-4')

# Хранение активных кодов и введённых пользователями данных
active_codes = {"123456": "valid"}
user_inputs = {}

buttons_emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

# Команда для старта
@bot.message_handler(commands=['start'])
def start_message(message):
    user_inputs[message.chat.id] = ""
    send_code_keyboard(message)

# Отправляем клавиатуру с цифрами
def send_code_keyboard(message, user_inputs):
    markup = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text=button, callback_data=str(i+1))
        for i, button in enumerate(buttons_emoji)
    ]
    buttons.append(types.InlineKeyboardButton(text="0️⃣", callback_data="0"))
    markup.add(*buttons)

    bot.send_message(
        message.chat.id,
        "🔑ENTER ACTIVATION KEY🔑\n⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n\nKey: " + display_code(user_inputs[message.chat.id]),
        reply_markup=markup
    )

# Отображаем введённые цифры с пропусками
def display_code(code):
    return " ".join(list(code) + ["_"] * (6 - len(code)))

# Обрабатываем нажатие на кнопки
@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def handle_digit_input(call):
    chat_id = call.message.chat.id
    if chat_id not in user_inputs:
        user_inputs[chat_id] = ""

    current_input = user_inputs[chat_id]

    if len(current_input) < 6:
        current_input += call.data
        user_inputs[chat_id] = current_input

        # Обновляем сообщение после каждой введенной цифры
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,
            text="🔑ENTER ACTIVATION KEY🔑\n⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n\nKey: " + display_code(current_input),
            reply_markup=call.message.reply_markup
        )

        # После ввода последней цифры проверяем код
        if len(current_input) == 6:
            bot.answer_callback_query(call.id)  # Убираем индикатор загрузки
            check_code(call.message, current_input)

# Проверяем введённый код
def check_code(message, code):
    if code in active_codes:
        bot.send_message(message.chat.id, "✅ Код активации введён правильно!")
    else:
        bot.send_message(message.chat.id, "❌ Неверный код активации!")

    # Сброс кода
    user_inputs[message.chat.id] = ""
    send_code_keyboard(message)

bot.polling()