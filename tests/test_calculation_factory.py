import pytest
from app.services.calculation_factory import (
    CalculationFactory,
    AddStrategy,
    SubtractStrategy,
    MultiplyStrategy,
    DivideStrategy,
)

class TestCalculationStrategies:
    
    def test_add_strategy(self):
        strategy = AddStrategy()
        assert strategy.execute(5, 3) == 8
        assert strategy.execute(-2, 7) == 5
        assert strategy.execute(0, 0) == 0
    
    def test_subtract_strategy(self):
        strategy = SubtractStrategy()
        assert strategy.execute(10, 3) == 7
        assert strategy.execute(5, 10) == -5
        assert strategy.execute(0, 0) == 0
    
    def test_multiply_strategy(self):
        strategy = MultiplyStrategy()
        assert strategy.execute(5, 3) == 15
        assert strategy.execute(-2, 4) == -8
        assert strategy.execute(0, 10) == 0
    
    def test_divide_strategy(self):
        strategy = DivideStrategy()
        assert strategy.execute(10, 2) == 5
        assert strategy.execute(7, 2) == 3.5
        assert strategy.execute(-10, 2) == -5
    
    def test_divide_by_zero(self):
        strategy = DivideStrategy()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            strategy.execute(10, 0)

class TestCalculationFactory:
    
    def test_factory_creates_add_strategy(self):
        strategy = CalculationFactory.create("Add")
        assert isinstance(strategy, AddStrategy)
    
    def test_factory_creates_subtract_strategy(self):
        strategy = CalculationFactory.create("Subtract")
        assert isinstance(strategy, SubtractStrategy)
    
    def test_factory_creates_multiply_strategy(self):
        strategy = CalculationFactory.create("Multiply")
        assert isinstance(strategy, MultiplyStrategy)
    
    def test_factory_creates_divide_strategy(self):
        strategy = CalculationFactory.create("Divide")
        assert isinstance(strategy, DivideStrategy)
    
    def test_factory_invalid_operation(self):
        with pytest.raises(ValueError, match="Unknown operation type"):
            CalculationFactory.create("InvalidOperation")
    
    def test_factory_calculate_convenience_method(self):
        assert CalculationFactory.calculate("Add", 5, 3) == 8
        assert CalculationFactory.calculate("Subtract", 10, 3) == 7
        assert CalculationFactory.calculate("Multiply", 4, 5) == 20
        assert CalculationFactory.calculate("Divide", 10, 2) == 5
    
    def test_factory_calculate_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            CalculationFactory.calculate("Divide", 10, 0)
