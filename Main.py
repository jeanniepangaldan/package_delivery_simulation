# Jeannie Pangaldan, ID: 001219661
# WGU: C950 Project

import csv
from Package import loadPackageData, initializePackages
from GUIDesigner import buildGUI

# Load package data from Package.csv
loadPackageData('Package.csv')

# Read distances from Distance.csv
with open('Distance.csv', 'r') as distanceCSV:
    distanceData = csv.reader(distanceCSV)
    distanceList = list(distanceData)

# Read Addresses from Address.csv
with open('Address.csv', 'r') as addressCSV:
    addressData = csv.reader(addressCSV)
    next(addressData)
    addressList = list(addressData)

# Initialize packages
initializePackages()

# Open GUI
buildGUI()

