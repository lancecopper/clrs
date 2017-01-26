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
    for i in range(m):
        pi[i] += 1
    return pi

def compute_transition_function(p, sigma):
    pi = compute_prefix_function(p)
    m = len(p)
    delta = dict()
    delta[0] = dict()
    for a in sigma:
        if p[0] != a:
            delta[0][a] = 0
        else:
            delta[0][a] = 1
    for q in range(1, m + 1):
        delta[q] = dict()
        if q == m:
            for a in sigma:
                delta[q][a] = delta[pi[q - 1]][a]
        else:
            for a in sigma:
                if p[q] != a:
                    delta[q][a] = delta[pi[q - 1]][a]
                else:
                    delta[q][a] = q + 1
    return delta


if __name__ == "__main__":
    pattern = list('ababaca')
    sigma = ['a', 'b', 'c']
    delta = compute_transition_function(pattern, sigma)
    print("test for compute_transition_function")
    for q in range(len(pattern) + 1):
        print("condition{} :".format(q))
        for a in sigma:
            print(a, delta[q][a], end = ',  ')
        print()
