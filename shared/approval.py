import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler
from shared.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


async def send_message(text: str) -> None:
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text, parse_mode="Markdown")


async def send_for_approval(text: str, item_id: str) -> None:
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Approve", callback_data=f"approve:{item_id}"),
            InlineKeyboardButton("Edit", callback_data=f"edit:{item_id}"),
            InlineKeyboardButton("Skip", callback_data=f"skip:{item_id}"),
        ]
    ])
    await bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=text,
        reply_markup=keyboard,
        parse_mode="Markdown",
    )


def notify(text: str) -> None:
    asyncio.run(send_message(text))
