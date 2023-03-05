# python3

import sys
import threading

def compute_height(n, parents):
    max_height = 0
    return max_height

def main():
  
    n = int(input("Enter the number of nodes: "))
    parents = list(map(int, input("Enter the parent of each node separated by space: ").split()))

    print("Maximum height of the tree:", compute_height(n, parents))
    
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
