from typing import Optional
from pydantic import BaseModel, Field

class FoodBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    calories: float = Field(..., ge=0)
    protein: float = Field(..., ge=0)
    carbs: float = Field(..., ge=0)
    fats: float = Field(..., ge=0)
    fiber: Optional[float] = Field(0.0, ge=0)
    sugar: Optional[float] = Field(0.0, ge=0)
    sodium: Optional[float] = Field(0.0, ge=0)
    serving_size: float = Field(100.0, ge=0)
    serving_unit: str = Field("g")
    category: str = Field("General")
    diet_type: Optional[str] = Field("Veg")

class FoodCreate(FoodBase):
    is_custom: Optional[bool] = False

class FoodUpdate(BaseModel):
    name: Optional[str] = None
    calories: Optional[float] = None
    protein: Optional[float] = None
    carbs: Optional[float] = None
    fats: Optional[float] = None
    fiber: Optional[float] = None
    sugar: Optional[float] = None
    sodium: Optional[float] = None
    serving_size: Optional[float] = None
    serving_unit: Optional[str] = None
    category: Optional[str] = None
    diet_type: Optional[str] = None

class FoodResponse(FoodBase):
    id: str
    is_custom: bool = False
    created_by: Optional[str] = None
    created_at: Optional[str] = None
