from typing import Optional, List, Literal
from pydantic import BaseModel, Field

ActivityLevelType = Literal["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"]
DietPreferenceType = Literal["Veg", "Non-Veg", "Eggetarian", "Vegan", "Other"]
GenderType = Literal["Male", "Female", "Other"]
NutritionGoalType = Literal["weight_loss", "weight_gain", "maintenance", "muscle_gain", "healthy_eating"]

class ProfileBase(BaseModel):
    age: Optional[int] = Field(None, ge=1, le=120, description="Age in years (1 - 120)")
    gender: Optional[str] = Field(None, description="Male, Female, or Other")
    height: Optional[float] = Field(None, gt=0, le=300, description="Height in cm (e.g. 175.5)")
    weight: Optional[float] = Field(None, gt=0, le=500, description="Weight in kg (e.g. 70.0)")
    activity_level: Optional[str] = Field("Moderately Active", description="Sedentary, Lightly Active, Moderately Active, Very Active")
    dietary_preference: Optional[str] = Field("Veg", description="Veg, Non-Veg, Eggetarian, Vegan")
    food_preferences: Optional[List[str]] = Field(default_factory=list, description="Preferred cuisines or dishes")
    allergies: Optional[List[str]] = Field(default_factory=list, description="Allergies e.g. Peanuts, Dairy, Gluten")
    medical_or_dietary_restrictions: Optional[List[str]] = Field(default_factory=list, description="Medical/dietary restrictions e.g. Diabetes, High Blood Pressure")
    nutrition_goal: Optional[str] = Field("maintenance", description="Target health goal: weight_loss, weight_gain, maintenance, muscle_gain, healthy_eating")

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class UserProfileUpdateRequest(ProfileBase):
    name: Optional[str] = Field(None, min_length=1, max_length=255, description="User full name")

class ProfileResponse(ProfileBase):
    id: Optional[str] = None
    user_id: str
    bmi: Optional[float] = None
    bmi_category: Optional[str] = None
    bmr: Optional[float] = None
    tdee: Optional[float] = None
    daily_calorie_target: Optional[float] = None
    daily_protein_target: Optional[float] = None
    daily_carbs_target: Optional[float] = None
    daily_fat_target: Optional[float] = None
    daily_water_target_ml: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class UserProfileResponse(BaseModel):
    user_id: str
    email: Optional[str] = None
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    activity_level: Optional[str] = "Moderately Active"
    dietary_preference: Optional[str] = "Veg"
    food_preferences: List[str] = Field(default_factory=list)
    allergies: List[str] = Field(default_factory=list)
    medical_or_dietary_restrictions: List[str] = Field(default_factory=list)
    nutrition_goal: Optional[str] = "maintenance"
    bmi: Optional[float] = None
    bmi_category: Optional[str] = None
    bmr: Optional[float] = None
    tdee: Optional[float] = None
    daily_calorie_target: Optional[float] = None
    daily_protein_target: Optional[float] = None
    daily_carbs_target: Optional[float] = None
    daily_fat_target: Optional[float] = None
    daily_water_target_ml: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
