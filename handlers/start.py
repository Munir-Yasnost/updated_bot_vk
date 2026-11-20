import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message
import random


async def start_func(bot:Bot):

    @bot.on.message(text = ['start', 'привет', 'Привет'])
    async def start_hendler(message:Message):

        user_id = message.from_id
        user = await message.ctx_api.users.get(user_ids=user_id)
        first_name = user[0].first_name

        await message.answer(f'Привет {first_name}!')


