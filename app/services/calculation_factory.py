from abc import ABC, abstractmethod
from typing import Dict, Type

class CalculationStrategy(ABC):
    
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

class AddStrategy(CalculationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a + b

class SubtractStrategy(CalculationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a - b

class MultiplyStrategy(CalculationStrategy):
    def execute(self, a: float, b: float) -> float:
        return a * b

class DivideStrategy(CalculationStrategy):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class CalculationFactory:
    
    _strategies: Dict[str, Type[CalculationStrategy]] = {
        "Add": AddStrategy,
        "Subtract": SubtractStrategy,
        "Multiply": MultiplyStrategy,
        "Divide": DivideStrategy,
    }
    
    @classmethod
    def create(cls, operation_type: str) -> CalculationStrategy:
        strategy_class = cls._strategies.get(operation_type)
        if not strategy_class:
            raise ValueError(f"Unknown operation type: {operation_type}")
        return strategy_class()
    
    @classmethod
    def calculate(cls, operation_type: str, a: float, b: float) -> float:
        strategy = cls.create(operation_type)
        return strategy.execute(a, b)
