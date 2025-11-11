import csv
from HashTable import HashTable

# Read Addresses from Address.csv
with open('Address.csv', 'r') as addressCSV:
    addressData = csv.reader(addressCSV)
    next(addressData)
    addressList = list(addressData)

# Creates Address class.
class Address:
    def __init__(self, ID, addressName, address):
        self.ID = ID
        self.addressName = addressName
        self.address = address

    def __str__(self):
        return "%s, %s, %s" % (self.ID, self.addressName, self.address)


# Loads the package data from the csv file to a hash table.
def loadAddressData(file):
    with open(file) as addressCSV:
        addressData = csv.reader(addressCSV, delimiter=',')
        next(addressData)
        for package in addressData:
            addressId = int(package[0])
            addressName = package[1]
            address = package[2]

            address1 = Address(addressId, addressName, address)
            addressHashTable.insertIntoHash(addressId, address1)


# Creates Address HashTable.
addressHashTable = HashTable()


# Load data from Package.csv
loadAddressData('Address.csv')


# Gets the addressId with an address as an input.
def getAddressId(packageAddress):
    for address in addressList:
        if address[2] == packageAddress:
            return address[0]
    return None

# Gets the Address using addressId as an input.
def getAddress(addressId):
    id = str(addressId)
    for address in addressList:
        if address[0] == id:
            return address[2]
    return None
