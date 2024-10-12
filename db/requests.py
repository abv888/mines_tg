import json
from os import getenv

# from requests import session
from sqlalchemy import select, update, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.attributes import flag_modified

from .models import User

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def admin_add_permission_to(
        session: AsyncSession,
        tg_username: str
):
    query = (
        update(
            User
        )
        .where(
            User.username == tg_username
        )
        .values(
            permission=True
        )
    )
    await session.execute(query)
    await session.commit()


async def check_user_existence(
        session: AsyncSession,
        tg_id: int
):
    query = (
        select(
            User
        )
        .where(
            User.telegram_id == tg_id
        )
    )
    result = await session.execute(query)
    return (result.scalar() is not None) or (tg_id == getenv('ADMIN_ID'))

async def check_permission(
        session: AsyncSession,
        tg_username: str
):
    query = (
        select(
            User
        )
        .where(
            User.username == tg_username
        )
    )
    result = await session.execute(query)
    return result.scalar().permission or tg_username == getenv('ADMIN')

async def get_localization_for_user(
        session: AsyncSession,
        user_id: int
):
    query = (
        select(
            User
        )
        .where(
            User.telegram_id == user_id
        )
    )
    result = await session.execute(query)
    return result.scalar().localization

# async def set_localization_for_user(
#         session: AsyncSession,
#         user_id: int,
#         localization: str
# ):
#     query = (
#         update(
#             User
#         )
#         .where(
#             User.telegram_id == user_id
#         )
#         .values(
#             localization=localization
#         )
#     )
#     await session.execute(query)
#     await session.commit()