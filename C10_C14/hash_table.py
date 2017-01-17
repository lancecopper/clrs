import random
import math

def modular_exponentiation(a, b, n):
    c = 0
    d = 1
    bina = bin(b)[2:]
    k = len(bina)
    for i in range(0, k):
        c = 2 * c
        d = (d * d) % n
        if bina[i] == 1:
            c = c + 1
            d = (d * a) % n
    return d

def pseudoprime(n):
    if modular_exponentiation(2, n - 1, n) % n != 1:
        return False
    else:
        return True

def fermat_test(n):
    return pseudoprime(n)

def miller_rabin_test(n, s = 50):
    for j in range(0, s):
        a = random.randint(1, n - 1)
        if witness(a, n):
            return False
    return True

def witness(a, n):
    if not n % 2:
        return False
    t = 0
    u = n - 1
    while not u % 2:
        t += 1
        u //= 2
    x = []
    x.append(modular_exponentiation(a, u, n))

    for i in range(1, t + 1):
        x.append(pow(x[i-1], 2) % n)
        if x[i] == 1 and x[i - 1] != 1 and x[i - 1] != n - 1:
            return True
    if x[t] != 1:
        return True
    return False

def generate_big_prime():
    low_bound = pow(2, 1023)
    high_bound = pow(2, 1024) - 1
    p = random.randint(low_bound, high_bound)
    while not miller_rabin_test(p):
        p = random.randint(low_bound, high_bound)
    return p

def random_hash_function(m):
    p = generate_big_prime()
    a = random.randint(1, p)
    b = random.randint(0, p)
    def func(k):
        return ((a * k + b) % p) % m
    return func

class ChainHashTable(object):

    def __init__(self, m, data = []):
        self.m = m
        self._slots = []
        for i in range(m):
            self._slots.append([])
        self.hash_function = random_hash_function(m)
        for single_data in data:
            self.insert(single_data)

    def insert(self, x):
        print("insert key =: ", x.key)
        self._slots[self.h(x.key)].append(x)

    def search(self, k):
        print("search key =", k)
        for x in self._slots[self.h(k)]:
            if x.key == k:
                return x
        print("node with key =", k, "not found!")
        return None

    def delete(self, x):
        print("delete key =", x.key)
        self._slots[self.h(x.key)].remove(self.search(x.key))

    def h(self, k):
        return self.hash_function(k)

class Node():
    def __init__(self, key):
        self.key = key

if __name__ == "__main__":
    ht = ChainHashTable(10)
    nodes = []
    for i in range(300):
        node = Node(i)
        nodes.append(node)
        ht.insert(node)

    for k in range(10, 20):
        print(ht.search(k))

    x = ht.search(10)
    ht.delete(x)
    print(ht.search(10))











