import os
import asyncio
import ssl
import aiohttp

from dotenv import load_dotenv
from vkbottle import Bot, AiohttpClient
from handlers import start, atach, action


load_dotenv()

token = os.getenv("VK_TOKEN")

if not token:
    raise ValueError("Не найден VK_TOKEN! Проверь файл .env")


async def main():
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    connector = aiohttp.TCPConnector(ssl=ssl_context)
    http_client = AiohttpClient(connector=connector)

    bot = Bot(token=token)
    bot.api.http_client = http_client

    await start.start_func(bot)
    await atach.atach_func(bot)
    action.action_func(bot)

    await bot.run_polling()


if __name__ == "__main__":
    asyncio.run(main())