import random
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

    print("genereting random number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')

    insertion_sort(nums)
    print("the sorted number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')


