from pydantic import BaseModel 
from typing import Optional 

class ProductBase(BaseModel):
    name: str 
    price: float 
    in_stock: Optional[bool] = True 

class ProductCreate(ProductBase):
    pass 

class ProductPublic(ProductBase):
    id: int 

    class Config:
        orm_mode = True