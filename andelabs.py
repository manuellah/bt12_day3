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
        
        result_dict['count'] = 3
        result_dict['index'] = -1
        return result_dict
    
