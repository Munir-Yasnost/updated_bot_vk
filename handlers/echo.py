import sys 
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message

async def echo_func(bot:Bot):
  
    @bot.on.message()
    async def echo_handlers(message:Message):
        text = message.text.lower()

        if 'пароль' in text or 'секрет' in text:
            await message.answer("Я никому не скажу! 🤫")
        else:
            await message.answer(message.text)