from fastapi import APIRouter, status, Depends

from app.boards.dependencies import get_board_service
from app.boards.schema import BoardUpsertRequest, BoardResponse
from app.boards.service import BoardService

from typing import List

router = APIRouter(
    prefix="/boards",
    tags=["boards"]
)


@router.post(
    "", # path
    response_model=BoardResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_board(
    request: BoardUpsertRequest,
    service: BoardService = Depends(get_board_service)
):
    return await service.save_board(request)


@router.get(
    "/{board_id}",
    response_model=BoardResponse,
    status_code=status.HTTP_200_OK
)
async def find_board_by_id(
    board_id: int,
    service: BoardService = Depends(get_board_service)
):
    return await service.find_board_by_id(board_id)


@router.get(
    "",
    response_model=List[BoardResponse],
    status_code=status.HTTP_200_OK
)
async def find_all_boards(
    service: BoardService = Depends(get_board_service)
):
    return await service.find_all()


@router.patch(
    "/{board_id}",
    response_model=BoardResponse,
    status_code=status.HTTP_200_OK
)
async def update_board_by_id(
    board_id: int,
    upsert_request: BoardUpsertRequest,
    service: BoardService = Depends(get_board_service)
):
    return await service.update_by_id(board_id, upsert_request)


@router.delete(
    "/{board_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_board_by_id(
    board_id: int,
    service: BoardService = Depends(get_board_service)
):
    await service.delete_by_id(board_id)




