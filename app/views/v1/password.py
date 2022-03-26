from typing import List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.schemas import (
    ExceptionResponseSchema,
    GetPasswordListResponseSchema,
    CreatePasswordRequestSchema,
    CreatePasswordResponseSchema,
)
from app.services import PasswordService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAuthenticated,
)

password_router = APIRouter()


@password_router.get(
    "",
    response_model=List[GetPasswordListResponseSchema],
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def get_password_list(request: Request):
    print("REQUEST:")
    print(request.user)
    return await PasswordService().get_password_list(
        user_id=request.user.id,
    )


@password_router.post(
    "",
    response_model=CreatePasswordResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
)
async def create_password(request: Request, data: CreatePasswordRequestSchema):
    return await PasswordService().create_password(
        user_id=request.user.id, **data.dict()
    )
