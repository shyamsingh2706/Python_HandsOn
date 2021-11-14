# https://leetcode.com/problems/paint-house/
# https://www.youtube.com/watch?v=fZIsEPhSBgM&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=18

# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green.
# The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.


def paint_house(cost):

    n = len(cost)

    if n == 0 :
        return 0

    for i in range(1,n):

        cost[i][0] = cost[i][0] + min(cost[i-1][1] , cost[i-1][2])
        cost[i][1] = cost[i][1] + min(cost[i-1][0], cost[i-1][2])
        cost[i][2] = cost[i][2] + min(cost[i-1][0] , cost[i-1][1])

    return min(min(cost[n-1][0],cost[n-1][1]),cost[n-1][2])

def main():


    cost = [
        [17,2,17],
        [16,16,5],
        [14,3,19]
        ]

    print("Min cost is for paiting houses is, " , paint_house(cost))

if __name__ == "__main__":
    main()