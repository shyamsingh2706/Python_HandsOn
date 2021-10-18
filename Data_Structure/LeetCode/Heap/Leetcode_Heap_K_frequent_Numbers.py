# https://leetcode.com/problems/top-k-frequent-elements/

import heapq

def find_k_frequent_Numbers(arr,k):

    freq_dict = {}
    count = 1
    for j in arr:
        if j in freq_dict.keys():
            freq_dict[j] = freq_dict[j] + 1
        else:
            freq_dict[j] = count

    heap = []

    for key in freq_dict.keys():
        heapq.heappush(heap,(freq_dict[key],key)) # creating Min heap as we need to find most freq numbers
        if len(heap) > k :
            heapq.heappop(heap)

    result = []
    while heap:
        result.append(heapq.heappop(heap)[1])

    return result

def main():

    heap = [1,1,1,3,2,2,4]
    k = 2
    print(find_k_frequent_Numbers(heap,k))


if __name__ == "__main__":
    main()