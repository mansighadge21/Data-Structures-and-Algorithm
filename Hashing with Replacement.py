class HashTable:
    # Initialize hash table
    def __init__(self):
        self.size = 10
        self.hash = [-1] * self.size

    # Insert key with replacement
    def insert(self, key):
        index = key % self.size

        if self.hash[index] == -1:
            self.hash[index] = key
            return

        if self.hash[index] % self.size != index:
            temp = self.hash[index]
            self.hash[index] = key

            print(temp, "is displaced from index", index)

            i = (index + 1) % self.size

            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size

            if self.hash[i] == -1:
                self.hash[i] = temp
            else:
                self.hash[index] = temp
                print("Hash Table is Full!")

        else:
            i = (index + 1) % self.size

            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size

            if self.hash[i] == -1:
                self.hash[i] = key
            else:
                print("Hash Table is Full!")

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
