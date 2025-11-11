import csv
from HashTable import HashTable

allPackages = []
truckOnePackages = [1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 34, 39, 40]
truckTwoPackages = [5, 6, 8, 9, 10, 11, 17, 18, 23, 30, 31, 32, 36, 37, 38]
truckThreePackages = [2, 3, 4, 12, 22, 24, 25, 26, 27, 28, 33, 35]
delayedPackages = [6, 25, 28, 33]
class Package:
    def __init__(self, ID, packageAddress, city, state, zip, deadline, weight, timeDelivered, truck, status):
        self.ID = ID
        self.packageAddress = packageAddress
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.timeDelivered = timeDelivered
        self.truck = truck
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.packageAddress, self.city, self.state, self.zip,
                                                       self.deadline, self.weight, self.timeDelivered, self.truck, self.status)

    def updateTimeDelivered(self, timeDelivered):
        self.timeDelivered = timeDelivered

    def updateTruck(self, truckId):
        self.truck = truckId

    def updatePackageStatus(self,status):
        self.status = status

    def updatePackageAddress(self, packageAddress):
        self.packageAddress = packageAddress

    def updateZip(self, zip):
        self.zip = zip

    def getDeadline(self):
        return self.deadline
    def getPackageStatus(self):
        return self.status

    def getPackageAddress(self):
        return self.packageAddress

    def getTimeDelivered(self):
        return self.timeDelivered

    def getCity(self):
        return self.city

    def getWeight(self):
        return self.weight

    def getZip(self):
        return self.zip



# This function loads the package data from the csv file to a hash table.
def loadPackageData(file):
    with open(file) as packageCSV:
        packageData = csv.reader(packageCSV, delimiter=',')
        next(packageData)
        for package in packageData:
            packageId = int(package[0])
            packageAddress = package[1]
            packageCity = package[2]
            packageState = package[3]
            packageZip = package[4]
            packageDeadline = package[5]
            packageWeight = package[6]
            packageTimeDelivered = 'Not Delivered Yet'
            packageTruck = ''
            packageStatus = ''

            package1 = Package(packageId, packageAddress, packageCity, packageState, packageZip, packageDeadline, packageWeight, packageTimeDelivered, packageTruck, packageStatus)
            packageHashTable.insertIntoHash(packageId, package1)

packageHashTable = HashTable()

# Load data from Package.csv
loadPackageData('Package.csv')


# Loops through the hash table and prints each package.
def printHash():
    for i in range(len(packageHashTable.table) + 1):
        print("{}".format(packageHashTable.searchHash(i + 1)))


# Get list will all package IDs.
def allPackageList():
    for i in range(len(packageHashTable.table) + 1):
        packageId = i + 1
        allPackages.append(packageId)
    return allPackages


# When GUI starts, set each package status to "At the hub" unless it is a delayed package.
def initializePackages():
    allPackageList() # Get list of all package IDs.

    # Set all packages to "At the hub"
    for packageId in allPackages:
        package = packageHashTable.searchHash(packageId)
        status = 'At the hub'
        package.updatePackageStatus(status)

    # Set delayed package status to "Delayed"
    for packageId in delayedPackages:
        package = packageHashTable.searchHash(packageId)
        status = 'Delayed'
        package.updatePackageStatus(status)

    # Set truck to 1 for each package in this list.
    for packageId in truckOnePackages:
        package = packageHashTable.searchHash(packageId)
        package.updateTruck(1)

    # Set truck to 2 for each package in this list.
    for packageId in truckTwoPackages:
        package = packageHashTable.searchHash(packageId)
        package.updateTruck(2)

    # Set truck to 3 for each package in this list.
    for packageId in truckThreePackages:
        package = packageHashTable.searchHash(packageId)
        package.updateTruck(3)


# Updates package 9 address to '410 S State St'
def updatePackageNineAddress():
    package = packageHashTable.searchHash(9)
    newAddress = '410 S State St'
    newZip = '84111'
    package.updatePackageAddress(newAddress)
    package.updateZip(newZip)
    return None


# Look up package function.
def searchPackage(packageId):
    package = packageHashTable.searchHash(packageId)
    packageAddress = package.getPackageAddress()
    deadline = package.getDeadline()
    city = package.getCity()
    zip = package.getZip()
    weight = package.getWeight()
    status = package.getPackageStatus()
    deliveryTime = package.getTimeDelivered()
    string = (f"Package {packageId}: \t Address: {packageAddress} \t Deadline: {deadline} \t City: {city} \t Zip: {zip} \t Weight: {weight} kilo \t Status: {status} \t Delivery Time: {deliveryTime}")
    return string
