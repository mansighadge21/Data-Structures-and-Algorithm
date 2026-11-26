
class HashTable:
    # Initialize hash table
    def __init__(self):
        self.size = 10
        self.hash = [-1] * self.size

    # Insert key without replacement
    def insert(self, key):
        index = key % self.size
        start = index

        while self.hash[index] != -1:
            index = (index + 1) % self.size

            if index == start:
                print("Hash Table is Full!")
                return

        self.hash[index] = key
        print(key, "inserted at index", index)

    # Display hash table
    def display(self):
        print("\nIndex\tValue")

        for i in range(self.size):
            if self.hash[i] == -1:
                print(i, "\tEmpty")
            else:
                print(i, "\t", self.hash[i])


# Main program
h = HashTable()

n = int(input("Enter number of keys: "))

keys = list(map(int, input("Enter keys separated by spaces: ").split()))

for key in keys[:n]:
    h.insert(key)

h.display()
