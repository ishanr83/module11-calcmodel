from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime

class Calculation(Base):
    __tablename__ = "calculations"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    a: Mapped[float] = mapped_column(Float, nullable=False)
    b: Mapped[float] = mapped_column(Float, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    result: Mapped[float] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    def calculate(self) -> float:
        operations = {
            "Add": lambda: self.a + self.b,
            "Subtract": lambda: self.a - self.b,
            "Multiply": lambda: self.a * self.b,
            "Divide": lambda: self.a / self.b if self.b != 0 else None,
        }
        return operations.get(self.type, lambda: None)()
