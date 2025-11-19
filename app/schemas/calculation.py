from pydantic import BaseModel, Field, root_validator
from typing import Literal, Optional
from datetime import datetime

class CalculationCreate(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")
    type: Literal["Add", "Subtract", "Multiply", "Divide"] = Field(
        ..., description="Operation type"
    )
    
    @root_validator
    def validate_division(cls, values):
        if values.get("type") == "Divide" and values.get("b") == 0:
            raise ValueError("Cannot divide by zero")
        return values

class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: Optional[float] = None
    created_at: str
    
    class Config:
        from_attributes = True
        orm_mode = True

class CalculationUpdate(BaseModel):
    a: Optional[float] = None
    b: Optional[float] = None
    type: Optional[Literal["Add", "Subtract", "Multiply", "Divide"]] = None
