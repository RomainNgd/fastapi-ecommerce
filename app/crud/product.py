from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.models.user import User

def create_product(db: Session, product: ProductCreate, owner: User):
    db_product = Product(
        **product.model_dump(),
        owner_id=owner.id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product
