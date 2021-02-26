from src.common.database import Database
from menu import Menu

__author__ = 'Allen'

Database.initialize()

menu = Menu()

menu.run_menu()
