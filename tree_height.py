# python3

import sys
import threading

def compute_height(n, parents):
   
    children = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            if parent in children:
                children[parent].append(node)
            else:
                children[parent] = [node]

    
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
  
    n = int(input())
    parents = list(map(int, input().split()))

   
    print(compute_height(n, parents))
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
