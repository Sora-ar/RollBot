import random
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = "7920120199:AAHZ4Stb1RkywvI5l2aefiIzvMjND65uc3E"

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем экземпляры бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

questions = {
    1: "Яка твоя улюблена книга?",
    2: "Що б ти зробив, якби виграв мільйон доларів?",
    3: "Яке твоє улюблене хобі?",
    4: "Яку країну ти б хотів відвідати?",
    5: "Якби ти міг мати суперсилу, яку б ти вибрав?",
    6: "Що тебе найбільше мотивує у житті?"
}

@dp.message(Command("roll"))
async def roll_dice(message: Message):
    # Отправляем анимированный кубик
    dice_message = await message.answer_dice()

    # Ждем результат броска (около 3 сек)
    await asyncio.sleep(5)

    # Число на кубике (от 1 до 6)
    dice_result = dice_message.dice.value
    question = questions.get(dice_result, "Щось пішло не так...")

    await message.answer(f"🎲 Тобі випало {dice_result}!\n❓ {question}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
