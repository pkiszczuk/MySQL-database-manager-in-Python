import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "helloworld",
	)

my_cursor = mydb.cursor()

def create_database():
	print("Name of database:")
	db_name = input()
	sqlStuff = "CREATE DATABASE "+ db_name +""
	try:
		my_cursor.execute(sqlStuff)
	except mysql.connector.errors.DatabaseError:
		print("Database exists")
	
def show_databases():
	my_cursor.execute("SHOW DATABASES")
	for db in my_cursor:
		print(db[0])

def used_database():
	print("What database want you to use?")
	db_name = input()
	sqlStuff = "USE "+ db_name +""
	try:
		my_cursor.execute(sqlStuff)
	except mysql.connector.errors.ProgrammingError:
		print("That database don't exists")

def create_table():
	print("Name of table:")
	tb_name = input()
	sqlStuff = "CREATE TABLE "+ tb_name +"(id INTEGER AUTO_INCREMENT PRIMARY KEY)"
	try:
		my_cursor.execute(sqlStuff)
	except mysql.connector.errors.ProgrammingError:
		print("You don't choose any database")

def add_column():  #WYJĄTKI
	print("In what table want you to add column?")
	tb_name = input()
	print("Name of column:")
	col_name = input()
	print("Type of data in column:")
	col_type = input()
	sqlStuff = "ALTER TABLE "+ tb_name +" ADD "+ col_name +"  "+ col_type
	my_cursor.execute(sqlStuff)

def show_tables():
	try:
		my_cursor.execute("SHOW TABLES")
	except mysql.connector.errors.ProgrammingError:
		print("You don't choose any database")
	for tb in my_cursor:
		print(tb[0])