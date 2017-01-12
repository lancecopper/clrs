import random
from insertion_sort import insertion_sort


def quicksort(a, p, q):
    if p < q:
        r = random_partition(a, p, q)
        quicksort(a, p, r)
        quicksort(a, r + 1, q)


def random_partition(a, p, q):
    r = random.randint(p, q)
    a[r], a[q] = a[q], a[r]
    x = a[q]
    j = p - 1
    for i in range(p, q):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[j + 1], a[q] = a[q], a[j + 1]
    return j + 1


if __name__ == "__main__":
    def dfs(g):  
    for u in g.get_v():
        u.color = "white"
        u.parent = None
    for u in g.get_v():
        if u.color == "white":
          dfs_visit(g, u)

    def generat_dfs_visit():
        time = 0
        def dfs_visit(g, u):
            time += 1
            u.d = time
            u.color = "gray"
            for v in g.adj(u):
                if v.color == "white":
                    v.parent = u
                    dfs_visit(g, v)
            u.color = "black"
            time += 1
            u.f = time
        return dfs_visit

    def dfs_visit(g, u):
        func = generat_dfs_visit()
        func(g, u)
        nums = []
        for i in range(0, 10):
            temp = random.randint(0, 100)
            nums.append(temp)

    nums1 = list(nums)

    print("genereting random number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')

    quicksort(nums, 0, len(nums) - 1)
    insertion_sort(nums1)

    if (nums != nums1):
        print("false!")
    else:
        print("right...")
        
    for i in range(0, 10):
        print(nums[i], end=' ')

    print('')









