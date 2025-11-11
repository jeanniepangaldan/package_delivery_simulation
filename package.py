import csv
from hashtable import HashTable

all_packages = []
truck_one_packages = [1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 34, 39, 40]
truck_two_packages = [5, 6, 8, 9, 10, 11, 17, 18, 23, 30, 31, 32, 36, 37, 38]
truck_three_packages = [2, 3, 4, 12, 22, 24, 25, 26, 27, 28, 33, 35]
delayed_packages = [6, 25, 28, 33]

class Package:

  # Create package
  def __init__(self, id, package_address, city, state, zip, deadline, weight, time_delivered, truck, status):
    self.id = id
    self.package_address = package_address
    self.city = city
    self.state = state
    self.zip = zip
    self.deadline = deadline
    self.weight = weight
    self.time_delivered = time_delivered
    self.truck = truck
    self.status = status

  def __str__(self):
    return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.package_address, self.city, self.state, 
                                                       self.zip, self.deadline, self.weight, self.time_delivered, 
                                                       self.truck, self.status)
  # Update delivery time of package.
  def update_time(self, time_delivered):
    self.time_delivered - time_delivered

  # Update truck of package.
  def update_truck(self, truck_id):
    self.truck = trcuk_id

  # Update package status
  def update_status(self, status): 
    self.status = status

  # Update package address
  def updated_address(self, package_address):
    self.package_address = package_address

  # Update package zip
  def update_zip(self, zip):
    self.zip = zip

  # Get deadline of package
  def get_deadline(self):
    return self.deadline

  # Get status of package
  def get_status(self):
    return self.status

  # Get address of package
  def get_address(self):
    return self.package_address

  # Get time the package was delivered
  def get_time(self):
    return self.time_delivered

  # Get city package was delivered to
  def get_city(self):
    return self.city

  # Get weight of package
  def get_weight(self):
    return self.weight

  # Get zip of package address
  def get_zip(self):
    return self.zip


  # Laods the package data from the CSV file to a hashtable
  def load_package_data(file):
    with open(file) as package_csv:
      package_data = csv.reader(package.csv, delimiter=',')
      next(packate_data)
      for package in package_data:
        id = int(package[0])
        package_address = package[1]
        city = package[2]
        state = package[3]
        zip = package[4]
        deadline = package[5]
        weight = package[6]
        time_delivered = 'Not Delivered Yet'
        truck = ''
        status = ''
        
        package1 = Package(id, package_address, city, state, zip, deadline, weight, time_delivered, truck, status)
        package_hash_table.insert_hash(id, package1)
        
  package_hash_table = HashTable()

  # Load data from Package.csv
  load_package_data('Package.csv')

  # Loops through hash table and prints each package
  def print_hash():
    for i in range(len(package_hash_table.table) + 1):
      print("{}".format(package_hash_table.search_hash(i+1)))

  # Get list with all package IDs
  def all_package_list():
    for i in range(len(package_hash_table.table) + 1):
      id = i + 1
      all_packages.append(id)
    return all_packages



  # Initalize all packages. 
  def initialize_packages():

    # Set all packages status to "At the hub"
    for id in all_packages:
      package = package_hash_table.search_hash(id)
      status = 'At the hub'
      package.update_status(status)

    # Set delayed package status' to "Delayed"
    for id in all_packages:
      package = package_hash_table.search_hash(id)
      status = "Delayed"
      package.update_status(status)

    # Set truck to 1 for each package in this list.
    for id in truck_one_packages:
      package = package_hash_table.search_hash(id)
      package.updated_truck(1)

    # Set truck to 2 for each package in this list.
    for id in truck_two_packages:
      package = package_hash_table.search_hash(id)
      package.updated_truck(2)

    # Set truck to 3 for each package in this list.
    for id in truck_three_packages:
      package = package_hash_table.search_hash(id)
      package.updated_truck(3)


  # Updates package 9 address to '410 S State St'
  def update_package_nine():
    package = package_hash_table.search_hash(9)
    address = '410 S State St'
    zip = '84111'
    package.update_address(address)
    package.update_zip(zip)
    return None

  # Look up package
  def search_package(id):
    package = package_hash_table.search_hash(id)
    address = package.get_address()
    deadline = package.get_deadline()
    city = package.get_city()
    zip = package.get_zip()
    weight = package.get_weight()
    status = package.get_status()
    delivery_time = package.get_time()
    string = (f"Package {packageId}: \t Address: {packageAddress} \t Deadline: {deadline} \t City: {city} \t Zip: {zip} \t Weight: {weight} kilo \t Status: {status} \t Delivery Time: {deliveryTime}")
    return string
    



















  
