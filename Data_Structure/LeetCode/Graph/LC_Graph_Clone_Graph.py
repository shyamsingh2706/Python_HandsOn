#https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
class Node():

    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


import copy
def CloneGraph(Graph):

    if len(Graph) == 0 :
        return
    New_graph = copy.deepcopy(Graph)
    return New_graph

def CloneGraphDFS(Graph):

    # create an empty Adj list that will hold new graph nodes
    new_graph_adjList =[]

    # create a map to hold mapping of Old vs new nodes
    global map
    map = {}

    # loop through every graph node and create a copy of new node
    for node in Graph:
        # if empty node , copy will also be empty
        if not node:
            return node
        else:
            # create a new node
            new_node = CloneGraphDFSNode(node,map)
            # add that new node to new Adj List
            new_graph_adjList.append(new_node)

    # return this new Adj list
    return new_graph_adjList

def CloneGraphDFSNode(node,map):

    # create copy of existing node

    # if not a node , return the same
    if not node:
        return node
    # if for old node, new node is already created , return the same
    elif id(node) in map.keys():
        return map[id(node)]
    # else create a new node for old node
    else:
        # creae a copy
        copy = Node(node.val,neighbors=[])
        # store the same in Map against old node address
        map[id(node)] =  copy
        # loop through neighbours of existing old node
        for old_neighbours in node.neighbors:
            # append the same against copy's neighbours list
            # do a recursion call to create a copy of a neighbour node in case its copy is not created yet
            map[id(node)].neighbors.append(CloneGraphDFSNode(old_neighbours,map))

    # return the copy
    return copy

def buildGraph():

    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()

    node1.val = 1
    node2.val = 2
    node3.val = 3
    node4.val = 4

    node1.neighbors = [node2,node4]
    node2.neighbors = [node1,node3]
    node3.neighbors = [node2,node4]
    node4.neighbors = [node1,node3]

    graph = []
    graph.append(node1)
    graph.append(node2)
    graph.append(node3)
    graph.append(node4)

    return graph


def main():

    #graph = {1: [2,4],2: [1,3],3: [2,4],4: [1,3] }

    graph_adj_list = buildGraph()

    for node in graph_adj_list:
        print(f"existing node is {node} , its value is {node.val}  and its neighbour's address is {node.neighbors} ")

    new_graph_adjList = CloneGraph(graph_adj_list)

    for node in new_graph_adjList:
        print(f"new graph node through deep copy function is {node} , its value is {node.val}  and its neighbour's address is {node.neighbors} ")

    new_graph_adjList_DFS = CloneGraphDFS(graph_adj_list)

    for node in new_graph_adjList_DFS:
        print(f"new graph node through DFS is {node} , its value is {node.val}  and its neighbour's address is {node.neighbors} ")



if __name__ == '__main__':
    main()