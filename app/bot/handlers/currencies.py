from aiogram import Router, F
from aiogram.types import Message
import re

from app.bot.utils import convert

router = Router()

@router.message(F.text)
async def currency(message: Message):
    pattern = r"^\s*(\d+(?:\.\d+)?)\s+(UZS|USD|EUR|RUB|JPY|AUD|GBP|INR|ZAR|uzs|usd|eur|rub|jpy|aud|gbp|inr|zar)\s+(UZS|USD|EUR|RUB|JPY|AUD|GBP|INR|ZAR|uzs|usd|eur|rub|jpy|aud|gbp|inr|zar)\s*$"
    match = re.match(pattern, message.text)
    if match:
        amount = float(match.group(1))
        from_currency: str = match.group(2)
        to_currency: str = match.group(3)
        await message.answer(f"{amount} {from_currency.upper()} = {convert(amount, from_currency, to_currency)} {to_currency.upper()}")
    else:
        await message.answer("Invalid input format. Please use the format:\n AMOUNT FROM_CURRENCY TO_CURRENCY\nExample: 100 USD UZS\n\n💡 Supported currencies: UZS 🇺🇿, USD 🇺🇸, EUR 🇪🇺, RUB 🇷🇺, JPY 🇯🇵, \nAUD 🇦🇺, GBP 🇬🇧, INR 🇮🇳, ZAR 🇿🇦\n\nFor more informations /help")
