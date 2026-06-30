from sqlalchemy.ext.asyncio import AsyncSession

from app.boards.repository import BoardRepository
from app.boards.schema import BoardUpsertRequest
from app.boards.models import Board

class BoardService:

    def __init__(self, session: AsyncSession, repository: BoardRepository):
        self.session = session
        self.repository = repository


    async def save_board(self, request: BoardUpsertRequest):

        board = Board(name=request.name)
        try:
            saved_board = await self.repository.save(board)
            await self.session.commit()
            await self.session.refresh(saved_board)
            return saved_board
        except Exception:
            await self.session.rollback()
            raise


    async def find_board_by_id(self, board_id: int):
        return await self.repository.find_by_id(board_id)


    async def find_all(self):
        return await self.repository.find_all()


    async def update_by_id(self, board_id: int, request: BoardUpsertRequest):

        find_board = await self.find_board_by_id(board_id)

        if find_board is None:
            raise ValueError("해당 게시판은 존재하지 않습니다.")

        find_board.name = request.name

        try:
            await self.session.commit()
            await self.session.refresh(find_board)
            return find_board
        except Exception:
            await self.session.rollback()
            raise

    async def delete_by_id(self, board_id: int):
        find_board = await self.find_board_by_id(board_id)

        if find_board is None:
            raise ValueError("해당 게시판은 존재하지 않습니다.")

        try:
            await self.repository.delete(find_board)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise





