def test_data(rows, columns, data):
    if len(data) == rows:
        for l in data:
            if len(l) != columns:
                return False
        return True
    else:
        return False

class Matrix():
    def __init__(self, rows, columns, data = None):
        if data and test_data(rows, columns, data):
            self._data = list(data)
        elif data:
            raise ValueError("data contradict \
                             rows and columns")
        else:
            self._data = []
            for i in range(rows):
                temp = []
                for j in range(columns):
                    temp.append(None)
                self._data.append(temp)
        self.rows = rows
        self.columns = columns
    def __getitem__(self, i):
        return self._data[i]

    def __setitem__(self, k, v):
        self._data[k] = v


def matrix_multiply(a, b):
    if a.columns != b.rows:
        raise ValueError('incompatible dimensions')
    else:
        c = Matrix(a.rows, b.columns)
        for i in range(0, a.rows):
            for j in range(0, b.columns):
                c[i][j] = 0
                for k in range(0, a.columns):
                    c[i][j] = c[i][j] + a[i][k] * b[k][j]
    return c



def matrix_chain_order(p):
    n = len(p) - 1
    m = []
    s = []
    for i in range(n):
        temp1 = []
        temp2 = []
        for i in range(n):
            temp1.append(None)
            temp2.append(None)
        m.append(temp1)
        s.append(temp2)
    for i in range(n):
        m[i][i] = 0
    for l in range(2, n + 1):       #l is the chain length
        for i in range(n - l + 1 ):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                print(m[i][k], m[k+1][j])
                print(q)
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_solution(s, i, j):
    if i == j:
        print("A{{{}}}".format(i), end = "")
    else:
        print('(', end = '')
        print_optimal_solution(s, i, s[i][j])
        print(' * ', end = '')
        print_optimal_solution(s, s[i][j] + 1, j)
        print(')', end = '')
    




if __name__ == "__main__":

    '''
    a = Matrix(2, 3, [[1,1,1,], [1,1,1]])
    b = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
    c = matrix_multiply(a, b)
    d = matrix_multiply(b, a)
    c1 = []
    d1 = []
    for i in range(0, c.rows):
        c1.append(c[i])
    for i in range(0, d.rows):
        d1.append(d[i])
    print(c1)
    print(d1)
    '''
    p = [30,35,15,5,10,20,25]
    n = len(p) - 1
    m, s = matrix_chain_order(p)
    print("the least calc times is", m[0][n - 1])
    print_optimal_solution(s, 0, n - 1)
    print()








