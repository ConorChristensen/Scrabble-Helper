class HashTable:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.array = size*[None]
        self.largest_group = 0
        self.largest_group_index = None             #Keeps track of current largest group as each word is added to the table.

    def hash(self, key):
        primes = [3, 37, 79, 131, 181, 239, 293, 359, 421, 479, 557, 613, 673, 743, 821, 881, 953, 1021, 1091, 1163]
        hash_index = 1
        a_prime = 691
        b = (len(key))
        c = 443
        which_prime = -1*b
        if which_prime*-1 > len(primes)-1:
            which_prime += len(primes)
        d = primes[which_prime]
        for i in range(len(key)):
                hash_index *= (ord(key[i])*a_prime*c)
        hash_index = (hash_index) % self.size
        return hash_index

    def add(self, key):
        index = self.hash(key)
        length = len(key)
        if self.array[index] == None:
            self.array[index] = [key]
            self.count += 1
        elif len(self.array[index][0]) != length:
            placed = False
            p=1
            while not placed:
                if self.array[index+p] == None:
                    self.array[index+p] = [key]
                    placed=True
                    if len(self.array[index+p])>self.largest_group:
                        self.largest_group = len(self.array[index+p])
                        self.largest_group_index = index+p
                elif len(self.array[index+p][0]) == length:
                    self.array[index+p].append(key)
                    placed = True
                    if len(self.array[index+p]) > self.largest_group:
                        self.largest_group = len(self.array[index+p])
                        self.largest_group_index = index+p
                p+=1
        else:
            self.array[index].append(key)
            if len(self.array[index]) > self.largest_group:
                self.largest_group = len(self.array[index])
                self.largest_group_index = index


    def __getitem__(self, key):
        index = self.hash(key)
        if self.array[index] == None:
            raise KeyError("Queery does not exist in this dictionary.")
        else:
            if len(self.array[index][0]) != len(key):
                found = False
                length = len(key)
                p=1
                while not found:
                    if self.array[index+p] == None:
                        raise KeyError("Queery does not exist in this dictionary")
                    elif len(self.array[index+p][0]) == length:
                        return self.array[index+p]
                    found = True
                    p+=1
            else:
                return self.array[index]
    def largestGroup(self):
        if self.largest_group_index == None:
            raise IndexError("Error, the Hash Table is empty.")
        else:
            return self.array[self.largest_group_index]
