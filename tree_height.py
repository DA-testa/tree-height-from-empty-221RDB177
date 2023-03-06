import sys
import threading
import numpy as np


def compute_tree_height(n: int, parents: List[int]) -> int:
    children = {i: [] for i in range(n)}
    root_nodes = []
    for i, parent in enumerate(parents):
        if parent == -1:
            root_nodes.append(i)
        else:
            children[parent].append(i)

    def get_depth(node: int, curr_depth: int) -> int:
        if not children[node]:
            return curr_depth
        else:
            max_depth = 0
            for child in children[node]:
                child_depth = get_depth(child, curr_depth + 1)
                max_depth = max(max_depth, child_depth)
            return max_depth

    max_height = 0
    for root in root_nodes:
        tree_height = get_depth(root, 0)
        max_height = max(max_height, tree_height)

    return max_height + 1


def main() -> None:
    input_mode = input("Enter F (for file) or I (for input): ")
    if "I" in input_mode:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in input_mode:
        filename = input("Enter file name: ")
        file_path = f"./test/{filename}"
        if "a" not in filename:
            try:
                with open(file_path) as test_file:
                    n = int(test_file.readline())
                    parents = list(map(int, test_file.readline().split()))
            except Exception as error:
                print("Error:", str(error))
                return
        else:
            print("Error. Try again")
            return

    print(compute_tree_height(n, parents))


sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
