class Node():
    __slots__ = ['freq', 'key', 'left', 'right']
    def __init__(self, frequency, key = None, left = None, right = None):
        self.freq = frequency
        self.key = key
        self.left = left
        self.right = right

class CharacterQueue():
    def __init__(self, queue = []):
        if not isinstance(queue, list):
            raise TypeError("class <CharacterQueue> expected <list> arg")
        self.queue = queue

    def insert(self, x):
        self.queue.append(x)

    def extract_min(self):
        min_freq = float("inf")
        for __char in self.queue:
            if __char.freq < min_freq:
                min_freq = __char.freq
                min_char = __char
        self.queue.remove(min_char)
        return min_char

def huffman(c):
    n = len(c)
    q = CharacterQueue(c)
    for i in range(n - 1):
        z = Node(0)
        x = z.left = q.extract_min()
        y = z.right = q.extract_min()
        z.freq = x.freq + y.freq
        q.insert(z)
    return q.extract_min()

def print_huffman_tree(node, code):
    if node:
        if node.key:
            print(''.join(code), ' : ', node.key)
        print_huffman_tree(node.left, code+['0'])
        print_huffman_tree(node.right, code+['1'])
    else:
        return

if __name__ == "__main__":
    frequencies = [45, 13, 12, 16, 9, 5]
    keys = ['a', 'b', 'c', 'd', 'e', 'f']
    characters = []

    for i in range(len(keys)):
        node = Node(frequencies[i], keys[i])
        print(node.key, node.freq)
        characters.append(node)

    root = huffman(characters)
    print_huffman_tree(root, [])












