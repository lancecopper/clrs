import math
def bit_reverse_copy(a):
    n = len(a)
    lgn = int(math.log(n, 2))
    result = [None] * n
    for k in range(n):
        digits = bin(k)[2:]
        digits = '0' * (lgn - len(digits)) + digits
        result[int(digits[::-1], 2)] = a[k]
    return result

def rev(k, a):
    a = bin(a)[2:]
    a = "0" * (k - len(a)) + a
    a = a[::-1]
    return int(a, 2)

def bit_reverse_copy1(a):
    length = len(a)
    temp = a[length - 1]
    k = len(bin(temp)) - 2
    result = [None] * length
    for i in range(length):
        result[rev(k, i)] = a[i]
    return result

def bit_reverse_copy2(a):
    """
    #use amotized analysis to get a tight boundary
    """
    length = len(a)
    temp = a[length - 1]
    k = len(bin(temp)) - 2
    result = [None] * length
    result[0] = 0
    for i in range(1, length):
        result[i] = bit_reversed_increment(k, result[i - 1])
    return result

def bit_reversed_increment(k, a):
    a = bin(a)[2:]
    a = "0" * (k - len(a)) + a
    a = list(a)
    i = 0
    while i <= k - 1 and a[i] == '1':
        a[i] = '0'
        i += 1
    if i <= k - 1:
        a[i] = '1'
    a = ''.join(a)
    return int(a, 2)

def bit_reverse_copy3(a):
    """
    #use amotized analysis to get a tight boundary
    """
    length = len(a)
    temp = a[length - 1]
    k = len(bin(temp)) - 2
    result = [None] * length
    result[0] = 0
    for i in range(1, length):
        result[i] = bit_reversed_increment1(k, result[i - 1])
    return result

def bit_reversed_increment1(k, a):
    a = bin(a)[2:]
    a = "0" * (k - len(a)) + a
    a = list(a)
    i = 0
    while i <= k - 1 and a[i] == '1':
        a[i] = '0'
        i += 1
    if i <= k - 1:
        a[i] = '1'
    a = ''.join(a)
    return int(a, 2)



if __name__ == "__main__":
    a = list(range(16))
    print(bit_reverse_copy1(a))
    print(bit_reverse_copy2(a))


