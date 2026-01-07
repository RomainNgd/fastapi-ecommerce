from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

class ProductRead(ProductCreate):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
