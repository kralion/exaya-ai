from fastapi import FastAPI
from pydantic import BaseModel
from routers.boletos import router as boletos_router
from routers.usuarios import router as usuarios_router
from router.limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded


app = FastAPI()
test_router = APIRouter()
    

app.include_router(boletos_router)
app.include_router(usuarios_router)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@test_router.get("/test")
async def test():
    return {"message": "Hello, World"}

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
       return {"item_price": item.price, "item_id": item_id}



