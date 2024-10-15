import re
from telebot import types

BUTTONS_EMOJI = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

async def is_subscriber(bot, channel_id, user_id):
    try:
        subscription = await bot.get_chat_member(channel_id, user_id)
        if subscription.status in ['member', 'administrator', 'creator']:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False

def escape_markdown(text):
    return re.sub(r'([_\*\[\]\(\)\~\`\>\#\+\-\=\|\{\}\.\!])', r'\\\1', text)

def display_code(code):
    return " ".join(list(code) + ["_"] * (6 - len(code)))

def send_code_keyboard(bot, telegram_id):
    markup = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(text=button, callback_data=str(i+1))
        for i, button in enumerate(BUTTONS_EMOJI)
    ]
    buttons.append(types.InlineKeyboardButton(text="0️⃣", callback_data="0"))
    markup.add(*buttons)

    bot.send_message(
        telegram_id,
        "🔑ENTER ACTIVATION KEY🔑\n⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n\nKey: " + display_code(user_inputs[telegram_id]),
        reply_markup=markup
    )