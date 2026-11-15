import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message

async def task(bot:Bot):

    @bot.on.message()
    async def name(message:Message):

        if message.text:
            text = message.text
        else:
            text = 'Вы не ввели текст'

        len_of_message = len(message.attachments)
        await message.answer(f'Кол-во вложений: {len_of_message}. {text}')
