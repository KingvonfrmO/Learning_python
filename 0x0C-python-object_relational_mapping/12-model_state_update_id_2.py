import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == "__main__":
	engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()

	state = session.query(State).filter(State.id == 2)
	state[0].name = "New Mexico"

	session.commit()