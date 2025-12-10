from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from typing import List 

from .. import models, schemas 
from ..database import get_db 

router = APIRouter ( 
    prefix = "/products",
    tags = ["products"] 
)
# CREATE
@router.post("/", response_model=schemas.ProductPublic, status_code=status.HTTP_201_CREATED) 
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)): 
    db_product = models.Product(name = product.name, price = product.price, in_stock = product.in_stock) 
    db.add(db_product) 
    db.commit()
    db.refresh(db_product) 
    return db_product 

# READ ALL 
@router.get("/", response_model = List[schemas.ProductPublic]) 
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# REAL ONE 
@router.get("/{product_id}", response_model = schemas.ProductPublic) 
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product: 
        raise HTTPException(status_code = 404, detail = "Product not found!") 
    return product 

# UPDATE 
@router.put("/{product_id}", response_model=schemas.ProductPublic)
def update_product(product_id: int, updated: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = updated.name
    product.price = updated.price
    product.in_stock = updated.in_stock
    db.commit()
    db.refresh(product)
    return product

# DELETE
@router.delete("/{product_id}", response_model = schemas.ProductPublic)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code = 404, detail = "Product not found")
    deleted = product
    db.delete(product)
    db.commit()
    return deleted
