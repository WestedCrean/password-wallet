from typing import List

from fastapi import APIRouter, Depends

from app.schemas import (
    ExceptionResponseSchema,
    GetPasswordListResponseSchema,
    CreatePasswordRequestSchema,
    CreatePasswordResponseSchema,
)
from app.services import passwordService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAuthenticated,
)

password_router = APIRouter()


@password_router.get(
    "",
    response_model=List[GetpasswordListResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def get_password_list(limit: int = 10, prev: int = None):
    return await passwordService().get_password_list(limit=limit, prev=prev)


@password_router.post(
    "",
    response_model=CreatepasswordResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def create_password(request: CreatepasswordRequestSchema):
    return await passwordService().create_password(**request.dict())