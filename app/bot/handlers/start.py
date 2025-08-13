from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

@router.message(Command("start"))
async def start(message: Message):
    text = """💱 Welcome to Currency Converter Bot!  
I can quickly convert between major world currencies:  

UZS 🇺🇿 | USD 🇺🇸 | EUR 🇪🇺 | RUB 🇷🇺 | JPY 🇯🇵 | 
AUD 🇦🇺 | GBP 🇬🇧 | INR 🇮🇳 | ZAR 🇿🇦  

Just send me the amount and the currency you want to convert from,  
and I’ll give you the result instantly. ⚡  

Type /help to learn how to use me.
"""
    await message.answer(text)

@router.message(Command("help"))
async def help(message: Message):
    text = """ℹ️ How to use Currency Converter Bot

1️⃣ Send a message in the format:  
AMOUNT FROM_CURRENCY TO_CURRENCY
Example: 100 USD UZS  

2️⃣ I will reply with the converted amount using real-time exchange rates.  

💡 Supported currencies:  
UZS 🇺🇿, USD 🇺🇸, EUR 🇪🇺, RUB 🇷🇺, JPY 🇯🇵, AUD 🇦🇺, GBP 🇬🇧, INR 🇮🇳, ZAR 🇿🇦  

📌 You can also reverse the order (UZS USD) to convert in the opposite direction.  

Type /start to see the welcome message again.
"""
    await message.answer(text)