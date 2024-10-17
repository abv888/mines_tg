import asyncio

import telebot.async_telebot as telebot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
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
    admin_add_permission_to, set_localization_for_user, activate_bot_for, get_all_users
)

from utils.localization import LOCALE, GREETING_1, GREETING_2, SUPPORT_USERNAME
from utils.utils import is_subscriber, escape_markdown, send_code_keyboard, display_code, BUTTONS_EMOJI

bot = telebot.AsyncTeleBot(token=os.getenv("BOT_TOKEN"))
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL")
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))
SUPPORT_LINK = os.getenv("SUPPORT_LINK")
ADMIN = os.getenv("ADMIN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
IOS_APP = os.getenv("IOS_APP")
ANDROID_APP = os.getenv("ANDROID_APP")
REFERRAL_LINK = os.getenv("REFERRAL_LINK")
ACTIVATION_CODE = os.getenv("ACTIVATION_CODE")
CODE_INPUTS = {}

@bot.message_handler(commands=['start'])
async def start(message):
    async with session_maker() as session:
        if await check_user_existence(session, message.from_user.id) is None:
            user = User(
                telegram_id=message.from_user.id,
                full_name=message.from_user.full_name,
                localization='en',
                username=message.from_user.username,
                permission=False
            )
            session.add(user)
            await session.commit()
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        next_step_button = types.InlineKeyboardButton(
            text=f"NEXT STEP👞",
            callback_data="check_subscription"
        )
        keyboard.add(
            next_step_button
        )
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"{GREETING_1}, {message.from_user.username}, "
                                    f"{GREETING_2}",
                               reply_markup=keyboard,
                               disable_web_page_preview=True,
                               parse_mode="HTML"
                               )



