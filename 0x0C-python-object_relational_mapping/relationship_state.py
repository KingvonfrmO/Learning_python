from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class State(Base):
	__tablename__ = "states"
	id = Column(Integer, nullable = False, primary_key = True, unique = True, autoincrement = True)
	name = Column(String(128), nullable = False)
	cities = relationship("City", backref="state")