import random
from insertion_sort import insertion_sort
from quicksort import quicksort

def median(a):
    length = len(a)
    #print("median->length: ", length)
    return a[(length - 1) // 2]

def partition(a, p, q, x):
    #print("partition-> p, q, x:", p, q, x)
    j = p - 1
    #print("partition-> a:", a)
    for i in range(p, q + 1):
        #print("a[i], x: ", a[i], x)
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    #print("partition-> p, q, j:", p, q, j)
    return j



def select(a, p, q, j):
    #print("select->p, q, j: ", p, q, j)
    #print("select->a: ", a)
    if q - p + 1 < j:
        raise ValueError("select out of range!")
    if p == q and j == 1:
        return a[p]

    b = []
    medians = []
    b_length = (q - p + 1) // 5
    
    if (q - p + 1) % 5:
        b_length += 1
    if b_length > 1:
        for i in range(0, b_length - 1):
            b.append(a[p + 5 * i : p + 5 * i + 5])
        i += 1
        b.append(a[p + 5 * i : q + 1])
    else:   
        b.append(a[p : q + 1])
    #print("b: ", b)
    for i in range(0, b_length):
        insertion_sort(b[i])
        medians.append(median(b[i]))
    #print("medians: ", medians)
    x = select(medians, 0, len(medians) - 1, (len(medians) + 1) // 2)
    r = partition(a, p, q, x)
    k = r - p + 1
    #print("j,k: ", j, k)
    if j == k:
        return a[r]
    elif j < k:
        return select(a, p, r - 1, j)
    else:
        return select(a, p + k , q, j - k)


if __name__ == "__main__":
    nums = []
    for i in range(0, 10):
        temp = random.randint(0, 100)
        nums.append(temp)
    nums1 = list(nums)

    print("genereting random number sequence: \n", nums)
    i = random.randint(1, 10)
    result = select(nums, 0, 9, i)
    print("i =", i)
    print("result: ", result)
    quicksort(nums1, 0, 9)
    print(nums1)
    print(nums)
    if nums[i - 1] == result:
        print("right...")
    else:
        print("wrong")













