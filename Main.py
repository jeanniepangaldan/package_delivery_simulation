import csv
from package import load_package_data, initialize_packages
from gui_designer import build_gui

# Load package data from Package.csv
load_package_data('Package.csv')

# Read dsiatnces from Distance.csv
with open('Distance.csv', 'r') as distance_csv:
  distance_data = csv.reader(distance_csv)
  distance_list = list(distance_data)

# Read addresses from Address.csv
with open('Address.csv', 'r') as address_csv:
  next(address_data)
  address_list = list(address_data)

# Initialize packages
initialize_packages()

# Open GUI
build_gui()
  
  
