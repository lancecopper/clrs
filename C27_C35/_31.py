import random
import math

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)
gcd = euclid
def extended_euclid(a, b):
    # d = gcd(a, b) = ax + by
    if b == 0:
        return a, 1, 0
    else:
        d1, x1, y1 = extended_euclid(b, a % b)
        d, x, y = d1, y1, x1 - a // b * y1
        return d, x, y
def modular_linear_equation_solver(a, b, n):
    d, x1, y1 = extended_euclid(a, n)
    #print(d, x1, y1)
    if b % d == 0:
        result = []
        x0 = (x1 * (b // d)) % n
        #print("x0", x0)
        for i in range(d):
            temp = (x0 + i * (n // d)) % n
            result.append(temp)
            #print(temp)
        return result
    else:
        print("no solutions")
mles = modular_linear_equation_solver
def modular_exponentiation(a, b, n):
    ''' 
    # raising to powers with repeated squaring 
    # and get modular_exponentiation
    # calc (a ^ b) mod n
    '''
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

def chinese_remainder(ak, nk):
    n = 1
    for i in nk:
        n *= i
    mk = []
    mk1 = []
    ck = []
    for i in range(len(nk)):
        temp_mk = 1
        for j in range(len(nk)):
            if i != j:
                temp_mk *= nk[j]
        mk.append(temp_mk)
    for i in range(len(mk)):
        temp_mk1 = modular_linear_equation_solver(mk[i], 1, nk[i])[0]
        mk1.append(temp_mk1)
        temp_ck = mk[i] * (temp_mk1 % nk[i])
        ck.append(temp_ck)
    sum_ac = 0
    for i in range(len(nk)):
        sum_ac += ak[i] * ck[i]
    print(mk,mk1,ck)
    return sum_ac % n

def pollard_rho(n):
    i = 1
    xi = random.randint(0, n - 1)
    y = xi
    k = 2
    while True:
        i += 1
        xi = (pow(xi, 2) - 1) % n
        d = gcd(y - xi, n)
        if d != 1 and d != n:
            print(d)
            return d
        if i == k:
            y = xi
            k *= 2

if __name__ == "__main__":
    #mles(13, 1, 5)
    print(chinese_remainder([2, 3], [5, 13]))










