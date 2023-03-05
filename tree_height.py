# python3

import sys
import threading

def compute_height(n, parents):
   
    tree = {}
    for i in range(n):
        tree[i] = []
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

   
    def height(node):
        if not tree[node]:
            return 1
        else:
            return max(height(child) for child in tree[node]) + 1

    return height(root)


n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))

    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
