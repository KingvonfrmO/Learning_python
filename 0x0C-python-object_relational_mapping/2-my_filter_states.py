import MySQLdb
import sys

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
cursor.execute("SELECT * FROM states WHERE name = {} ORDER BY id ".format(state_name))

rows = cursor.fetchall()
for row in rows:
	print(row)

cursor.close()
db.close()

