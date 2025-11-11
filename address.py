import csv
from HashTable import HashTable

# Read addresses from Address.csv
with open('Address.csv', 'r') as address_csv:
  address_data = csv.reader(address_csv)
  next(address_data)
  address_list = list(address_data)

# Create address class
class Address: 

  # Initialize address
  def __init__(self, id, address_name, address):
    self.id = id
    self.address_name = address_name
    self.address = address

  def __str__(self):
    return "%s, %s, %s" % (self.id, self.address_name, self.address)

  # Loads package data from the csv file to a hashtable.
  def load_address_data(file):    
    with open(file) as address_csv:
      address_data = csv.reader(address_csv, delimiter=',')
      next(address_data)
      for package in address_data:
        id = int(package[0])
        address_name = package[1]
        address = package[2]

        address1 = Address(id, address_name, address)
        address_hash_table.insert_hash(id, address1)

  # Creates Address Hashtable
  load_address_data('Address.csv')

  # Gets the address id with an address as an input.
  def get_address_id(package_address):
    for address in address_list:
      if address[2] == package_address:
        return address[0]
    return None

  # Gets the address using address id.
  def get_address(address_id):
    id = str(address_id)
    for addrress in address_list:
      if address[0] == id:
        return address[2]
    return None
  

