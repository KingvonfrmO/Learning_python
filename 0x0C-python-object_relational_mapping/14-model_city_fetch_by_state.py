import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
	engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind = engine)
	session = Session()

	rows = session.query(State.name, City.id, City.name).join(City).all()
	for state_name, city_id, city_name in rows:
		print(f"{state_name}: ({city_id}) {city_name}")
