import uuid
from datetime import datetime
from typing import Optional, Text

from pydantic import BaseModel, Field, ConfigDict, EmailStr, PositiveInt
from decimal import Decimal

from pygments.lexer import default


class CategoryCreate(BaseModel):
    """
    Модель для создания и обновления категории.
    Используется в POST и PUT запросах.
    """
    name: str = Field(..., min_length=3, max_length=50,
                      description="Название категории (3-50 символов)")
    parent_id: int | None = Field(None, description="ID родительской категории, если есть")


class Category(BaseModel):
    """
    Модель для ответа с данными категории.
    Используется в GET-запросах.
    """
    id: int = Field(..., description="Уникальный идентификатор категории")
    name: str = Field(..., description="Название категории")
    parent_id: int | None = Field(None, description="ID родительской категории, если есть")
    is_active: bool = Field(..., description="Активна ли категория")

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    price: Decimal = Field(...,max_digits=10, decimal_places=2)
    image_url: str = Field(..., max_length=200)
    stock: int = Field(..., ge=0)
    is_active: bool = Field(default = True)
    category_id: int



class Product(BaseModel):
    id: int = Field(..., description="Уникальный идентификатор продукта")
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    price: Decimal = Field(..., max_digits=10, decimal_places=2)
    image_url: str = Field(..., max_length=200)
    stock: int = Field(..., ge=0)
    is_active: bool = None
    category_id: Optional[int] = None



class UserCreate(BaseModel):
    email: EmailStr = Field(description="Email пользователя")
    password: str = Field(min_length=8, description="Пароль (минимум 8 символов)")
    role: str = Field(default="buyer", pattern="^(buyer|seller)$", description="Роль: 'buyer' или 'seller'")


class User(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    role: str
    model_config = ConfigDict(from_attributes=True)

class RefreshTokenRequest(BaseModel):
    refresh_token: str


class ReviewCreate(BaseModel):
    product_id: PositiveInt = Field(description="Id товара")
    comment:Optional[str] = Field(default=None)
    grade: PositiveInt = Field(ge=1, le=5, description="Оценка должна иметь значение от 1 до 5")



class Review(BaseModel):
    id: PositiveInt
    user_id: PositiveInt
    product_id: PositiveInt
    comment:str
    comment_date:datetime = Field(default_factory=datetime.now)
    grade: PositiveInt = Field(ge=1, le=5, description="Оценка должна иметь значение от 1 до 5")
    is_active: bool = Field(default=True)