from sys import argv
from controller import Controller

csv_file = argv[1]

ctrl = Controller(csv_file)
ctrl.login()
