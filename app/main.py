from fastapi import FastAPI
from app.database import engine, Base
from app.api import products, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API")

app.include_router(products.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"status": "API up and running very good🚀"}

    
