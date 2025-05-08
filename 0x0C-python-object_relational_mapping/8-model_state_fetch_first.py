import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
	engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()
	state = session.query(State).first()
	if state is None:
		print("Nothing")

	print("{}: {}".format(state.id, state.name))