class BinarySearch(list):
    
    # initializing the class with provided variables
    def __init__(self, a, b):
        self.length = a
        super(BinarySearch, self).__init__(self)
        self += range(b, (a * b) + 1, b)
        self.arr = self
    

    def search(self, val):
        first = 0
        last = len(self.arr) - 1
        
        found = False
        count = 0
        index = 0
        output = {}
        
        #iterates through variables in search of index while counting iterations
        while first <= last and not found:

            mid = (first + last) // 2
            if self.arr[mid] == val:
                index = mid
                found = True
            else:
                if val < self.arr[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            
            count += 1
        
        output['count'] = count
        output['index'] = index
        return output