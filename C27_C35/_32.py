def naive_string_matcher(t, p):
    n = len(t)
    m = len(p)
    result = []
    for s in range(n - m + 1):
        if p[0:m] == t[s:s + m]:
            print("Pattern occurs with shift", s)
            result.append(s)
    return result

def rabin_kapp_matcher(arg_t, arg_p, d, q):
    '''
    # args: the text T, the patter P,
    # the radix d(which is typically taken to be |sigma|)
    # the prime q(a prime, which make dq smaller than a word size)
    # t[s + 1] = (d(t[s] - T[s + 1]h) + T[s + m + 1]) mod q
    '''
    n = len(arg_t)
    m = len(arg_p)
    h = pow(d, m - 1) % q
    p = 0
    t = [None] * (n - m + 1)
    t[0] = 0
    result = []
    for i in range(m):  #preprocessing
        p = (d * p + arg_p[i]) % q
        t[0] = (d * t[0] + arg_t[i]) % q
    for s in range(n - m + 1):
        if p == t[s]:
            if arg_p[0:m] == arg_t[s:s + m]:
                print("Pattern occurs with shift", s)
                result.append(s)
        if s < n - m:
            t[s + 1] = (d * (t[s] - arg_t[s] * h) + arg_t[s + m]) % q
    return result

def finite_automaton_matcher(t, delta, m):
    n = len(t)
    q = 0
    result = []
    for i in range(n):
        q = delta(q, t[i])
        if q == m:
            result.append(i - m + 1)
            print("pattern occurs with shift", i - m + 1)
    return result

def compute_transition_function(p, sigma):
    m = len(p)
    delta = dict()
    for q in range(m + 1):
        delta[q] = dict()
        for a in sigma:
            k = min(m, q + 1)
            while not p[0:k] == (p[0:q] + [a])[q + 1 - k:q + 1]:
                k -= 1
            delta[q][a] = k
    return delta

def kmp_matcher(t, p):
    n = len(t)
    m = len(p)
    pi = compute_prefix_function(p)
    q = 0
    result = []
    for i in range(n):
        while q >= 0 and p[q + 1] != t[i]:
            q = pi[q]
        if p[q + 1] == t[i]:
            q += 1
        if q == m - 1:
            result.append(i - m + 1)
            print("Pattern occurs with shift", i - m + 1)
            q = pi[q]
    return result

def compute_prefix_function(p):
    m = len(p)
    pi = [None] * m
    pi[0] = -1
    k = -1
    for q in range(1, m):
        while k >= 0 and p[k + 1] != p[q]:
            k = pi[k]
        if p[k + 1] == p[q]:
            k += 1
        pi[q] = k
    return pi


if __name__ == "__main__":
    '''
    print("test for naive_string_matcher and rabin_kapp_matcher")
    print("test for rabin_kapp_matcher")
    text = [2,3,4,5,0,2,3,1,4,1,5,2,6,7,3,9,9,2,1]
    pattern = [3,1,4,1,5,2]
    print(naive_string_matcher(text, pattern))
    print(rabin_kapp_matcher(text, pattern, 10, 13))
    '''
    pattern = list('ababaca')
    sigma = ['a', 'b', 'c']
    delta = compute_transition_function(pattern, sigma)
    
    '''
    print("test for compute_transition_function")
    for q in range(len(pattern) + 1):
        print("condition{} :".format(q))
        for a in sigma:
            print(a, delta[q][a], end = ',  ')
        print()
    '''
    #'''
    print("test for finite_automaton_matcher...")
    text = list("abababacaba")
    def generate_delta_func(delta):
        def func(q, a):
            return delta[q][a]
        return func
    delta_func = generate_delta_func(delta)
    print(finite_automaton_matcher(text, delta_func, len(pattern)))
    #'''
    print("test for compute_prefix_function...")
    pattern = list('ababaca')
    text = list("abababacaba")
    pi = compute_prefix_function(pattern)
    print(kmp_matcher(text, pattern))







