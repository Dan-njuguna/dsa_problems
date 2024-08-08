#!/usr/bin/python3

class MyhashMap():
    def __init__(self) -> None:
        self.hashtable_size = 1000
        self.hashtable = [[] for _ in range(self.hashtable_size)]

    def put(self, key: int, value: int) -> None:
        hash_index = key % self.hashtable_size
        self.bucket = self.hashtable[hash_index]


    def get(self, key: int) -> int:
        pass

    def remove(self, key: int) -> None:
        pass