# https://practice.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1
# https://leetcode.com/discuss/interview-question/1392284/solving-tower-of-hanoi-using-the-magic-of-recursion

# The tower of Hanoi is a famous puzzle where we have three rods and N disks.
# The objective of the puzzle is to move the entire stack to another rod.
# You are given the number of discs N. Initially, these discs are in the rod 1.
# You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.

# You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk cannot be placed on top of a smaller disk.

# Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N.
# Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc.


# Input:
# N = 2
# Output:
# move disk 1 from rod 1 to rod 2
# move disk 2 from rod 1 to rod 3
# move disk 1 from rod 2 to rod 3
# 3
# Explanation: For N=2 , steps will be
# as follows in the example and total
# 3 steps will be taken.


def tower_of_hanoi(n,s,d,h):

    count = 1

    if n == 1:
        print(f" move disk {n} from rod {s} to rod {d}")
        return 1

    # put N-1 rod from Source to helper
    # ie. Source rod is s
    # destination rod is h
    # and helper rod is d
    count = count + tower_of_hanoi(n-1,s,h,d)

    # move N-1 th rod from Source to destination now as remaning disks are in helper rod
    print(f" move disk {n-1} from rod {s} to rod {d}")

    # now move N-1 rods from helper rod to destination rod
    # i.e. source rod is h
    # targer rod is d
    # helper rod is s
    count = count +  tower_of_hanoi(n - 1, h, d, s)

    return count ;


def main():

    N = 3
    s = 1 # Source rod number is 1
    h = 2 # helper rod number of 2
    d = 3 # destination rod number is 3

    total_steps = tower_of_hanoi(N,s,d,h)
    print(" total number of steps needed is ", total_steps )

if __name__ == "__main__":
    main()
