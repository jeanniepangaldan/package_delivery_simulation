# HashTable class using chaining.
class HashTable:
    def __init__(self, initial_capacity=39):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])


    # This function inserts a new object into the hash table.
    def insertIntoHash(self, id, object):
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        # If the ket exists, the values of the object will be updated.
        for value in bucket_list:
            if value[0] == id:
                value[1] = object
                return True

        # If the key does not exist, insert the object to the end of the bucket list.
        key_value = [id, object]
        bucket_list.append(key_value)
        return True


    # This function searches for an object with a matching key in the hash table.
    def searchHash(self, id):
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        # The id is searched to see if it exists in the bucket list.
        for value in bucket_list:
            if value[0] == id:
                return value[1]
        return None

    # This function deletes an object with the matching id from the hash table.
    def deleteFromHash(self, id):
        # get the bucket list where this item will be removed from.
        bucket = hash(id) % len(self.table)
        bucket_list = self.table[bucket]

        # If the id is found in the hash table, the object is deleted.
        for value in bucket_list:
            if value[0] == id:
                bucket_list.remove([value[0], value[1]])

