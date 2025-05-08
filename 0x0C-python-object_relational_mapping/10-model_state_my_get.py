import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == "__main__":
	engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	name = sys.argv[4]
	session = Session()
	states = session.query(State).filter(State.name == name)
	try:
		print(states[0].id)
	except IndexError:
		print("Not Found")
