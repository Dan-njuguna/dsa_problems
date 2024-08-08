#!/usr/bin/python3

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def add(self, key: int) -> None:
        """Adds a key to the HashSet. If the key already exists in the HashSet, it does nothing.
        
        Parameters:
            key (int): The key to be added to the HashSet.

        Returns:
            None: This function does not return any value.
        """
        bucket_index = key % self.size # Create an index of a related set of objects
        bucket = self.buckets[bucket_index] # Create bucket for each set of related objects
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:    
        """Removes a key from the HashSet. If the key does not exist in the HashSet, it does nothing.
        
        Parameters:
            key (int): The key to be removed from the HashSet.

        Returns:
            None: This function does not return any value.
        """
        bucket_index = key % self.size # Create an index of a related set of objects(Index for each Linked List.)
        bucket = self.buckets[bucket_index] # Create bucket for each set of related objects(Similar to linked list for related object indexes.)
        if key in bucket:
            bucket.remove(key)
    
    def contains(self, key: int) -> bool:
        """Checks whether the HashSet contains a specific key.
        
        Parameters:
            key (int): The key to be checked in the HashSet.

        Returns:
            bool: True if the key exists in the HashSet, False otherwise.
        """
        bucket_index = key % self.size # Create an index of a related set of objects
        bucket = self.buckets[bucket_index] # Create bucket for each set of related objects
        return key in bucket
    
if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(10)
    obj.add(20)
    print(obj.contains(10))  # Output: True
    obj.remove(20)
    print(obj.contains(20)) # Output: False