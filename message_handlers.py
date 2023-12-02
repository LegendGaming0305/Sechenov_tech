from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import MenuButtonWebApp, WebAppInfo, WebAppData

from keyboards import markup

router = Router()

@router.message(Command('start'))
async def process_start(message: types.Message):
    await message.answer(text='Пройдите форму', reply_markup=markup)

@router.message(F.web_app_data)
async def process_web_app_data(web_app_data: types.WebAppData):
    pass