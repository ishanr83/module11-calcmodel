import pytest
from pydantic import ValidationError
from app.schemas.calculation import CalculationCreate, CalculationRead

class TestCalculationCreate:
    
    def test_valid_add_operation(self):
        data = {"a": 5.0, "b": 3.0, "type": "Add"}
        calc = CalculationCreate(**data)
        assert calc.a == 5.0
        assert calc.b == 3.0
        assert calc.type == "Add"
    
    def test_valid_subtract_operation(self):
        data = {"a": 10.0, "b": 3.0, "type": "Subtract"}
        calc = CalculationCreate(**data)
        assert calc.type == "Subtract"
    
    def test_valid_multiply_operation(self):
        data = {"a": 4.0, "b": 5.0, "type": "Multiply"}
        calc = CalculationCreate(**data)
        assert calc.type == "Multiply"
    
    def test_valid_divide_operation(self):
        data = {"a": 10.0, "b": 2.0, "type": "Divide"}
        calc = CalculationCreate(**data)
        assert calc.type == "Divide"
    
    def test_divide_by_zero_validation(self):
        data = {"a": 10.0, "b": 0.0, "type": "Divide"}
        with pytest.raises(ValidationError) as exc_info:
            CalculationCreate(**data)
        assert "Cannot divide by zero" in str(exc_info.value)
    
    def test_invalid_operation_type(self):
        data = {"a": 5.0, "b": 3.0, "type": "Modulo"}
        with pytest.raises(ValidationError):
            CalculationCreate(**data)
    
    def test_missing_required_fields(self):
        with pytest.raises(ValidationError):
            CalculationCreate(a=5.0)

class TestCalculationRead:
    
    def test_calculation_read_serialization(self):
        from datetime import datetime
        data = {
            "id": 1,
            "a": 5.0,
            "b": 3.0,
            "type": "Add",
            "result": 8.0,
            "created_at": datetime.utcnow()
        }
        calc = CalculationRead(**data)
        assert calc.id == 1
        assert calc.result == 8.0
