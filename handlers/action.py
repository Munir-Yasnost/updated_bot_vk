from vkbottle.bot import Message


def action_func(bot):
    @bot.on.message(action = 'chat_invite_user')
    async def invite_user(message:Message):

        user_id = message.action.member_id
        users = await message.ctx_api.users.get(user_ids = user_id)
        user = users[0]

        await message.answer(f'Добро пожаловать в чат, {user.first_name}! 🏡✨')


    @bot.on.message(action = 'chat_kick_user')
    async def kick_user(message:Message):
        await message.answer('Пока пока! 👋')


    @bot.on.message(action = 'chat_title_update')
    async def change_chat_name(message:Message):
        await message.answer('Хорошее название! ✨📝')


    @bot.on.message(action = 'chat_pin_message')
    async def pin_message(message:Message):
        await message.asnwer('Сообщение закпреплено! 📌✉️')


    @bot.on.message(action = 'chat_unpin_message')
    async def unpin_message(message:Message):
        await message.answer('Сообщение откреплено!')