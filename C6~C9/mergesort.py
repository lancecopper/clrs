import random
from insertion_sort import insertion_sort



def mergesort(a, p, q):
    if p < q:
        r = (p + q) // 2
        mergesort(a, p, r)
        mergesort(a, r + 1, q)
        merge(a, p, q, r)


def merge(a, p, q, r):
    al = []
    ar = []
    for i in range(p, r + 1):
        al.append(a[i])
    for i in range(r + 1, q + 1):
        ar.append(a[i])
    al.append(float("inf"))
    ar.append(float("inf"))
    i = 0
    j = 0
    for k in range(p, q + 1):
        if al[i] <= ar[j]:
            a[k] = al[i]
            i += 1
        else:
            a[k] = ar[j]
            j += 1


if __name__ == "__main__":
    nums = []
    for i in range(0, 10):
        temp = random.randint(0, 100)
        nums.append(temp)

    nums1 = list(nums)

    print("genereting random number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')

    mergesort(nums, 0, len(nums) - 1)
    insertion_sort(nums1)

    if (nums != nums1):
        print("false!")
    else:
        print("right...")
        
    for i in range(0, 10):
        print(nums[i], end=' ')

    print('')




