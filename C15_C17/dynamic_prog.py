def cut_rod(p, n):
    if n == 0:
        return 0
    q = - float("inf")
    for i in range(1, n+1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))
    return q

def memorized_cut_rod(p, n):
    r = []
    for i in range(0, n + 1):
        r.append(-float("inf"))
    return memorized_cut_rod_aux(p, n, r)

def memorized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + memorized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q

def bottom_up_cut_rod(p, n):
    r = []
    for i in range(0, n + 1):
        r.append(-float("inf"))
    r[0] = 0
    for i in range(1, n + 1):
        q = -float("inf")
        for j in range(1, i + 1):
            q = max(q, p[j - 1] + r[i - j])
        r[i]=q
    return r[n]


def extended_bottom_up_cup_rod(p, n):
    r = []
    s = []
    for i in range(0, n + 1):
        r.append(-float("inf"))
        s.append(None)
    r[0] = 0
    for i in range(1, n + 1):
        q = -float("inf")
        for j in range(1, i + 1):
            if q < p[j - 1] + r [i - j]:
                q = p[j -1] + r[i - j]
                s[i] = j
        r[i]=q
    return r, s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cup_rod(p, n)
    print("the price will be :", r[n])
    while n > 0:
        print(s[n])
        n -= s[n]

if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    for i in range(11):
        print("####length: ", i)
        print(cut_rod(p,i))
        print(memorized_cut_rod(p, i))
        print(bottom_up_cut_rod(p, i))

    for i in range(11):
        print_cut_rod_solution(p, i)



