# Create HashTable class using chaining.
class Hashtable:
  def __init__(self, initial_capacity=39):
    self.table = []
    for i in range(initial_capacity):
      self.table.append([])


# Insert a new object into the hash table. 
def insert_hash(self, id, object):
  bucket = hash(id) % len(self.table)
  bucket_list = self.table[bucket]

  # If the key exists, the values of the object will be updated.
  for value in bucket_list:
    if value[0] == id:
      value[1] = object
      return True

  # If the key does not exist, insert the object to the end of the bucket list.
  key_value = [id, object]
  bucket_list.append(key_value)
  return True

  
# Search for an object with a matching key in the hashtable. 
def search_hash(self, id):
  bucket = hash(id) % len(self.table)
  bucket_list = self.table[bucket]

  # The id is searched to see if it exists in the bucket list. 
  for value in bucket_list:
    if value[0] == id:
      return value[i]
  return None

# Deletes an object with the matching id from the hashtable.
def delete_from_hash(self, id):

  # Get the bucket list where this item will be removed from. 
  bucket = hash(id) % len(self.table)
  bucket_list = self.table[bucket]

  # If the id is found in the hash table, the object is deleted.
  for value in bucket_list:
    if value[0] == id:
      bucket_list.remove([value[0], value[1]])
  