@bot.callback_query_handler(func=lambda call:True)
async def callback_inline(call):
    async with session_maker() as session:
        if call.data == "start_message":
            if await is_subscriber(
                    bot=bot,
                    channel_id=TARGET_CHANNEL_ID,
                    user_id=call.message.chat.id
            ):
                keyboard = types.InlineKeyboardMarkup(
                    row_width=1
                )
                next_step_button = types.InlineKeyboardButton(
                    text=f"NEXT STEP👞",
                    callback_data="check_subscription"
                )
                keyboard.add(
                    next_step_button
                )
                await bot.send_message(chat_id=call.message.chat.id,
                                       text=f"{GREETING_1}, {call.message.from_user.username}, "
                                            f"{GREETING_2}",
                                       reply_markup=keyboard,
                                       disable_web_page_preview=True,
                                       parse_mode="HTML"
                                       )
            else:
                call.data = "check_subscription"
        if call.data == "check_subscription":
            if await is_subscriber(
                    bot=bot,
                    channel_id=TARGET_CHANNEL_ID,
                    user_id=call.message.chat.id
            ):
                call.data = "subscriber"
            else:
                keyboard = types.InlineKeyboardMarkup(
                    row_width=1
                )
                subscribe_button = types.InlineKeyboardButton(
                    text="Subscribe",
                    url=TARGET_CHANNEL
                )
                check_button = types.InlineKeyboardButton(
                    text="✅ Check",
                    callback_data="start_message"
                )
                keyboard.add(
                    subscribe_button,
                    check_button
                )
                await bot.send_message(
                    chat_id=call.message.chat.id,
                    text="❗️ Error!\n"
                         "You have not subscribed to the channel.",
                    reply_markup=keyboard
                )
        if call.data == "subscriber":
            keyboard = types.InlineKeyboardMarkup(
                row_width=1
            )
            instruction_button = types.InlineKeyboardButton(
                text="How does the bot work? 🤖",
                callback_data="instruction"
            )
            keyboard.add(instruction_button)
            await bot.send_message(
                chat_id=call.message.chat.id,
                text="Great, you have subscribed to the channel.🎉",
                reply_markup=keyboard
            )
        if call.data == "instruction":
            keyboard = types.InlineKeyboardMarkup(
                row_width=1
            )
            choose_language = types.InlineKeyboardButton(
                text="Start earning money 💰",
                callback_data="choose_language"
            )
            keyboard.add(choose_language)
            await bot.send_video(
                video=open(f"resources/guide.MP4", "rb"),
                chat_id=call.message.chat.id,
                caption=f"||For the bot to work correctly, the minimum bet is $6||",
                reply_markup=keyboard,
                parse_mode="MarkdownV2"
            )
        if call.data == "choose_language":
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
            await bot.send_message(chat_id=call.message.chat.id,
                                   text="Select your country 🌍",
                                   reply_markup=keyboard)
        if call.data in LOCALE.keys():
            await set_localization_for_user(
                session=session,
                user_id=call.message.chat.id,
                localization=call.data
            )
            call.data = "registration"
        if call.data == "registration":
            language = await get_localization_for_user(
                session=session,
                user_id=call.message.chat.id
            )
            keyboard = types.InlineKeyboardMarkup(
                row_width=1
            )
            register_button = types.InlineKeyboardButton(
                text="REGISTER HERE ⛓️",
                url=LOCALE[language].link
            )
            get_signal_button = types.InlineKeyboardButton(
                text="GET SIGNAL",
                callback_data="get_signal"
            )
            keyboard.add(
                register_button,
                get_signal_button
            )
            await bot.send_photo(
                photo=open(f"resources/{language}.jpg", "rb"),
                chat_id=call.message.chat.id,
                caption=f"{LOCALE[language].register_text_1[0]}"
                     f"<a href='{REFERRAL_LINK}' style='text-decoration:none'>{LOCALE[language].link_text[0]}</a>"
                     f"{LOCALE[language].register_text_2[0]}",
                reply_markup=keyboard,
                parse_mode="HTML"
            )
        if call.data == "get_signal":
            language = await get_localization_for_user(
                session=session,
                user_id=call.message.chat.id
            )
            keyboard = types.InlineKeyboardMarkup(
                row_width=1
            )
            send_screenshot_button = types.InlineKeyboardButton(
                text="SEND SCREENSHOT",
                url=SUPPORT_LINK
            )
            check_permission_button = types.InlineKeyboardButton(
                text="ACTIVATE BOT 🔑",
                callback_data="activation"
            )
            keyboard.add(send_screenshot_button, check_permission_button)
            await bot.send_photo(
                photo=open(f"resources/account_screen.jpg", "rb"),
                chat_id=call.message.chat.id,
                caption=f"{LOCALE[language].verification_info_message_text[0]}",
                reply_markup=keyboard
            )
            await bot.send_photo(
                photo=open(f"resources/send_screenshot.jpg", "rb"),
                chat_id=call.message.chat.id
            )
        if call.data == "activation":
            if await check_permission(
                session=session,
                tg_username=call.message.from_user.username
            ):
                call.data = "referral"
            else:
                CODE_INPUTS[call.message.chat.id] = ""
                markup = types.InlineKeyboardMarkup(row_width=3)
                buttons = [
                    types.InlineKeyboardButton(text=button, callback_data=str(i + 1))
                    for i, button in enumerate(BUTTONS_EMOJI)
                ]
                buttons.append(types.InlineKeyboardButton(text="0️⃣", callback_data="0"))
                markup.add(*buttons)

                await bot.send_message(
                    call.message.chat.id,
                    "🔑ENTER ACTIVATION KEY🔑\n⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n\nKey: " + display_code(
                        CODE_INPUTS[call.message.chat.id]),
                    reply_markup=markup
                )
        if call.data.isdigit():
            user_id = call.message.chat.id
            if user_id not in CODE_INPUTS.keys():
                CODE_INPUTS[user_id] = ""
            if len(CODE_INPUTS[user_id]) < 6:
                CODE_INPUTS[user_id] = CODE_INPUTS[user_id] + call.data
                await bot.edit_message_text(
                    chat_id=user_id,
                    message_id=call.message.message_id,
                    text="🔑ENTER ACTIVATION KEY🔑\n⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️\n\nKey: " + display_code(CODE_INPUTS[user_id]),
                    reply_markup=call.message.reply_markup
                )
            if len(CODE_INPUTS[user_id]) == 6:
                await bot.answer_callback_query(call.id)
                if CODE_INPUTS[user_id] == ACTIVATION_CODE:
                    call.data = "referral"
                    await activate_bot_for(
                        session=session,
                        tg_id=user_id
                    )
                else:
                    await bot.send_message(
                        chat_id=user_id,
                        text="❌<b>INCORRECT ACTIVATION KEY</b>❌\n"
                             f"To get the key 🔑, send a screenshot of your 1WIN account to support {SUPPORT_USERNAME}",
                        parse_mode="HTML"
                    )
                CODE_INPUTS.pop(
                    user_id,
                    None
                )
        if call.data == "referral":
            language = await get_localization_for_user(
                session=session,
                user_id=call.message.chat.id
            )
            keyboard = types.InlineKeyboardMarkup(
                row_width=1
            )
            ios_webapp = types.WebAppInfo(
                url=IOS_APP,
            )
            android_webapp = types.WebAppInfo(
                url=ANDROID_APP,
            )
            ios_button = types.InlineKeyboardButton(
                text=LOCALE[language].open_ios_text[0],
                web_app=ios_webapp
            )
            android_button = types.InlineKeyboardButton(
                text=LOCALE[language].open_android_text[0],
                web_app=android_webapp
            )
            keyboard.add(
                ios_button,
                android_button
            )
            await bot.send_message(
                chat_id=call.message.chat.id,
                text=f"{LOCALE[language].webapp[0]}",
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

async def send_daily_notification():
    async with session_maker() as session:
        users = await get_all_users(session)
        for user in users:
            await bot.send_message(
                chat_id=user.telegram_id,
                text=LOCALE[user.localization].push[0]
            )

async def on_startup():
    scheduler.start()
    run_param = False
    if run_param:
        await drop_db()

    await create_db()

scheduler = AsyncIOScheduler()
scheduler.add_job(send_daily_notification, "cron", day_of_week="mon-sun", hour=13, minute=0)

async def main():
    await on_startup()
    await bot.polling(none_stop=True)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot Shut Down")