import MySQLdb
import sys

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	database_name = sys.argv[3]
	state_name = sys.argv[4]

	db = MySQLdb.connect(
		host = "localhost",
		port = 3306,
		user = username,
		passwd = password,
		db = database_name
	)

	cursor = db.cursor()
	cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id", (state_name,))

	rows = cursor.fetchall()

	print(", ".join([row[0] for row in rows]))
	cursor.close()
	db.close()