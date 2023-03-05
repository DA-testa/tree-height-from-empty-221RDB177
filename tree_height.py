# python3

import sys
import threading


def compute_height(n, parents):
    max_height = 0
    return max_height


def main():
    input_format = input().strip()
    
    
    if input_format == "I":
        
        n = int(input().strip())
        parents = list(map(int, input().strip().split()))
    else:
        
        file_name = input().strip()
        while "a" in file_name:
            file_name = input().strip()
        with open(f"./data/{file_name}", "r") as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
 
    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
