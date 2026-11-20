from vkbottle import Bot
from vkbottle.bot import Message
import random

games = {}
spisok = ['орел', 'решка']

async def game_func(bot):


    @bot.on.message(text = ['Играть', 'играть'])
    async def start_game(message:Message):

        choice = random.choice(spisok)
        games[message.from_id] = choice

        await message.answer('Выбирай: орел или решка!')

    @bot.on.message(text = ['орел', 'решка', 'Орел', 'Решка'])
    async def check_choice(message:Message):

        if message.from_id not in games:
            await message.answer('Сначала напиши "Играть", чтобы начать!')
            return

        text = message.text.lower()
        bot_choice = games[message.from_id]

        if text == bot_choice:
            await message.answer(f'Правильно! Я загадал: {bot_choice}')

        else:
            await message.answer(f'Неправильно! Я загадал: {bot_choice}')

        del games[message.from_id]

