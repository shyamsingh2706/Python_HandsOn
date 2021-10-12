
# https://leetcode.com/problems/allocate-mailboxes/
# https://leetcode.com/problems/allocate-mailboxes/discuss/1513947/The-explanation-you've-been-waiting-for
import sys

def loop (houses, start , end , num_mailboxes ) :

    num_houses = end - start + 1
    dist = 0

    if num_houses == num_mailboxes:
        return 0
    if num_mailboxes == 1:
        if num_houses % 2 == 0:
            mid = start + num_houses // 2
            pos = houses[mid - 1] + (houses[mid] - houses[mid - 1]) // 2
        else:
            mid = start + (num_houses - 1) // 2
            pos = houses[mid]

        return sum(abs(pos - houses[i]) for i in range(start, end + 1))


    min_dist = sys.maxsize
    for i in range(start, len(houses) - num_mailboxes + 1):
        dist = loop(houses,start, i, 1) + loop(houses,i + 1, end, num_mailboxes - 1)
        min_dist = min(min_dist, dist)

    return min_dist

def minDistance( houses , k ):

    houses.sort()
    Min_dist =  loop( houses, 0 , len(houses) - 1 , k)

    return Min_dist


def main():

    houses = [1,4,8,10,20]
    k = 3

    Min_dist = minDistance(houses,k)

    print("Min Ditance is :", Min_dist)

if __name__ == "__main__":

    main()