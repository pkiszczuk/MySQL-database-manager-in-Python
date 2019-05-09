import sys
import mysql.connector
import menu
import database

while True:
	menu.display_menu()
	option = int(input())
	menu.choose_option(option)

