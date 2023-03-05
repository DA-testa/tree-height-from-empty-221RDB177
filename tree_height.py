# python3

import sys
import threading

def compute_height(n, parents):
    # Create a dictionary to store the children of each node
    children = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            if parent in children:
                children[parent].append(node)
            else:
                children[parent] = [node]

    # Use a stack to traverse the tree and compute its height
    stack = [(root, 0)]
    max_height = 0
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        if node in children:
            for child in children[node]:
                stack.append((child, height + 1))

    return max_height

if __name__ == '__main__':
    # Read input from standard input
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute the height of the tree and print the result
    print(compute_height(n, parents))
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
