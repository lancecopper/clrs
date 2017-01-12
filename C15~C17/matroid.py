class Matroid():
    def __init__(self, s, belong_to_i):
        self.s = s
        self.belong_to_i = belong_to_i

'''
def insertion_sort(l, wfunc):
    length = len(l)
    wl = []
    for i in range(length):
        wl.append(wfunc(l[i]))
    for i in range(1, length):
        node = l[i]
        key = wl[i]
        j = i - 1
        while j >= 0 and wl[j] < key:
            wl[j + 1] = wl[j]
            l[ j + 1] = l[j]
            j -= 1
        w[j + 1] = key
        l[j + 1] = node
'''

def greedy(m, wfunc):
    a = []
    #insertion_sort(m.s, wfunc)
    for x in m.s:
        temp = a + [x]
        if m.belong_to_i(temp):
            a.append(x)
    return a



def final_disp(adv_tasks):
    length = len(adv_tasks)
    for i in range(1, length):
        key_value = d[adv_tasks[i] - 1]
        key = adv_tasks[i]
        j =  i - 1
        while j >= 0 and d[adv_tasks[j] - 1] > key_value:
            adv_tasks[j + 1] = adv_tasks[j]
            j -= 1
        adv_tasks[j + 1] = key
    total_tasks = list(range(1, len(w)+1))
    def_tasks = list(total_tasks)
    for task in adv_tasks:
        def_tasks.remove(task)
    return adv_tasks + def_tasks


if __name__ == "__main__":
    w = [70, 60, 50, 40, 30, 20, 10]
    d = [4, 2, 4, 3, 1, 4, 6]
    def wfunc(i):
        return w[i - 1]
    def belong_to_i(a):
        n = [0] * (len(w)+1)
        for i in a:
            n[d[i - 1]] += 1
        for i in range(2, len(n)):
            n[i] += n[i - 1]
        for i in range(2, len(n)):
            if n[i] > i:
                return False
        return True
    s = list(range(1, 8))
    m = Matroid(s, belong_to_i)
    result1 = greedy(m, wfunc)
    result2 = final_disp(result1)
    print(result1)
    print(result2)




