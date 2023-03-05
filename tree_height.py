# python3

import sys
import threading

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        

def compute_tree_height(node):
    if not node.children:
        return 1
    child_heights = [compute_tree_height(child) for child in node.children]
    return max(child_heights) + 1


def main():
  
    n = int(input())
    parents = list(map(int, input().split()))

   
    nodes = [TreeNode(i) for i in range(n)]
    root = None

   
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
            
            tree_height = compute_tree_height(root)

   
    print(tree_height)
    
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
