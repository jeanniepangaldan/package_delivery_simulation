import csv

# Read distances from Distance.csv
with open('Distance.csv', 'r') as distanceCSV:
    distanceData = csv.reader(distanceCSV)
    distanceList = list(distanceData)
    #for distance in distanceList:
    #    print(distance)

# Read Addresses from Address.csv
with open('Address.csv', 'r') as addressCSV:
    addressData = csv.reader(addressCSV)
    next(addressData)
    addressList1 = list(addressData)

# Gets the distance between two addresses using address ID.
def getDistance(firstAddressID, secondAddressID):
    firstAddressIndex = firstAddressID - 1
    secondAddressIndex = secondAddressID - 1
    distance = distanceList[firstAddressIndex][secondAddressIndex]
    # Switch row and column to find distance.
    if distance == '':
        distance = distanceList[secondAddressIndex][firstAddressIndex]
    return float(distance)


# Get the time it takes in minutes to get from one address to the next.
def timeElapsedForDelivery(distance):
    time = float(distance)/18 # time = distance / (18 mph)
    minutes = round(float(time*60))
    return minutes


# NEAREST NEIGHBOR ALGORITHM.
def getNearestLocation(currentAddressId, addressList):
    minDistance = 15.0
    for addressId in addressList:
        distance = float(getDistance(currentAddressId, addressId))
        if distance != 0.0 and distance < minDistance:
            minDistance = distance
            addressID = addressId
    return [addressID, minDistance]


