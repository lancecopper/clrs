import random 

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i +2


def max_heapify(a, i):
    l = left(i)
    r = right(i)
    if l <= len(a) - 1 and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= len(a) - 1 and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    i = len(a)//2 - 1
    while i >= 0:
        max_heapify(a, i)
        i -= 1

def heapsort(a):
    build_max_heap(a)
    i = len(a) - 1
    result = []
    while i >= 1:
        a[0], a[i] = a[i], a[0]
        result.append(a[i])
        del(a[i])
        i -= 1
        max_heapify(a, 0)
    result.append(a[i])
    return result



def heap_maximum(a):
    return a[0]

def heap_extraxt_max(a):
    length = len(a)
    if length < 1:
        raise ValueError("heap underflow")
    max = a[0]
    a[0] = a[length - 1]
    del(a[length - 1])
    max_heapify(a, 0)
    return max

def heap_increase_key(a, i, key):
    if key < a[i]:
        raise ValueError("new key is smaller than current key")
    a[i] = key
    while i > 0 and a[parent(i)] < a[i]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)

def max_heap_insert(a, key):
    a.append(-float("inf"))
    heap_increase_key(a, len(a) - 1, key)



if __name__ == "__main__":
    nums = []
    for i in range(0, 10):
        temp = random.randint(0, 100)
        nums.append(temp)

    print("genereting random number sequence: ")
    for i in range(0, 10):
        print(nums[i], end=' ')
    print('')

    result = heapsort(nums)
    print("the sorted number sequence: ")
    for i in range(0, 10):
        print(result[i], end=' ')
    print('')

    print(heap_maximum(result))
    print(result)
    print(heap_extraxt_max(result))
    print(result)

    heap_increase_key(result, 3, 200)
    print(result)

    max_heap_insert(result, 1000)
    print(result)




