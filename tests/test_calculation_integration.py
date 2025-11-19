import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.calculation import Calculation
from app.services.calculation_factory import CalculationFactory

TEST_DATABASE_URL = "sqlite:///./test_calculations.db"

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    
    yield session
    
    session.close()
    Base.metadata.drop_all(bind=engine)

class TestCalculationDatabaseIntegration:
    
    def test_create_calculation_in_db(self, db_session):
        calc = Calculation(a=5.0, b=3.0, type="Add")
        calc.result = CalculationFactory.calculate("Add", calc.a, calc.b)
        
        db_session.add(calc)
        db_session.commit()
        db_session.refresh(calc)
        
        assert calc.id is not None
        assert calc.a == 5.0
        assert calc.b == 3.0
        assert calc.type == "Add"
        assert calc.result == 8.0
    
    def test_create_multiple_calculations(self, db_session):
        calculations = [
            {"a": 10.0, "b": 5.0, "type": "Subtract"},
            {"a": 4.0, "b": 3.0, "type": "Multiply"},
            {"a": 20.0, "b": 4.0, "type": "Divide"},
        ]
        
        for calc_data in calculations:
            calc = Calculation(**calc_data)
            calc.result = CalculationFactory.calculate(calc.type, calc.a, calc.b)
            db_session.add(calc)
        
        db_session.commit()
        
        all_calcs = db_session.query(Calculation).all()
        assert len(all_calcs) == 3
        assert all_calcs[0].result == 5.0
        assert all_calcs[1].result == 12.0
        assert all_calcs[2].result == 5.0
    
    def test_query_calculations_by_type(self, db_session):
        for i in range(3):
            calc = Calculation(a=i * 2.0, b=1.0, type="Add")
            calc.result = CalculationFactory.calculate("Add", calc.a, calc.b)
            db_session.add(calc)
        
        calc = Calculation(a=10.0, b=2.0, type="Divide")
        calc.result = CalculationFactory.calculate("Divide", calc.a, calc.b)
        db_session.add(calc)
        
        db_session.commit()
        
        add_calcs = db_session.query(Calculation).filter(Calculation.type == "Add").all()
        assert len(add_calcs) == 3
        
        div_calcs = db_session.query(Calculation).filter(Calculation.type == "Divide").all()
        assert len(div_calcs) == 1
        assert div_calcs[0].result == 5.0
    
    def test_update_calculation(self, db_session):
        calc = Calculation(a=5.0, b=3.0, type="Add")
        calc.result = CalculationFactory.calculate("Add", calc.a, calc.b)
        db_session.add(calc)
        db_session.commit()
        
        calc.a = 10.0
        calc.result = CalculationFactory.calculate(calc.type, calc.a, calc.b)
        db_session.commit()
        
        updated_calc = db_session.query(Calculation).filter(Calculation.id == calc.id).first()
        assert updated_calc.a == 10.0
        assert updated_calc.result == 13.0
    
    def test_delete_calculation(self, db_session):
        calc = Calculation(a=5.0, b=3.0, type="Add")
        db_session.add(calc)
        db_session.commit()
        calc_id = calc.id
        
        db_session.delete(calc)
        db_session.commit()
        
        deleted_calc = db_session.query(Calculation).filter(Calculation.id == calc_id).first()
        assert deleted_calc is None
