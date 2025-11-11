import time
import datetime
from time import sleep

from Address import getAddressId, getAddress
from Distance import getNearestLocation, timeElapsedForDelivery, getDistance
from Package import packageHashTable, updatePackageNineAddress

# Creates Truck class.
class Truck:
    def __init__(self, ID, mileage, packages, numPackages, lastLocation, currentLocation, ready, status):
        self.ID = ID
        self.mileage = mileage
        self.packages = packages
        self.numPackages = numPackages
        self.lastLocation = lastLocation
        self.currentLocation = currentLocation
        self.ready = ready
        self.status = status

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.mileage, self.packages, self.numPackages,
                                               self.lastLocation, self.currentLocation, self.ready,
                                               self.status)

    def updateTruckLastLocation(self, lastLocation):
        self.lastLocation = lastLocation

    def updateTruckCurrentLocation(self, currentLocation):
        self.currentLocation = currentLocation

    def updateNextLocation(self, nextLocation):
        self.nextLocation = nextLocation

    def updateTruckMileage(self, mileage):
        self.mileage = mileage

    def updateTruckReady(self, ready):
        self.ready = ready

    def updateTruckStatus(self, status):
        self.status = status

    def getTruckId(self):
        return self.ID

    def getTruckDistance(self):
        return self.mileage

    def getTruckPackages(self):
        return self.packages

    def getNumPackages(self):
        return self.numPackages

    def getLastLocation(self):
        return self.lastLocation

    def getCurrentLocation(self):
        return self.currentLocation

    def getTruckDistance(self):
        return self.mileage

    def getTruckReady(self):
        return self.ready

    def getTruckStatus(self):
        return self.status


# Packages for each truck.
truckOnePackages = [1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 34, 39, 40]
truckTwoPackages = [5, 6, 8, 9, 10, 11, 17, 18, 23, 30, 31, 32, 36, 37, 38]
truckThreePackages = [2, 3, 4, 12, 22, 24, 25, 26, 27, 28, 33, 35]

# Delayed packages.
delayedPackages = [6, 25, 28, 33]

# Create truck objects
global truckOne
truckOne = Truck(1, 0.0, [1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 34, 39, 40],13,
                 '', '4001 South 700 East','Not Ready','At the hub. No packages delivered.')
truckOneId = truckOne.getTruckId()

global truckTwo
truckTwo = Truck(2, 0.0, [5, 6, 8, 9, 10, 11, 17, 18, 23, 30, 31, 32, 36, 37, 38], 15,
                 '', '4001 South 700 East','Not Ready','At the hub. No packages delivered.')
truckTwoId = truckTwo.getTruckId()

global truckThree
truckThree = Truck(3, 0.0, [2, 3, 4, 12, 22, 24, 25, 26, 27, 28, 33, 35], 12,
                '', '4001 South 700 East','Not Ready', 'At the hub. No packages delivered.')
truckThreeId = truckThree.getTruckId()


# Once a package is delivered, a string will be added to the list.
deliveryList = []

