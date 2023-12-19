from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from keyboards import markup
from additional import counting_results

router = Router()

@router.message(Command('start'))
async def process_start(message: types.Message):
    await message.answer(text='Пройдите форму', reply_markup=markup)

@router.message(F.web_app_data)
async def process_web_app_data(message: types.Message):
    from main import bot
    await counting_results(information=message.web_app_data.data)
    pdf = FSInputFile('results.pdf')
    await bot.send_document(chat_id=message.from_user.id, document=pdf, caption='Результаты опроса')