# https://leetcode.ca/2016-10-18-323-Number-of-Connected-Components-in-an-Undirected-Graph/
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# video explanation
# https://www.youtube.com/watch?v=ymxPZk7TesQ&list=PLtQWXpf5JNGJrA4oZNuF8pRfdxRq3XVm9&index=10

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.

# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2

def Solution(n,edges):

    global ids
    ids = []

    #initialize Ids
    for i in range(n):
        ids.append(i)

    # Union the set
    for i in edges:
        union(i[0],i[1],ids)

    #print(ids)

    # post mergging the subsets, we need to count how many unique subsets we have
    unique_set = set()

    # loop through IDs array and find the parent against each edge and add in set
    for i in range(n):
        temp = find(i, ids)
        unique_set.add(temp)

    #print(ids)
    return len(unique_set)

# union will take 2 edges and ids array that we created
# find parent of edge1 , find parent of edge2 a
# asign one of the parent to other one
def union(edge1,edge2,ids):

    parent1 = find(edge1,ids)
    parent2 = find(edge2,ids)

    # Assign parent1 equal to parent 2
    ids[parent1] = parent2

# will return the parent for a given edge
def find(edge,ids):
    #parent is when the index is same as value of the index
    if ids[edge] != edge :
        # if not same find the parent recursively
        ids[edge] = find(ids[edge],ids)
    return ids[edge]

def main():

    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]

    print("Number of connected component in an undirected graph is " , Solution(n,edges))

if __name__ == "__main__":
    main()