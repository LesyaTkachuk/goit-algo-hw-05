class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        search_cell = self.table[key_hash]
        if search_cell is not None:
            new_cell = [i for i in filter(lambda array: array[0] != key, search_cell)]
            self.table[key_hash] = new_cell
            return True
        return None


if __name__ == "__main__":
    # Hash table testing
    H = HashTable(5)

    # insert elements to the table
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    H.insert("cherry", 25)
    H.insert("ananas", 50)
    H.insert("peach", 40)

    print(H.get("apple"))
    print(H.table)

    # delete elements from the table
    H.delete("peach")
    H.delete("ananas")
    H.delete("cherry")

    print(H.table)
