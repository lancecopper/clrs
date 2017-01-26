import random
from threading import Thread
def p_merge_sort(a, p, r, b, s):
    n = r - p + 1
    print("p_merge_sort", p, r, n)
    if n == 1:
        print("b[{}] = a[{}]".format(s, p))
        b[s] = a[p]
        print(a, b)
    else:
        t = [None] * n
        q = (p + r) // 2
        q1 = q - p + 1
        t1 = Thread(target = p_merge_sort, args = (a, p, q, t, 0))
        t2 = Thread(target = p_merge_sort, args = (a, q + 1, r, t, q1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("###ready to merge:... p_merge_sort, p={},r={},q={},q1={}".format(p, r, q, q1))
        print(t)
        p_merge(t, 0, q1 - 1, q1, n - 1, b, s)
        print(b)
def binary_search(x, t, p, r):
    low = p
    high = max(p, r + 1)
    while low < high:
        mid = (low + high) // 2
        if x <= t[mid]:
            high = mid
        else:
            low = mid + 1
    return high
def p_merge(t, p1, r1, p2, r2, a, p3):
    n1 = r1 - p1 + 1 
    n2 = r2 - p2 + 1
    if n1 < n2:
        p1, p2 = p2, p1
        r1, r2 = r2, r1
        n1, n2 = n2, n1
    if n1 == 0:
        return
    else:
        q1 = (p1 + r1) // 2
        q2 = binary_search(t[q1], t, p2, r2)
        q3 = p3 + (q1 - p1) + (q2 - p2)
        print("a[{}] = t[{}]".format(q3, q1))
        a[q3] = t[q1]
        t1 = Thread(target = p_merge, args = (t, p1, q1 - 1, p2, q2 - 1, a, p3))
        t2 = Thread(target = p_merge, args = (t, q1 + 1, r1, q2, r2, a, q3 + 1))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        p_merge(t, p1, q1 - 1, p2, q2 - 1, a, p3)
        p_merge(t, q1 + 1, r1, q2, r2, a, q3 + 1)
def insertion_sort(l):
    length = len(l)
    for i in range(1, length):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
if __name__ == "__main__":
    nums = []
    for i in range(0, 10):
        temp = random.randint(0, 100)
        nums.append(temp)
    nums1 = nums.copy()
    print("genereting random number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')
    result_num = [None] * len(nums)
    p_merge_sort(nums, 0, len(nums) - 1, result_num, 0)
    insertion_sort(nums1)
    if (result_num != nums1):
        print("false!")
    else:
        print("right...")   
    for i in range(0, 10):
        print(result_num[i], end=' ')
    print('')





