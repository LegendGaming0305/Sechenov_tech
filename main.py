import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import BOT_API

dp = Dispatcher()
bot = Bot(BOT_API, parse_mode=ParseMode.HTML)

async def on_startup() -> None:
    print('Бот запущен!')

async def on_shutdown() -> None:
    print('Бот выключен!')

async def main() -> None:
    from message_handlers import router
    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.include_routers(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())