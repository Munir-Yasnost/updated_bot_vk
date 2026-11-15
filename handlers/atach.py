import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message
from vkbottle.tools import PhotoMessageUploader

async def atach_func(bot:Bot):
    @bot.on.message()
    async def atach_handler(message:Message):

        attachments = message.attachments
        
        for attachment in attachments:
            if attachment.type == 'photo':
                
                await message.answer('Это фотография')

            elif attachment.type == 'sticker':

                await message.answer('Это стикер')

            elif attachment.type == 'doc':

                await message.answer('Это документ')

