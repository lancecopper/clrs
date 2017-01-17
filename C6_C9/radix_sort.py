import random
from insertion_sort import insertion_sort

def digit(n, d):
    return n // pow(10, d) % 10


def counting_sort(a, b, k, d):
    c = []
    for i in range(0, k + 1):
        c.append(0)
    a_length = len(a)
    for j in range(0, a_length):
        c[digit(a[j], d)] += 1
        b.append(float("inf"))
        #print("c1: ", c)
    for i in range(1, k + 1):
        c[i] += c[i - 1]
        #print("c2: ", c)
    for j in range (a_length - 1, -1, -1):
        b[c[digit(a[j], d)] - 1] = a[j]
        c[digit(a[j], d)] -= 1

def radix_sort(a, d):
    length = len(a)
    a_digits = []
    c = list(a)

    for k in range(0, d):
        b = []
        counting_sort(c, b, 9, k)
        c = b
    for i in range(0, length):
        a[i] = c[i]


if __name__ == "__main__":
    nums = []
    for i in range(0, 10):
        temp = random.randint(0, 99)
        nums.append(temp)

    nums1 = list(nums)

    print("genereting random number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')


    insertion_sort(nums1)
    radix_sort(nums, 2)


    if (nums1 != nums):
        print("false!")
    else:
        print("right...")
        
    for i in range(0, 10):
        print(nums[i], end=' ')

    print('')




