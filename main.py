import sys

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "helloworld",
	)

my_cursor = mydb.cursor()

def display_menu():
	print()
	print("1.Create database")	#OK
	print("2.Show databases")	#OK
	print("3.Used database")	#OK
	print("4.Create table")		#OK
	print("5.Add column")		#OK
	print("6.Show tables")		#OK
	print("9.Exit")				#OK

def choose_option(option):
	if option == 1:
		create_database()
	elif option == 2:
		show_databases()
	elif option == 3:
		used_database()
	elif option == 4:
		create_table()
	elif option == 5:
		add_column()
	elif option == 6:
		show_tables()
	elif option == 9:
		print("Thanks for using BYE!")
		sys.exit()
	else:
		print("Choose number from 1 to 9")

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

while True:
	display_menu()
	option = int(input())
	choose_option(option)

