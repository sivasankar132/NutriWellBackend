from typing import Optional, List, Literal
from pydantic import BaseModel, Field
from datetime import date as DateType

MealType = Literal["breakfast", "lunch", "dinner", "snack", "Breakfast", "Lunch", "Dinner", "Snacks"]

class MealItemBase(BaseModel):
    food_id: Optional[str] = None
    food_name: str = Field(..., min_length=1)
    quantity: float = Field(1.0, gt=0)
    serving_size: Optional[str] = "1 serving"
    calories: float = Field(..., ge=0)
    protein: float = Field(0.0, ge=0)
    carbs: float = Field(0.0, ge=0)
    fats: float = Field(0.0, ge=0)
    fiber: Optional[float] = Field(0.0, ge=0)

class MealItemCreate(MealItemBase):
    pass

class MealItemUpdate(BaseModel):
    food_name: Optional[str] = None
    quantity: Optional[float] = Field(None, gt=0)
    serving_size: Optional[str] = None
    calories: Optional[float] = Field(None, ge=0)
    protein: Optional[float] = Field(None, ge=0)
    carbs: Optional[float] = Field(None, ge=0)
    fats: Optional[float] = Field(None, ge=0)
    fiber: Optional[float] = Field(None, ge=0)

class MealItemResponse(MealItemBase):
    id: str
    meal_id: str
    created_at: Optional[str] = None

class MealBase(BaseModel):
    meal_type: MealType = Field(..., description="breakfast, lunch, dinner, snack")
    meal_date: Optional[DateType] = None
    notes: Optional[str] = None

class MealCreate(MealBase):
    items: List[MealItemCreate] = Field(default_factory=list)

class MealUpdate(BaseModel):
    meal_type: Optional[MealType] = None
    meal_date: Optional[DateType] = None
    notes: Optional[str] = None

class MealResponse(MealBase):
    id: str
    user_id: str
    total_calories: float = 0.0
    total_protein: float = 0.0
    total_carbs: float = 0.0
    total_fats: float = 0.0
    total_fiber: float = 0.0
    items: List[MealItemResponse] = Field(default_factory=list)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
