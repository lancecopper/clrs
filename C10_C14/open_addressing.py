import math, random
from hash_table import generate_big_prime, random_hash_function, Node

def random_hash_function1(m):
    p = generate_big_prime()
    a = random.randint(1, p)
    b = random.randint(0, p)
    def func(k):
        temp = ((a * k + b) % p) % m
        if not temp % 2:
            temp = (temp + 1) % m
        return temp
    return func

def opening_addressing_hash_function(m):
    '''
    双重散列(double hashing)采用如下形式的散列函数: 
    h(k,i) = (h(k) + i*h2(k)) mod m, 
    为了保证散列的均匀，h2(k)必须要与m互素，
    这里采用的策略就是，取m为2的幂，并保证h2总产生奇数。
    '''
    h1 = random_hash_function(m)
    h2 = random_hash_function1(m)
    def func(k, i):
        return (h1(k) + i * h2(k)) % m
    return func

class OpenAddressingHashTable():
    def __init__(self, m, data = []):
        if (m - pow(2, int(math.log(m, 2)))) or m < 2:
            raise ValueError("the scale of OpenAddressingHashTable \
                must be power of 2!")
        self.m = m
        self._slots = []
        for i in range(m):
            self._slots.append(None)
        self.hash_function = opening_addressing_hash_function(m)
        for single_data in data:
            self.insert(single_data)

    def insert(self, x):
        i = 0
        while i < self.m:
            j = self.h(x.key, i)
            if self._slots[j] is None:
                self._slots[j] = x
                return j
            else:
                i += 1
        raise IndexError("open addressing hash table overflow")

    def search(self, k):
        i = 0
        j = self.h(k, i)
        while not (self._slots[j] is None or i == self.m):
            if self._slots[j].key == k:
                return self._slots[j]
            i += 1
            j = self.h(k, i)
        return None

    '''
    def search(self, k):
        i = 0
        j = self.h(x.key, i)
        while not (self._slots[j] is None or i == self.m):
            if self._slots[j] == x.key:
                return x
            i += 1
            j = self.h(x.key, i)
        return None
    '''

    def __getitem__(self, i):
        return self._slots[i]

    def h(self, k, i):
        return self.hash_function(k, i)


if __name__ == "__main__":
    
    data = []
    for i in range(300):
        data.append(Node(i))

    ht = OpenAddressingHashTable(512, data)    

    for k in range(10, 20):
        print(ht.search(k).key)

    for i in range(512):
        if ht[i] is not None:
            print(i, ht[i].key)



