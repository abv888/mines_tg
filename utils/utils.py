async def is_subscriber(bot, channel_id, user_id):
    try:
        subscription = await bot.get_chat_member(channel_id, user_id)
        if subscription.status in ['member', 'administrator', 'creator']:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False