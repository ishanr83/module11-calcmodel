from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional
from datetime import datetime

class CalculationCreate(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")
    type: Literal["Add", "Subtract", "Multiply", "Divide"] = Field(
        ..., description="Operation type"
    )
    
    @field_validator("b")
    @classmethod
    def validate_divisor(cls, v, info):
        if info.data.get("type") == "Divide" and v == 0:
            raise ValueError("Cannot divide by zero")
        return v

class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: Optional[float] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class CalculationUpdate(BaseModel):
    a: Optional[float] = None
    b: Optional[float] = None
    type: Optional[Literal["Add", "Subtract", "Multiply", "Divide"]] = None
