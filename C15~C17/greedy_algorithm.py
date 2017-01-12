def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []

def greedy_activity_selector(s, f):
    k = 1
    n = len(s) - 1
    a = [1]
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            a.append(m)
            k = m
    return a

if __name__ == "__main__":
    s = [0] + [1,3,0,5,3,5,6,8,8,2,12]
    f = [0] + [4,5,6,7,9,9,10,11,12,14,16]
    n = len(s) - 1
    a = recursive_activity_selector(s, f, 0, n)
    print(a)
    a = greedy_activity_selector(s, f)
    print(a)







