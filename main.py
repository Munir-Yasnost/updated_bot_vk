import asyncio
import os 
from dotenv import load_dotenv
import ssl
import aiohttp
from vkbottle import Bot, API, AiohttpClient
from handlers import start, echo

async def main():
    load_dotenv()

    token = os.getenv('VK_TOKEN')

    if not token:
        raise RuntimeError("Переменна VK_TOKEN не задана")

    ssl_context = ssl.create_default_context()

    http_client = AiohttpClient(connector=aiohttp.TCPConnector(ssl=ssl_context))

    api = API(token=token, http_client=http_client)
    print("Генератор токена:", type(api.token_generator).__name__)
    bot = Bot(api=api)

    await start.start_func(bot)
    # await echo.echo_func(bot)

    await bot.run_polling()

if __name__ == '__main__':
    asyncio.run(main())