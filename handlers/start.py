import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message
import random

spisok = ['орел', 'решка']

async def start_func(bot:Bot):

    @bot.on.message(text = 'start')
    async def start_hendler(message:Message):

        user_id = message.from_id
        user = await message.ctx_api.users.get(user_ids=user_id)
        first_name = user[0].first_name

        await message.answer(f'Привет {first_name}!')
        await message.answer('Хочешь сыграть орел и решка? Если хочешь напиши "Играть" ')

    @bot.on.message(text = ['Играть', 'играть'])
    async def orel_and_rehska(message:Message):

        await message.answer('Выбирай орел или решка!')

        @bot.on.message(text = ['орел', 'решка', 'Орел', 'Решка'])
        async def orel_and_rehska_answer(message:Message):
            text = message.text.lower()
            choice = random.choice(spisok)

            if text == choice:
                await message.answer(f'Правильно, я загадал: {choice}')

            elif text != choice:
                await message.answer(f'Неправильно, я загадал: {choice}')


