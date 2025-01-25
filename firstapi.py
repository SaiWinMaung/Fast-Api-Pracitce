from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="This is our first route")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "Hello from the post route"}


@app.put("/")
async def put():
    return {"message": "Hello from the put route"}


@app.delete("/")
async def delete():
    return {"message": "Hello from the delete route"}


@app.get("/items")
async def list_item():
    return {"message": "List Item route"}


@app.get("/item/{item_id}")
async def get_item(item_id, isset=False):
    if not isset:
        item_id = {"message": f"Item id is {item_id}"}
    return item_id


@app.get("/user/{user_id}/item/{item_id}")
async def get_user(
    item_id: int, user_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."
            }
        )
    return item