from pydantic import BaseModel, Field, model_validator
from typing import Literal, Optional
from datetime import datetime

class CalculationCreate(BaseModel):
    a: float = Field(..., description="First operand")
    b: float = Field(..., description="Second operand")
    type: Literal["Add", "Subtract", "Multiply", "Divide"] = Field(
        ..., description="Operation type"
    )
    
    @model_validator(mode='after')
    def validate_division(self):
        if self.type == "Divide" and self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self

class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: str
    result: Optional[float] = None
    created_at: str
    
    class Config:
        from_attributes = True

class CalculationUpdate(BaseModel):
    a: Optional[float] = None
    b: Optional[float] = None
    type: Optional[Literal["Add", "Subtract", "Multiply", "Divide"]] = None
