import math
import os
def mostBalancedPartition(parent, files_size):
    # Write your code here
    n = len(parent)
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[parent[i]].append(i)
    sizeSums = [None for _ in range(n)]
    
    def size_sums_rec(i):
        sizeSums[i] = files_size[i] + sum(size_sums_rec(child) for child in children[i])
        return sizeSums[i]
    
    size_sums_rec(0)
    return min(abs(sizeSums[0] - 2 * size_sum) for size_sum in sizeSums[1:])

 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()
