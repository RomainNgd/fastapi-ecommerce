from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.product import ProductCreate, ProductRead
from app.crud import product as crud
from app.core.deps import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductRead)
def create(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[ProductRead])
def read_all(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.get("/{product_id}", response_model=ProductRead)
def read_one(
    product_id: int,
    user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
    ):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(404, "Product not found")
    return product

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, product_id)
    if not product:
        raise HTTPException(404, "Product not found")
    return {"deleted": True}
