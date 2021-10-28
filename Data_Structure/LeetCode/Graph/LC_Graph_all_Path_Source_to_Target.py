#https://leetcode.com/problems/all-paths-from-source-to-target/

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows:
# graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
import copy
from collections import deque

def all_path_src_to_tgt_BFS(graph):

    if len(graph) == 0 :
        return

    result_path = [] # create variable to hold all final path when reached on last node
    Q = []

    goal_node = len(graph) - 1 # decide end node i.e. last index of Graph given its a directed acyclic graph as per condition

    # add Node 0 and  its neighbourhood path into Queue
    for node in graph[0]:
        Q.append([0,node])

    # start BFS transversal
    while  len(Q) != 0 :
        # pull first path available in Queue
        path = Q.pop(0)
        # pull last node of the path
        last_node = path[-1]
        # if last node is same as target path , add in result
        if last_node == goal_node:
            result_path.append(path)
        #else continue BFS transversal
        else:
            # pull neighbourhood nodes from last node's index postion of Graph
            neighbours = graph[last_node]
            # navigate the neighbours and add them in queue by appending to existing path
            for nodes in neighbours:
                temp_list = copy.copy(path)
                temp_list.append(nodes)
                Q.append(temp_list)

    # return result path in the very end.
    return result_path

def all_path_src_to_tgt_DFS(graph, cur_node=0, curr_path =[] , res_path=[]):

    # check ig graph dont have a node, return None
    if len(graph) == 0 :
        return

    # create a temp new path and copy previous path details in it
    new_path = copy.copy(curr_path)
    # append current node we are navigating
    new_path.append(cur_node)

    # if current node is same as goal node, append to result path and return
    if cur_node == len(graph) -1 :
        res_path.append(new_path)
        return res_path

    # if not, navigate to neighbour nodes of last accessed node
    for neighbour in graph[cur_node]:
        # do a recursion call to navigate further for neighbour node
        all_path_src_to_tgt_DFS(graph,neighbour,new_path,res_path)

    return res_path

def main():

    global grid

    graph =  [[4,3,1],[3,2,4],[3],[4],[]]

    print("all paths from Source to target node is  " , all_path_src_to_tgt_BFS(graph))
    print("all paths from Source to target node is  ", all_path_src_to_tgt_DFS(graph))

if __name__ == "__main__":
    main()