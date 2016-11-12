class BinarySearch():
    def __init__(self, a, b):
        self.length = a
        self.created_list = self.create_list(a, b)
        
    def create_list(self, a, b):
        my_list = [b]
        for i in range(a-1):
            my_list.append(my_list[i] + b)
        return my_list
    
    def search(self, find):
        result_dict = {}
        first = 0
        last = len(self.created_list) - 1
        found = False
        counter = 0
        find = int(find)
        
        while first <= last and not found:
            counter += 1
            midpoint = (first + last) // 2
            if self.created_list[midpoint] == find:
                result_dict['count'] = counter
                result_dict['index'] = self.created_list.index(find)
                return result_dict
            else:
                if find < self.created_list[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        
        return 'not found'
    
bs = BinarySearch(20,2)
print len(bs.created_list)
print bs.created_list
print bs.search(4)
