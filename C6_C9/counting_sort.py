import random
from insertion_sort import insertion_sort

def counting_sort(a, b, k):
    c = []
    for i in range(0, k + 1):
        c.append(0)
    a_length = len(a)
    for j in range(0, a_length):
        c[a[j]] += 1
        b.append(float("inf"))
        #print("c1: ", c)
    for i in range(1, k + 1):
        c[i] += c[i - 1]
        #print("c2: ", c)
    for j in range (a_length - 1, -1, -1):
        print(j, a[j], c[a[j]])
        b[c[a[j]] - 1] = a[j]
        print("b: ", b)
        c[a[j]] -= 1

if __name__ == "__main__":
    nums = []
    nums2 = []
    for i in range(0, 10):
        temp = random.randint(0, 100)
        nums.append(temp)

    nums1 = list(nums)

    print("genereting random number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')

    counting_sort(nums, nums2, 100)
    insertion_sort(nums1)


    if (nums1 != nums2):
        print("false!")
    else:
        print("right...")
        
    for i in range(0, 10):
        print(nums[i], end=' ')

    print('')












