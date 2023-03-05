# python3

import sys
import threading

def compute_height(n, parents):
   

 children = [[] for _ in range(n)] # initialize empty list for each node
    for i, parent in enumerate(parents):
        if parent == -1: # found root node
            root = i
        else:
            children[parent].append(i) # add i-th node as a child of parent node
    
    # compute height of the tree
    def compute_depth(node):
        if not children[node]: # leaf node
            return 1
        max_depth = 0
        for child in children[node]:
            depth = compute_depth(child)
            max_depth = max(max_depth, depth)
        return max_depth + 1

    return compute_depth(root)


def main():
    # read input from standard input or file
    input_type = input()

    if 'I' in input_type: # read from standard input
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height)
    elif 'F' in input_type: # read from file
        filename = input()
        with open(filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            height = compute_height(n, parents)
            print(height)
    else:
        print("Error: Invalid input type.")
        exit()
    
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
