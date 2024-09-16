from typing import Annotated

from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/items",
    tags=['items'],
)


@router.get("/")
async def list_items(
        page_no: Annotated[int, Query(description='页码')] = 1,
        page_size: Annotated[int, Query(description='页面数量')] = 10
):
    return [
        {'id': 1, 'name': 'abc'},
        {'id': 2, 'name': 'def'},
    ]

@router.get("/{id}")
async def read_item(id: int):
    """
    Path parameters example
    :param id:
    :return:
    """
    return {
        'id': id
    }

