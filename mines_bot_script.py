import asyncio

import telebot.async_telebot as telebot
from telebot import types

import os

from dotenv import (
    load_dotenv,
    find_dotenv
)

load_dotenv(find_dotenv())

from db.engine import (
    session_maker,
    drop_db,
    create_db
)
from db.models import User
from db.requests import (
    check_user_existence,
    get_localization_for_user,
    check_permission,
    admin_add_permission_to
)

from utils.localization import LOCALE
from utils.utils import is_subscriber



bot = telebot.AsyncTeleBot(token=os.getenv("BOT_TOKEN"))
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))
SUPPORT_LINK = os.getenv("SUPPORT_LINK")
ADMIN = os.getenv("ADMIN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

@bot.message_handler(commands=['start'])
async def start(message):
    async with session_maker() as session:
        if await check_user_existence(session, message.from_user.id):
            localization = await get_localization_for_user(
                session=session,
                user_id=message.from_user.id
            )
            keyboard = types.InlineKeyboardMarkup(
                row_width=1
            )
            subscribe_button = types.InlineKeyboardButton(
                text=f"{LOCALE[localization].subscribe[0]}",
                url=TARGET_CHANNEL
            )
            check_button = types.InlineKeyboardButton(
                text=f"{LOCALE[localization].already_subscribed[0]}",
                callback_data="check_subscription"
            )
            keyboard.add(
                subscribe_button,
                check_button
            )
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"{LOCALE[localization].greeting_welcome_start[0]}, {message.from_user.username}, "
                                        f"{LOCALE[localization].greeting_welcome_end[0]}",
                                   reply_markup=keyboard,
                                   parse_mode="Markdown"
                                   )
        else:
            keyboard = types.InlineKeyboardMarkup(
                row_width=2
            )
            ind_en_button = types.InlineKeyboardButton(
                text="India 🇮🇳 (En)",
                callback_data="ind_en"
            )
            ind_hi_button = types.InlineKeyboardButton(
                text="India 🇮🇳 (Hi)",
                callback_data="ind_hi"
            )
            uz_button = types.InlineKeyboardButton(
                text="O'zbekiston 🇺🇿",
                callback_data="uz"
            )
            ag_button = types.InlineKeyboardButton(
                text="Argentina 🇦🇷",
                callback_data="ag"
            )
            ch_button = types.InlineKeyboardButton(
                text="Chilie 🇨🇱",
                callback_data="ch"
            )
            bn_button = types.InlineKeyboardButton(
                text="Bangladesh 🇧🇩",
                callback_data="bn"
            )
            gh_button = types.InlineKeyboardButton(
                text="Ghana 🇬🇭 (Africa)",
                callback_data="gh"
            )
            tr_button = types.InlineKeyboardButton(
                text="Turkey 🇹🇷",
                callback_data="tr"
            )
            br_button = types.InlineKeyboardButton(
                text="Brazil 🇧🇷",
                callback_data="br"
            )
            np_button = types.InlineKeyboardButton(
                text="Nepal 🇳🇵",
                callback_data="np"
            )
            pk_button = types.InlineKeyboardButton(
                text="Pakistan 🇵🇰",
                callback_data="pk"
            )
            ru_button = types.InlineKeyboardButton(
                text="Русский 🇷🇺",
                callback_data="ru"
            )
            esp_button = types.InlineKeyboardButton(
                text="Other 🇪🇸 (Spainish)",
                callback_data="esp"
            )
            en_button = types.InlineKeyboardButton(
                text="Other 🇬🇧 (English)",
                callback_data="en"
            )
            keyboard.add(
                ind_en_button,
                ind_hi_button,
                uz_button,
                ag_button,
                ch_button,
                bn_button,
                gh_button,
                tr_button,
                br_button,
                np_button,
                pk_button,
                ru_button,
                esp_button,
                en_button
            )
            await bot.send_message(chat_id=message.chat.id,
                                   text="Select your country 🌍",
                                   reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
async def callback_inline(call):
    async with session_maker() as session:
        if call.data in LOCALE.keys():
            user = User(
                telegram_id=call.message.chat.id,
                full_name=call.from_user.full_name,
                localization=call.data,
                username=call.from_user.username,
                permission=False
            )
            session.add(user)
            await session.commit()
            keyboard = types.InlineKeyboardMarkup(
                row_width=1
            )
            subscribe_button = types.InlineKeyboardButton(
                text=LOCALE[call.data].subscribe[0],
                url=TARGET_CHANNEL
            )
            check_button = types.InlineKeyboardButton(
                text=LOCALE[call.data].already_subscribed[0],
                callback_data="check_subscription"
            )
            keyboard.add(
                subscribe_button,
                check_button
            )
            await bot.delete_message(
                chat_id=call.message.chat.id,
                message_id=call.message.id
            )
            await bot.send_message(chat_id=call.message.chat.id,
                                   text=f"{LOCALE[call.data].greeting_welcome_start[0]}, {call.from_user.username}"
                                        f"{LOCALE[call.data].greeting_welcome_end[0]}",
                                   reply_markup=keyboard
                                   )
        else:
            language = await get_localization_for_user(
                session=session,
                user_id=call.message.chat.id
            )
            if call.data == "check_subscription":
                if await is_subscriber(
                        bot=bot,
                        channel_id=TARGET_CHANNEL_ID,
                        user_id=call.message.chat.id
                ):
                    call.data = "subscriber"
                else:
                    await bot.answer_callback_query(
                        callback_query_id=call.id,
                        show_alert=True,
                        text=LOCALE[language].error_subscription[0]
                    )
                    await bot.delete_message(
                        chat_id=call.message.chat.id,
                        message_id=call.message.id
                    )
                    keyboard = types.InlineKeyboardMarkup(
                        row_width=1
                    )
                    subscribe_button = types.InlineKeyboardButton(
                        text=LOCALE[call.data].subscribe[0],
                        url=TARGET_CHANNEL
                    )
                    check_button = types.InlineKeyboardButton(
                        text=LOCALE[call.data].already_subscribed[0],
                        callback_data="check_subscription"
                    )
                    keyboard.add(
                        subscribe_button,
                        check_button
                    )
                    await bot.delete_message(
                        chat_id=call.message.chat.id,
                        message_id=call.message.id
                    )
                    await bot.send_message(chat_id=call.message.chat.id,
                                           text=f"{LOCALE[call.data].greeting_welcome_start[0]}, {call.from_user.username}"
                                                f"{LOCALE[call.data].greeting_welcome_end[0]}",
                                           reply_markup=keyboard
                                           )
            if call.data == "subscriber":
                keyboard = types.InlineKeyboardMarkup(
                    row_width=1
                )
                instruction_button = types.InlineKeyboardButton(
                    text=LOCALE[language].how_does_the_bot_work,
                    callback_data="instruction"
                )
                keyboard.add(instruction_button)
                await bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=call.message.id
                )
                await bot.send_message(
                    chat_id=call.message.chat.id,
                    text=LOCALE[language].subscriber[0],
                    reply_markup=keyboard
                )
            if call.data == "instruction":
                keyboard = types.InlineKeyboardMarkup(
                    row_width=1
                )
                start_earning_button = types.InlineKeyboardButton(
                    text=LOCALE[language].start_earning[0],
                    callback_data="registration"
                )
                keyboard.add(start_earning_button)
                await bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=call.message.id
                )
                await bot.send_message(
                    chat_id=call.message.chat.id,
                    # video="",
                    text=LOCALE[language].gift[0],
                    reply_markup=keyboard
                )
            if call.data == "registration":
                keyboard = types.InlineKeyboardMarkup(
                    row_width=1
                )
                register_button = types.InlineKeyboardButton(
                    text=LOCALE[language].register_button[0],
                    url=LOCALE[language].link
                )
                get_signal_button = types.InlineKeyboardButton(
                    text=LOCALE[language].get_signal_button[0],
                    callback_data="get_signal"
                )
                keyboard.add(register_button, get_signal_button)
                await bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=call.message.id
                )
                await bot.send_message(
                    chat_id=call.message.chat.id,
                    text=f"{LOCALE[language].register_text_1[0]}"
                         f"<a href='{LOCALE[language].link}' style='text-decoration:none'>{LOCALE[language].link_text}</a>"
                         f"{LOCALE[language].register_text_2[0]}",
                    reply_markup=keyboard,
                    parse_mode="HTML"
                )
            if call.data == "get_signal":
                keyboard = types.InlineKeyboardMarkup(
                    row_width=1
                )
                send_screenshot_button = types.InlineKeyboardButton(
                    text=LOCALE[language].send_screenshot_button_text[0],
                    url=SUPPORT_LINK
                )
                check_permission_button = types.InlineKeyboardButton(
                    text=LOCALE[language].check_permission_button[0],
                    callback_data="check_permission"
                )
                keyboard.add(send_screenshot_button, check_permission_button)
                await bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=call.message.id
                )
                # await bot.send_media_group(
                #     chat_id=call.message.chat.id,
                #     media=[]
                # )
                await bot.send_message(
                    chat_id=call.message.chat.id,
                    text=f"{LOCALE[language].verification_info_message_text[0]}",
                    reply_markup=keyboard
                )
            if call.data == "check_permission":
                if await check_permission(
                    session=session,
                    tg_username=call.message.chat.username
                ):
                    call.data = "referral"
                else:
                    keyboard = types.InlineKeyboardMarkup(
                        row_width=1
                    )
                    contact_support_button = types.InlineKeyboardButton(
                        text=LOCALE[language].contact_support_button[0],
                        url=SUPPORT_LINK
                    )
                    check_permission_button = types.InlineKeyboardButton(
                        text=LOCALE[language].check_permission_button[0],
                        callback_data="check_permission"
                    )
                    keyboard.add(contact_support_button, check_permission_button)
                    await bot.delete_message(
                        chat_id=call.message.chat.id,
                        message_id=call.message.id
                    )
                    await bot.send_message(
                        chat_id=call.message.chat.id,
                        text=LOCALE[language].no_permission_text[0],
                        reply_markup=keyboard
                    )
            if call.data == "referral":
                keyboard = types.InlineKeyboardMarkup(
                    row_width=1
                )
                webapp = types.WebAppInfo(
                    url=LOCALE[language].link_to_webapp[0],
                )
                ios_button = types.InlineKeyboardButton(
                    text=LOCALE[language].open_ios_text[0],
                    web_app=webapp
                )
                android_button = types.InlineKeyboardButton(
                    text=LOCALE[language].open_android_text[0],
                    web_app=webapp
                )
                keyboard.add(
                    ios_button,
                    android_button
                )
                await bot.delete_message(
                    chat_id=call.message.chat.id,
                    message_id=call.message.id
                )
                await bot.send_message(
                    chat_id=call.message.chat.id,
                    text=f"{LOCALE[language].webapp}",
                    reply_markup=keyboard
                )


@bot.message_handler(
    func=lambda message: message.text
                         and message.text.__contains__("@")
                         and message.from_user.username == ADMIN
)
async def admin_command_handler(message):
    username = message.text.split(" ")[0].split("@")[-1]
    cmd = message.text.split(" ")[-1]
    if cmd == 'add':
        async with session_maker() as session:
            await admin_add_permission_to(
                session=session,
                tg_username=username
            )

async def on_startup():
    run_param = False
    if run_param:
        await drop_db()

    await create_db()

async def main():
    await on_startup()
    await bot.polling(none_stop=True)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot Shut Down")