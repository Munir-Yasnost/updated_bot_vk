import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message

async def start_func(bot:Bot):

    @bot.on.message(text = 'start')
    async def start_hendler(message:Message):
        await message.answer('Привет привет')

    @bot.on.message(text = 'help')
    async def help_handler(message:Message):
        await message.answer('Я пока ничего не умею')
