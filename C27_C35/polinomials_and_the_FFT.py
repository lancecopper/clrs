import math
from functools import partial
from threading import Thread

class UnityComplexRoot:
    def __init__(self, n, k):
        pass

def get_w(n):
    for k in range(n):
        w[k] = pow(math.e, 2 * math.pi * (0 + 1j) * k / n)

#w = get_w(n)
'''
def lagrange_formula():
    #点阵-->系数, 拉格朗日公式, O(n ^ 2)

* 系数-->点阵， O(n * lgn)
'''
def get_w(n, k):
    k = k % n
    return pow(math.e, 2 * math.pi * k * (0 + 1j) / n)
def get_w_sc(n, k):
    u = 2 * math.pi * k / n
    return math.cos(u) + math.sin(u) * (0 + 1j)

get_w8 = partial(get_w, 8)
get_w8_sc = partial(get_w_sc, 8)

def recursive_fft(a):
    '''
    # A(x) = sigma{j = 0 ~ n - 1}(a[j] * x ^ j )
    # x belongs to {omiga_n ^ 0, omiga_n ^ 1, ... , omiga_n ^ n - 1}
    # this function calulate y = A(x),
    # as a vector y = (y[0], y[1], ... , y[n - 1])
    '''
    n = len(a)    # n is a power of 2
    if n == 1:
        return a
    wn = pow(math.e, 2 * math.pi * (0 + 1j) / n)
    var_w = 1
    a0 = a[::2]
    a1 = a[1::2]
    y0 = recursive_fft(a0)
    y1 = recursive_fft(a1)
    y = [None] * n
    for k in range(n // 2):
        #y[k] = round(y0[k] + var_w * y1[k], 4)
        #y[k + n // 2] = round(y0[k] - var_w * y1[k], 4)
        y[k] = y0[k] + var_w * y1[k]
        y[k + n // 2] = y0[k] - var_w * y1[k]
        var_w = var_w * wn
    return y

def inverse_recursive_fft(a):
    n = len(a)    # n is a power of 2
    if n == 1:
        return a
    wn = 1 / pow(math.e, 2 * math.pi * (0 + 1j) / n)
    var_w = 1
    a0 = a[::2]
    a1 = a[1::2]
    y0 = inverse_recursive_fft(a0)
    y1 = inverse_recursive_fft(a1)
    y = [None] * n
    for k in range(n // 2):
        #y[k] = round(y0[k] + var_w * y1[k], 4)
        #y[k + n // 2] = round(y0[k] - var_w * y1[k], 4)
        y[k] = y0[k] + var_w * y1[k]
        y[k + n // 2] = y0[k] - var_w * y1[k]
        var_w = var_w * wn
    return y

def inverse_fft(y):
    n = len(y)
    result = inverse_recursive_fft(y)
    for i in range(n):
        result[i] /= n
    return result

def polynomials_mult(a, b):
    n1 = len(a)
    n2 = len(b)
    n = max(n1, n2)
    a.extend([0] * (2 * n - n1))
    b.extend([0] * (2 * n - n2))
    ya = recursive_fft(a)
    yb = recursive_fft(b)
    print(ya, yb)
    y = [None] * 2 * n
    for i in range(2 * n):
        y[i] = ya[i] * yb[i]
    print(y)
    result = inverse_fft(y)
    for i in range(2 * n):
        num = result[i]
        imag = round(num.imag, 4)
        result[i] = num.real + (0 + i) * imag
    return result

def bit_reverse_copy(a):
    n = len(a)
    lgn = int(math.log(n, 2))
    result = [None] * n
    for k in range(n):
        digits = bin(k)[2:]
        digits = '0' * (lgn - len(digits)) + digits
        result[int(digits[::-1], 2)] = a[k]
    return result

def iterative_fft(a):
    a = bit_reverse_copy(a)
    n = len(a)
    for s in range(1, int(math.log(n, 2)) + 1):
        m = pow(2, s)
        wm = pow(math.e, 2 * math.pi * (0 + 1j) / m)
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * a[k + j + m // 2]
                u = a[k + j]
                a[k + j] = u + t
                a[k + j + m // 2] = u - t
                w *= wm
    return a

def inverse_iterative_fft(a):
    a = bit_reverse_copy(a)
    n = len(a)
    for s in range(1, int(math.log(n, 2)) + 1):
        m = pow(2, s)
        wm = 1 / pow(math.e, 2 * math.pi * (0 + 1j) / m)
        for k in range(0, n, m):
            w = 1
            for j in range(m // 2):
                t = w * a[k + j + m // 2]
                u = a[k + j]
                a[k + j] = u + t
                a[k + j + m // 2] = u - t
                w *= wm
    return a

def inverse_fft1(y):
    n = len(y)
    result = inverse_iterative_fft(y)
    for i in range(n):
        result[i] /= n
    return result

def polynomials_mult1(a, b):
    n1 = len(a)
    n2 = len(b)
    n = max(n1, n2)
    a.extend([0] * (2 * n - n1))
    b.extend([0] * (2 * n - n2))
    ya = iterative_fft(a)
    yb = iterative_fft(b)
    y = [None] * 2 * n
    for i in range(2 * n):
        y[i] = ya[i] * yb[i]
    result = inverse_fft1(y)
    for i in range(2 * n):
        num = result[i]
        imag = round(num.imag, 4)
        result[i] = num.real + (0 + i) * imag
    return result


def adjuvant_p_fft(a, p, q):
    '''
    #p_fft(bit_reverse_copy(a), 0, len(a) - 1)
    '''
    n = q - p + 1    # n is a power of 2
    if n == 1:
        return
    r = (p + q) // 2
    t1 = Thread(target = adjuvant_p_fft, args = (a, p, r))
    t2 = Thread(target = adjuvant_p_fft, args = (a, r + 1, q))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    wm = pow(math.e, 2 * math.pi * (0 + 1j) / n)
    p_adju_calc_fft(a, p, n, 0, n // 2 - 1, wm)

def p_adju_calc_fft(a, p, n, p1, q1, wm):
    if p1 == q1:
        w = pow(wm, q1)
        t = w * a[p + p1 + n // 2]
        u = a[p + p1]
        a[p + p1] = u + t
        a[p + p1 + n // 2] = u - t
        return
    r1 = (p1 + q1) // 2
    t1 = Thread(target = p_adju_calc_fft, args = (a, p, n, p1, r1, wm))
    t2 = Thread(target = p_adju_calc_fft, args = (a, p, n, r1 + 1, q1, wm))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def p_fft(a):
    a = bit_reverse_copy(a)
    adjuvant_p_fft(a, 0, len(a) - 1)
    return a

if __name__ == "__main__":
    '''
    print("test for fft...")
    a = [1]
    r = recursive_fft(a)
    print(r)
    a = [1, 1]
    r= recursive_fft(a)
    print(r)
    '''

    '''
    print("test for dft...")
    a = [1,2,3,4]
    r = inverse_fft(recursive_fft(a))
    print(r)
    '''

    '''
    print("test for bit_reverse_copy...")
    a = list(range(0,8))
    a = bit_reverse_copy(a)
    print(a)
    '''
    '''
    print("test for dft...iterative")
    a = [1,2,3,4,5,6,7,8]
    print(iterative_fft(a) == recursive_fft(a))
    print(inverse_iterative_fft(a) == inverse_recursive_fft(a))
    r = inverse_fft1(iterative_fft(a))
    r1 = inverse_fft(iterative_fft(a))
    print(r1)
    '''

    '''
    print("test for poly_mult...")
    a = [1, 1, 2, 3]
    b = [1, 1, 2, 3]
    print(polynomials_mult1(a, b))
    '''
    print("test for parallel:")
    a = [1,2,3,4,5,6,7,8]
    print(iterative_fft(a) == p_fft(a))
    '''
    print(inverse_iterative_fft(a) == inverse_recursive_fft(a))
    r = inverse_fft1(iterative_fft(a))
    r1 = inverse_fft(iterative_fft(a))
    print(r1)
    '''
