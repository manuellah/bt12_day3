def find_missing(list1, list2):
    if not list1 and not list2:
        return 0
    elif list1 == list2:
        return 0
    elif not (isinstance(list1, list) or isinstance(list1, list)):
        return 0
    elif len(list1) > len(list2):
        set_difference = set(list1) - set(list2)
    elif len(list2) > len(list1):
        set_difference = set(list2) - set(list1)
    else:
        return 0
    
    return set_difference[0]


class BinarySearch(list):
    def __init__(self, a, b):
        try:
            self.length = a
            self.created_list = self.create_list(a, b)
            list.__init__(self, self.created_list)
        except TypeError:
            self.created_list = []
            list.__init__(self, self.created_list)
        
    def create_list(self, a, b):
        my_list = [b]
        for i in range(a-1):
            my_list.append(my_list[i] + b)
        return my_list
    
    def search(self, find):
        find = int(find)
        result_dict = {}
        first = 0
        last = len(self.created_list) - 1
        found = False
        counter = 0
        if not self.created_list:
            return "invalid input"
        elif find not in self.created_list:
            return {'count': counter, 'index': -1 }
        
        while first <= last and not found:
            midpoint = (first + last) // 2
            if self.created_list[midpoint] == find or self.created_list[first] ==\
            find or self.created_list[last] == find: 
                found = True
            
            else:
                if find < self.created_list[midpoint]:
                    last = midpoint - 1
                    counter += 1
                else:
                    first = midpoint + 1
                    counter += 1
        
    
        return {'count': counter, 'index': self.created_list.index(find)}
    
print BinarySearch(20, 2).search(40)