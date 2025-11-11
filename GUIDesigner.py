import threading
import PySimpleGUI as psg
from Package import packageHashTable, initializePackages, searchPackage
from Truck import truckOne, truckTwo, truckThree, deliverPackages

# Builds GUI with PySimpleGUI.
def buildGUI():
    initializePackages()

    truckOneDistance = truckOne.getTruckDistance()
    truckTwoDistance = truckTwo.getTruckDistance()
    truckThreeDistance = truckThree.getTruckDistance()
    totalDistance = truckOneDistance + truckTwoDistance + truckThreeDistance

    truckOnePackages = truckOne.getTruckPackages()
    truckTwoPackages = truckTwo.getTruckPackages()
    truckThreePackages = truckThree.getTruckPackages()


    # Truck 1 Layout
    truckOneColumnLayout = [
        [
            psg.Text(f"Truck {truckOne.getTruckId()}", font=("Helvetica", 20, "bold")),
            psg.Text(f"Total Packages: {truckOne.getNumPackages()}")
        ],
        [psg.Text(f"Total Distance: {truckOne.getTruckDistance()} miles",key="truckOneDistanceText")],
        [psg.Text(" ")],
        [psg.Text(f"Last Location:", key="lastLocationOne")],
        [psg.Text(f"Current Location: At the hub",key="currentLocationOne")],
        [psg.Text(f"Truck Status: {truckOne.getTruckStatus()}", key="statusOne")],
        [psg.Text(" ")]
    ]


    # Loads each packageId and status for truck 1.
    for packageId in truckOnePackages:
        thisPackage = packageHashTable.searchHash(packageId)
        status = thisPackage.getPackageStatus()
        truckOneColumnLayout.append(
            [psg.Text(f"Package {packageId}: "),
             psg.Text(status, key="statusTextOne" + str(packageId))]
        )


    # Truck 2 Layout
    truckTwoColumnLayout = [
        [
            psg.Text(f"Truck {truckTwo.getTruckId()}", font=("Helvetica", 20, "bold")),
            psg.Text(f"Total Packages: {truckTwo.getNumPackages()}")
        ],
        [psg.Text(f"Total Distance: {truckTwo.getTruckDistance()} miles", key="truckTwoDistanceText")],
        [psg.Text(" ")],
        [psg.Text(f"Last Location:", key="lastLocationTwo")],
        [psg.Text(f"Current Location: At the hub", key="currentLocationTwo")],
        [psg.Text(f"Truck Status: {truckTwo.getTruckStatus()}", key="statusTwo")],
        [psg.Text(" ")]
    ]


    # Loads each packageId and status for truck 2.
    for packageId in truckTwoPackages:
        thisPackage = packageHashTable.searchHash(packageId)
        status = thisPackage.getPackageStatus()
        truckTwoColumnLayout.append(
            [psg.Text(f"Package {packageId}: "),
             psg.Text(status, key="statusTextTwo" + str(packageId))]
        )


    # Truck 3 Layout
    truckThreeColumnLayout = [
        [
            psg.Text(f"Truck {truckThree.getTruckId()}", font=("Helvetica", 20, "bold")),
            psg.Text(f"Total Packages: {truckThree.getNumPackages()}")
        ],
        [psg.Text(f"Total Distance: {truckThree.getTruckDistance()} miles", key="truckThreeDistanceText")],
        [psg.Text(" ")],
        [psg.Text(f"Last Location:", key="lastLocationThree")],
        [psg.Text(f"Current Location: At the hub", key="currentLocationThree")],
        [psg.Text(f"Truck Status: {truckThree.getTruckStatus()}", key="statusThree")],
        [psg.Text(" ")]
    ]


    # Loads each packageId and status for truck 3.
    for packageId in truckThreePackages:
        thisPackage = packageHashTable.searchHash(packageId)
        status = thisPackage.getPackageStatus()
        truckThreeColumnLayout.append(
            [psg.Text(f"Package {packageId}: "),
             psg.Text(status, key="statusTextThree" + str(packageId))]
        )

    # Fourth column layout.
    deliveriesColumn = [
        [psg.Text(f"08:00 AM", key="timeText", font=(20))],
        [psg.Text(f"Total Distance: {totalDistance} miles", key="totalDistanceText")],
        [psg.Text('Delivered Packages:')],
        [psg.Listbox(values=[], size=(100, 100),key="deliveredPackagesListBox")]
    ]


    # Create full layout.
    layout = [
        [psg.Button('Start Deliveries',key="startDeliveriesButton"),psg.Button("Exit", key="exitButton")],
        [psg.Text('Look up package:'), psg.Input(key='searchBar',size=5), psg.Button("Search",key="searchButton"), psg.Text('At time of search:')],
        [psg.Text(' ',key='packageInfo')],
        [
            psg.Column(truckOneColumnLayout, size=(380, 800)),
            psg.VSeparator(),
            psg.Column(truckTwoColumnLayout, size=(380, 800)),
            psg.VSeparator(),
            psg.Column(truckThreeColumnLayout, size=(400, 800)),
            psg.VSeparator(),
            psg.Column(deliveriesColumn, size=(600, 800))
        ],
    ]

    # Make full layout scrollable.
    fullLayout = [
        [psg.Column(layout, size=(1800, 900), scrollable=True)]
    ]

    # Create window.
    global window
    window = psg.Window('Truck Delivery GUI', fullLayout, size=(1800, 900), resizable=True, grab_anywhere=True)

    # Create threads to deliver packages of each truck.
    truckOneThread = threading.Thread(target=deliverPackages, args=(window, truckOne))
    truckTwoThread = threading.Thread(target=deliverPackages, args=(window, truckTwo))
    truckThreeThread = threading.Thread(target=deliverPackages, args=(window, truckThree))

    # Create event loop.
    while True:
        event, values = window.read()

        # End program if user closes window or clicks Exit button.
        if event == psg.WINDOW_CLOSED or event == "exitButton":
            break

        if event == "searchButton":
            packageId = int(window['searchBar'].get())
            if packageId > 0 and packageId < 41:
                string2 = searchPackage(packageId)
                window['packageInfo'].update(string2)
            else:
                window['packageInfo'].update(f"Error. Enter a number 1-40.")

        # Button to start deliveries.
        elif event == "startDeliveriesButton" and window['startDeliveriesButton'].get_text() == "Start Deliveries":

            # Execute threads when start button is clicked.
            truckTwoThread.start()
            truckThreeThread.start()
            truckOneThread.start()


            # Change text of button to Pause Deliveries.
            window['startDeliveriesButton'].update('Pause Deliveries')

        # Click button to pause deliveries.
        elif event == "startDeliveriesButton" and window['startDeliveriesButton'].get_text() == "Pause Deliveries":
            # Change text of button to Resume Deliveries.
            window['startDeliveriesButton'].update("Resume Deliveries")

        # Click button to start deliveries again after being paused.
        else:
            # Change text of button to Pause deliveries.
            window['startDeliveriesButton'].update("Pause Deliveries")

    # Close window.
    window.close()
