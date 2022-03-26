from typing import List

from fastapi import APIRouter, Depends

from app.schemas import (
    LoginRequestSchema,
    LoginResponseSchema,
    ExceptionResponseSchema,
)
from app.services import AuthService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAuthenticated,
)

auth_router = APIRouter()


@auth_router.post(
    "",
    response_model=LoginResponseSchema,
    responses={"401": {"model": ExceptionResponseSchema}},
)
async def login(request: LoginRequestSchema = Depends()):
    return await AuthService().login(**request.dict())
