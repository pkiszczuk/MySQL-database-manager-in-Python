import sys
import database

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
		database.create_database()
	elif option == 2:
		database.show_databases()
	elif option == 3:
		database.used_database()
	elif option == 4:
		database.create_table()
	elif option == 5:
		database.add_column()
	elif option == 6:
		database.show_tables()
	elif option == 9:
		print("Thanks for using BYE!")
		sys.exit()
	else:
		print("Choose number from 1 to 9")