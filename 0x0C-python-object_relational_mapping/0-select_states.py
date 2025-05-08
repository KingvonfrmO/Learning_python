import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database_username = sys.argv[3]

db = MySQLdb.connect(
	host = "localhost",
	port = 3306,
	user = username,
	passwd = password,
	db = database_username
)

cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id")

rows = cursor.fetchall()
for row in rows:
	print(row)

cursor.close()
db.close()


