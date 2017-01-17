import random
from insertion_sort import insertion_sort


def bucket_sort(a, scope):
    n = len(a)
    b = []
    for i in range(0, n):
        b.append([])
    for i in range(0, n):
        b[n * int(a[i]) // scope].append(a[i])
    for i in range(0, n):
        b[i].sort()
    for i in range(1, n):
        b[0].extend(b[i])
    for i in range(0, n):
        a[i] = (b[0][i])


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

    insertion_sort(nums1)
    bucket_sort(nums, 101)


    #print(nums1)
    #print(nums)
    if (nums1 != nums):
        print("false!")
    else:
        print("right...")
        
    for i in range(0, 10):
        print(nums[i], end=' ')

    print('')






