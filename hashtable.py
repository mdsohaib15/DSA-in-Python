class HashTable:
    def __init__(self):
        self.MAX= 100
        self.arr = [[] for i in  range(self.MAX)]

    def gethash(self,key):
        hashsum=0
        for char in key:
            hashsum += ord(char)
        return hashsum % self.MAX
            
    def __setitem__(self,key,value):
        h  = self.gethash(key)
        found = False
        # loop is successfuly run when the key already exist, if key not exist if condition executed
        for index,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key,value)
                found = True
        # this condition is executind when key is not found in an array
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.gethash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self,key):
        h = self.gethash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                print('del:', element)
                del self.arr[h][index]

hash = HashTable()
hash['muhammad'] = 40
hash['sohaib'] = 44
print(hash['muhammad'])
print(hash.arr)
del hash['sohaib']
print(hash.arr)