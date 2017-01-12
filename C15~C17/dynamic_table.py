# this module haven't pass a test

def table_insert(t, x):
    if t.size == 0:
        t.table.append(None)
        t.size = 1
    if t.num == t.size:
        for i in range(t.size):
            t.table.append(None)
        t.size *= 2
    for i in range(t.size):
        if t.table[i] is None:
            t.table[i] = x
            break
    t.num += 1

def table_delete(t, x):
    t.table.remove(x)
    t.table.append(None)
    t.num -= 1
    if t.num == t.size/4:
        t.table = t.table[0: int((len(t.table)+1)/2)]
        t.size /= 2

class DynamicTable():
    def __init__(self):
        self.table = []
        self.size = 0
        self.num = 0

    def insert(self, x):
        table_insert(self, x)

    def delete(self, x):
        table_delete(self, x)


if __name__ == "__main__":
    dt = DynamicTable()
    print("size, num, table")
    for i in range(20):
        dt.insert(i)
        print("insert", i)
        print(dt.size, dt.num, dt.table)

    for i in range(20):
        dt.delete(i)
        print("delete", i)
        print(dt.size, dt.num, dt.table)










