from fastapi import Request
from app.services.userService import get_all_users_service


async def get_all_users_controller(request: Request):
    pool = request.app.state.pool

    async with pool.acquire() as conn:
        return await get_all_users_service(conn)
