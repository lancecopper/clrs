def lcs_length(x, y):
    m = len(x)
    n = len(y) 
    b = []
    c = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(None)
        b.append(temp)
    for i in range(m + 1):
        temp = []
        for j in range(n + 1):
            temp.append(None)
        c.append(temp)

    for i in range(m + 1):
        c[i][0] = 0
    for j in range(n + 1):
        c[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i - 1][j - 1] = "left-up"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i - 1][j - 1] = "up"
            else:
                c[i][j] = c[i][j - 1]
                b[i - 1][j - 1] = "left"
    return c, b

def print_lcs(b, x, i, j):
    if i == 0 or j == 0:
        return 
    if b[i - 1][j - 1] == "left-up":
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1])
    elif b[i - 1][j - 1] == "up":
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)

if __name__ == "__main__":
    x = list("abcbdab")
    y = list("bdcaba")
    m = len(x)
    n = len(y) 
    c, b = lcs_length(x, y)
    '''
    for i in range(m+1):
        for j in range(n+1):
            print(c[i][j])
        print()
    for i in range(m):
        for j in range(n):
            print(b[i][j])
        print()
    '''
    
    print(c)
    print(b)
    print_lcs(b, x, len(x), len(y))
    
