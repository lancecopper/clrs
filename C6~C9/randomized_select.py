import random
from quicksort import random_partition as randomized_partition
from quicksort import quicksort

def randomized_select(a, p, q, i):
    print("randomized_select-> p, q, i:", p, q, i)
    if p == q:
        return a[p]
    r = randomized_partition(a, p, q)
    #print(a)
    #print("randomized_select->r:", r)
    
    
    k = r - p + 1

    #print("randomized_select->i,k:", i, k)
    if i == k:
        return a[r]
    elif i < k:
        return randomized_select(a, p, r , i)
    else:
        return randomized_select(a, r + 1, q, i - k)

if __name__ == "__main__":
    nums = []
    for i in range(0, 10):
        temp = random.randint(0, 100)
        nums.append(temp)
    nums1 = list(nums)

    print("genereting random number sequence: \n", nums)
    i = random.randint(1, 10)
    result = randomized_select(nums, 0, 9, i)
    print("i= ", i)
    print(result)
    quicksort(nums1, 0, 9)

    quicksort(nums, 0, 9)
    if nums[i - 1] == result:
        print("right...")
    else:
        print("wrong")

