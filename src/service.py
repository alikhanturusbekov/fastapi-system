from typing import Mapping

from src.database import example, database


async def get_all() -> Mapping:
    select_query = example.select()

    return await database.fetch_all(select_query)


async def get_by_id(example_id: int) -> Mapping:
    select_query = example.select().where(example.c.id == example_id)

    return await database.fetch_one(select_query)


async def insert(example_id: int, title: str) -> Mapping:
    insert_query = (
        example.insert()
        .values(id=example_id, title=title)
        .returning(example)
    )

    return await database.fetch_one(insert_query)


async def update(example_id: int, title: str) -> Mapping:
    update_query = (
        example.update()
        .values(id=example_id, title=title)
        .where(example.c.id == example_id)
        .returning(example)
    )

    return await database.fetch_one(update_query)


async def delete(example_id: int) -> None:
    update_query = (
        example.delete()
        .where(example.c.id == example_id)
    )

    await database.execute(update_query)