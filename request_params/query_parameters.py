from fastapi import FastAPI

query_parameters = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@query_parameters.get("/items/")
async def read_item(skip: int = 0, limit: int = 0):
    return fake_items_db[skip:skip + limit]
