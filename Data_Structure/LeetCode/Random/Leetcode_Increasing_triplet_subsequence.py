import sys

# https://leetcode.com/problems/increasing-triplet-subsequence/

def solution(arr):

    if len(arr) <= 2 :
        return False


    for j in range(0, len(arr) - 2 ): ## len -2 as Range is not considering last index as its exclusive that intern meant as loop will run until len - 3
        if arr[j] < arr[j+1] < arr[j+2]:
            return True

    return False

def increasingTriplet(arr):


    Min_element = sys.maxsize
    triplet_subSeq = []

    for j in arr :

        if len(triplet_subSeq) == 0 or j < min_element:
            min_element = j
            triplet_subSeq = []
            triplet_subSeq.append(j)
        elif len(triplet_subSeq) == 1 and j > min_element :
            min_element = j
            triplet_subSeq.append(j)
        elif len(triplet_subSeq) == 2 and j > min_element :
            min_element = j
            triplet_subSeq.append(j)
            #print(triplet_subSeq)
            return True

    return False

def main():

    arr = [2,1,5,0,4,6]

    print(increasingTriplet(arr))

if __name__ == "__main__":
    main()