# This function delivers all packages using window and truck object as inputs.
def deliverPackages(window, truck):

    # Time that global clock will start.
    dayStartTime = datetime.datetime.strptime('08:00:00', '%H:%M:%S').time()

    timer = 0


    # Get truck ID.
    truckId = truck.getTruckId()

    # Get packages for truck.
    packages = truck.getTruckPackages()

    # This allows truck 1 to leave hub at 8:01 am.
    if truckId == 1:
        timer1 = 1
        timer2 = 1

    # This allows truck 2 to leave hub at 9:05 am.
    if truckId == 2:
        timer1 = 65
        timer2 = 65

    # This allows truck 3 to leave hub at 9:53 am after truck one returns at 9:52 am.
    if truckId == 3:
        timer1 = 113
        timer2 = 113

    totalDistance = 0.0
    totalTime = 0

    nextLocations = []  # Addresses that packages have not been delivered to.
    deliveredPackages = []  # Packages that have been delivered.
    deliveredLocations = []  # Addresses that packages have already been delivered to.

    # Adds the list of address IDs to the nextLocations list.
    for packageId in packages:
        package = packageHashTable.searchHash(packageId)  # Search hash table for package object using the packageId.
        address = package.packageAddress  # Gets the address of a package.
        addressId = int(getAddressId(address))  # Converts the address to its address ID
        if addressId not in nextLocations:
            nextLocations.append(addressId)

    # As the global clock runs, packages will be delivered.
    while timer < 245:
        if window['startDeliveriesButton'].get_text() == 'Resume Deliveries':
            while window['startDeliveriesButton'].get_text() == 'Resume Deliveries':
                sleep(0.1)

        # Break out of loop once the truck returns to the hub.
        if truck.getCurrentLocation == "Back at Hub":
            print(f"Truck {truckId} returned to hub")
            break

        # Update truck mileage in GUI.
        window['truckOneDistanceText'].update(f"Total Distance: {truckOne.getTruckDistance()} miles")
        window['truckTwoDistanceText'].update(f"Total Distance: {truckTwo.getTruckDistance()} miles")
        window['truckThreeDistanceText'].update(f"Total Distance: {truckThree.getTruckDistance()} miles")

        # Update sum of truck mileage (truck 1 + truck 2 + truck 3) in GUI.
        allTruckDistances = round(truckOne.getTruckDistance() + truckTwo.getTruckDistance() + truckThree.getTruckDistance(),2)
        window['totalDistanceText'].update(f"Total Distance: {allTruckDistances} miles")

        timer += 1
        time.sleep(.1)

        # Updates global clock in GUI as each second passes.
        currentDateTime = datetime.datetime.combine(datetime.date.today(), dayStartTime) + datetime.timedelta(minutes=timer)
        window["timeText"].update(currentDateTime.strftime("%H:%M %p"))

        # Update truck 1 to "Ready" at 8:01 am.
        if timer == 1 and truckId == 1:
            truck.updateTruckReady("Ready")

        # Update truck 2 to "Ready" at 9:05 am.
        if timer == 65 and truckId == 2:
            truck.updateTruckReady("Ready")

        # Update truck 3 to "Ready" at 9:53 am.
        if timer == 113 and truckId == 3:
            truck.updateTruckReady("Ready")

        # Update delayed packages to "At the hub" at 9:05 am.
        if currentDateTime.hour == 9 and currentDateTime.minute == 5 and truckId == 2:
            for packageId in delayedPackages:
                package = packageHashTable.searchHash(packageId)
                if packageId == 6:
                    status = "At the hub"
                    package.updatePackageStatus(status)
                    window["statusTextTwo" + str(packageId)].update(status)
                    print(f"Package {packageId} on truck {truckId} at {currentDateTime.strftime("%H:%M %p")}")
        if currentDateTime.hour == 9 and currentDateTime.minute == 5 and truckId == 3:
            for packageId in delayedPackages:
                package = packageHashTable.searchHash(packageId)
                if packageId != 6:
                    status = "At the hub"
                    package.updatePackageStatus(status)
                    window["statusTextThree" + str(packageId)].update(status)
                    print(f"Package {packageId} on truck {truckId} at {currentDateTime.strftime("%H:%M %p")}")

        # Update package 9 address to "410 S State St" at 10:20 am.
        if currentDateTime.hour == 10 and currentDateTime.minute == 20 and truckId == 2:
            for packageId in truckTwoPackages:
                if packageId == 9:
                    package = packageHashTable.searchHash(9)
                    updatePackageNineAddress()
                    print(f"Package 9 address updated to {package.getPackageAddress()} at {currentDateTime.strftime("%H:%M %p")}")
                    window["statusTextTwo" + str(packageId)].update(f"En route to {package.getPackageAddress()}")


        # Start deliveries.
        if len(deliveredPackages) < truck.getNumPackages() and truck.getTruckReady() == "Ready":

            # Once truck is ready, package status will be updated to "En Route"
            for packageId in packages:
                package = packageHashTable.searchHash(packageId)
                status = "En Route"
                package.updatePackageStatus(status)
                string = f"En Route to {package.getPackageAddress()}"
                if truckId == 1:
                    window["statusTextOne" + str(packageId)].update(string)
                if truckId == 2:
                    window["statusTextTwo" + str(packageId)].update(string)
                if truckId == 3:
                    window["statusTextThree" + str(packageId)].update(string)

            # Once truck is ready, truck status will be updated to "Out for delivery"
            truckStatus = "Out for delivery"
            if truckId == 1:
                window['statusOne'].update(f"Truck Status: {truckStatus}")
            if truckId == 2:
                window['statusTwo'].update(f"Truck Status: {truckStatus}")
            if truckId == 3:
                window['statusThree'].update(f"Truck Status: {truckStatus}")

            # Get nearest location from current location.
            currentLocationId = int(getAddressId(truck.getCurrentLocation())) # Get ID of nearest location.
            nearestAddress = getNearestLocation(currentLocationId, nextLocations)
            nearestAddressId = int(nearestAddress[0]) # Get ID of nearest address.

            # Distance of delivery.
            nearestAddressDistance = getDistance(currentLocationId, nearestAddressId)

            # Minutes it takes for delivery from last location.
            timeToDistance = timeElapsedForDelivery(nearestAddressDistance)
            changeInTime = timer - timer1 # Minutes needed for delivery from last location.

            # This lets time pass for each delivery.
            if timeToDistance == changeInTime:
                timer1 = int(timer)

                if nearestAddressId not in deliveredLocations:

                    # Update truck's lastLocation.
                    deliveredLocations.append(nearestAddressId)

                    newCurrentLocationId = int(nearestAddressId)
                    newCurrentAddress = getAddress(newCurrentLocationId)

                    # Update last location
                    truck.updateTruckLastLocation(f"{truck.getCurrentLocation()}")

                    # Update current location.
                    truck.updateTruckCurrentLocation(newCurrentAddress)

                    # Update newLocationsList.
                    newLocationsList = list(filter((nearestAddressId).__ne__, nextLocations))
                    nextLocations = newLocationsList

                    # Update current location and last location in GUI.
                    if truckId == 1:
                        window['currentLocationOne'].update(
                            'Current Location: ' + str(truck.getCurrentLocation()))
                        window['lastLocationOne'].update('Last Location: ' + str(truck.getLastLocation()))
                    if truckId == 2:
                        window['currentLocationTwo'].update(
                            'Current Location: ' + str(truck.getCurrentLocation()))
                        window['lastLocationTwo'].update('Last Location: ' + str(truck.getLastLocation()))
                    if truckId == 3:
                        window['currentLocationThree'].update(
                            'Current Location: ' + str(truck.getCurrentLocation()))
                        window['lastLocationThree'].update('Last Location: ' + str(truck.getLastLocation()))

                    # Get time of arrival at location.
                    totalTime = totalTime + timeToDistance
                    packageTime = datetime.datetime.combine(datetime.date.today(),dayStartTime) + datetime.timedelta(minutes=totalTime + timer2)
                    deliveryTime = packageTime.strftime("%H:%M %p") # Time of arrival at location.

                    # Update packages to delivered if package address = current location.
                    for packageId in packages:
                        package = packageHashTable.searchHash(packageId)
                        packageLocation = package.getPackageAddress()
                        if packageLocation == newCurrentAddress and packageId not in deliveredPackages:
                            newPackagesList = list(filter((packageId).__ne__, packages)) # Removes the package from the package list.
                            packages = newPackagesList
                            deliveredPackages.append(packageId) # Add packageId to list of delivered packages.

                            # Update package status
                            package.updatePackageStatus("Delivered")

                            # Update package time
                            package.updateTimeDelivered(f"{deliveryTime}")

                            # Update deliveryList in GUI.
                            status = (f"Package {packageId} delivered to {package.getPackageAddress()} by truck {truckId} "
                                      f"at {package.getTimeDelivered()} (Deliver by {package.getDeadline()})")
                            if status not in deliveryList:
                                deliveryList.append(status)
                            window['deliveredPackagesListBox'].update(deliveryList)
                            print(status)

                            # Update package status in GUI.
                            if truckId == 1:
                                window["statusTextOne" + str(packageId)].update(f"Delivered at {package.getTimeDelivered()} to {package.getPackageAddress()}")
                            if truckId == 2:
                                window["statusTextTwo" + str(packageId)].update(f"Delivered at {package.getTimeDelivered()} to {package.getPackageAddress()}")
                            if truckId == 3:
                                window["statusTextThree" + str(packageId)].update(f"Delivered at {package.getTimeDelivered()} to {package.getPackageAddress()}")

                    # Update truck mileage.
                    nearestAddressDistance = float(nearestAddress[1])
                    totalDistance = round(totalDistance + nearestAddressDistance, 2)
                    truck.updateTruckMileage(totalDistance)

        # Return truck to hub when all packages delivered.
        if truck.getNumPackages() == len(deliveredPackages) and truck.getCurrentLocation() != "Back at Hub":

            # Current Location
            currentLocation = truck.getCurrentLocation()
            currentLocationId = int(getAddressId(currentLocation))

            # Address ID for hub.
            hubId = 1

            # Distance back to hub.
            distanceBackToHub = round(getDistance(hubId, currentLocationId),2)

            # Total distance for truck.
            totalDistance = round(truck.getTruckDistance() + distanceBackToHub,2)

            # Minutes it takes to return to Hub.
            timeToHub = timeElapsedForDelivery(distanceBackToHub)
            changeInTime = timer - timer1


            if timeToHub == changeInTime:
                # Update Last Location in GUI.
                if truckId == 1:
                    window['lastLocationOne'].update(f"Last Location: {currentLocation}")
                if truckId == 2:
                    window['lastLocationTwo'].update(f"Last Location: {currentLocation}")
                if truckId == 3:
                    window['lastLocationThree'].update(f"Last Location: {currentLocation}")

                # Update truck last location.
                truck.updateTruckLastLocation(currentLocation)

                # Update truck mileage.
                truck.updateTruckMileage(totalDistance)

                # Update current location.
                truck.updateTruckCurrentLocation("Back at Hub")

                # Time truck returned to Hub.
                returnTime = currentDateTime.time().strftime("%H:%M %p")

                # Update truck status.
                truckStatus = "Back at the hub. All packages delivered."
                truck.updateTruckStatus(truckStatus)

                # Update Current Location and Truck Status in GUI.
                if truckId == 1:
                    window['currentLocationOne'].update(f"Current Location: Back at the Hub at {returnTime}")
                    window['statusOne'].update(f"Truck Status: {truckStatus}")
                if truckId == 2:
                    window['currentLocationTwo'].update(f"Current Location: Back at the Hub at {returnTime}")
                    window['statusTwo'].update(f"Truck Status: {truckStatus}")
                if truckId == 3:
                    window['currentLocationThree'].update(f"Current Location: Back at the Hub at {returnTime}")
                    window['statusThree'].update(f"Truck Status: {truckStatus}")

