from fastapi import APIRouter, Request
from app.controller.usersController import get_all_users_controller

router = APIRouter()


@router.get("/api/users", tags=["users"])
async def get_all_users_router(request: Request):
    return await get_all_users_controller(request=request)
