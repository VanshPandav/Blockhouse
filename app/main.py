from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas

# Create tables in PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI, changed!"}

# Add a new order
@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Get all orders
@app.get("/orders/", response_model=list[schemas.Order])
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()