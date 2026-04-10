import mysql.connector
con = mysql.connector.connect(
	host="localhost",
	user = "root",
	password="root",
	database="niss"
)
if con:
	print("connector")
else:
	print("not connected")