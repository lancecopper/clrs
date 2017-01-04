import random
from insertion_sort import insertion_sort


def quicksort(a, p, q):
    if p < q:
        r = random_partition(a, p, q)
        quicksort(a, p, r)
        quicksort(a, r + 1, q)


def random_partition(a, p, q):
    #print("random_partition->p, q: ", p, q)
    if p < q:
        r = random.randint(p, q)
    else:
        r = p
    #print("random_partition->r: ", r)
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









