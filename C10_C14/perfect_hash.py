import math, random
from hash_table import generate_big_prime, random_hash_function, Node

def random_hash_function(m):
    p = generate_big_prime()
    a = random.randint(1, p)
    b = random.randint(0, p)
    def func(k):
        return ((a * k + b) % p) % m
    return func

def random_primary_hash_function(m, data):
    second_slot_nums = []
    for i in range(m):
        second_slot_nums.append(0)
    while True:
        temp_slot_nums = list(second_slot_nums)
        f = random_hash_function(m)
        for single_data in data:
            temp_slot_nums[f(single_data.key)] += 1
        total_slot_num = 0
        for i in temp_slot_nums:
            total_slot_num += pow(i, 2)
        if total_slot_num < m * 4:
            break
    return f

def random_secondary_hash_function(data):
    m = pow(len(data), 2)
    while True:
        suc_flag = True
        f = random_hash_function(m)
        second_slot_keys = []    
        for single_data in data:
            temp = f(single_data.key)
            if temp in second_slot_keys:
                suc_flag = False
                break
            else:
                second_slot_keys.append(single_data.key)
        if suc_flag:
            break
    return f

class Perfect_hash_table():
    def __init__(self, m, data):
        self.m = m
        self._slots = []
        self._primary_slots = []
        self.hash_function = random_primary_hash_function(m, data)
        for i in range(m):
            self._slots.append([])
            self._primary_slots.append(None)        
        for single_data in data:
            self._slots[self.h(single_data.key)].append(single_data)
        for i in range(m):
            if len(self._slots[i]):
                self._primary_slots[i] = Secondary_ht(self._slots[i])

    def search(self, k):
        return self._primary_slots[self.h(k)].search(k)
    def h(self, k):
        return self.hash_function(k)



class Secondary_ht():
    def __init__(self, data = []):
        self.m = pow(len(data), 2)
        self._slots = []
        for i in range(self.m):
            self._slots.append(None)
        self.hash_function = random_secondary_hash_function(data)
        for single_data in data:
            self._slots[self.h(single_data.key)] = single_data

    def search(self, k):
        return self._slots[self.h(k)]

    def h(self, k):
        return self.hash_function(k)



if __name__ == "__main__":
#if True:
    data = []
    for i in range(300):
        data.append(Node(i))
    ht = Perfect_hash_table(len(data), data)
    for k in range(10, 20):
        print(ht.search(k).key)





