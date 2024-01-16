import random
class RandomizedSet(object):
    
    def __init__(self):
        self.dicti={}
        self.lis=[]
        

    def insert(self, val):
        if val in self.dicti:
            return False
        self.dicti[val]=len(self.lis)
        self.lis.append(val)
        return True
        

    def remove(self, val):
        if not val in self.dicti:
            return False
        last_elem_in_list = self.lis[-1]
        index_of_elem_to_remove = self.dicti[val]

        self.dicti[last_elem_in_list] = index_of_elem_to_remove
        self.lis[index_of_elem_to_remove] = last_elem_in_list
        self.lis[-1] = val
        self.lis.pop()
        self.dicti.pop(val)
        return True
        

    def getRandom(self):
        return random.choice(self.lis)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
