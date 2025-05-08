import MySQLdb
import sys

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	database_name = sys.argv[3]

	db = MySQLdb.connect(
		host = "localhost",
		port = 3306,
		user = username,
		passwd = password,
		db = database_name
	)

	cursor = db.cursor()
	cursor.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id = cities.state_id ORDER BY id;")

	rows = cursor.fetchall()
	for row in rows:
		print(row)

	cursor.close()
	db.close()