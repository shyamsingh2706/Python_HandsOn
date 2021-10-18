# https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/

# There are given n ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to the sum of their lengths. We need to connect the ropes with minimum cost.

# For example, if we are given 4 ropes of lengths 4, 3, 2, and 6. We can connect the ropes in the following ways.
# 1) First, connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6, and 5.
# 2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
# 3) Finally connect the two ropes and all ropes have connected.

# Total cost for connecting all ropes is 5 + 9 + 15 = 29. # This is the optimized cost for connecting ropes.
# Other ways of connecting ropes would always have same or more cost.
# For example, if we connect 4 and 6 first (we get three strings of 3, 2, and 10), then connect 10 and 3 (we get two strings of 13 and 2).
# Finally, we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38.


import heapq

def find_min_cost(arr):

    heap=[]
    for i in arr:
        ## creating Min heap as we have to calculate minimal cost so we need Minimum element on top of heap
        heapq.heappush(heap,i)

    print(heap)
    total_cost = 0

    while len(heap) > 1:
        # pop 2 elements from Heap (min Elements )
        element_1 = heapq.heappop(heap)
        element_2 = heapq.heappop(heap)
        # Push their total cost back in heap to find further min post these 2 element consideration
        sum = element_1 + element_2
        # capture total cost at each step that will be minimum
        total_cost = total_cost + sum
        heapq.heappush(heap,sum)

    return total_cost



def main():

    arr = [2, 3, 4, 6]
    print("minimum cost for connecting ropes is " , find_min_cost(arr))

if __name__ == "__main__":
    main()