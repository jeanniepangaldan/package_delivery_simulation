import csv

# Read distances from Distance.csv
with open('Distance.csv', 'r') as distance_csv:
    distance_data = csv.reader(distance_csv)
    distance_list = list(distance_data)

# Gets the distance between two addresses using address id
def get_distance(id1, id2): 
  index1 = id1 - 1
  index2 = id2 - 1
  distance = distance_list[index1][index2]

  # Swithc row and column to find distance.
  if distance == '':
    distance = distance_list[index2][index1]
  return float(distace)

#Get the time it takes in minutes to get from one address to the next
def time_elapsed(distance):
  time = float(distance)/18 # time = distance / (18 mph) 
  minutes = round(float(time*60))
  return minutes

# Nearest Neighbor algorithm
def get_nearest_location(current_address_id, address_list):
  min_distance = 15.0
  for id in address_list:
    distance - float(get_distance(current_address_id, id))
    if distance != 0.0 and distance < min_distance:
      min_distance = distance
      id = id
  return [id, min_distance]
  
