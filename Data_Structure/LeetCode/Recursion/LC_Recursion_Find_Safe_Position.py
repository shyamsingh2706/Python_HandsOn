# https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle1840/1

# There are n people standing in a circle (numbered clockwise 1 to n) waiting to be executed.
# The counting begins at point 1 in the circle and proceeds around the circle in a fixed direction (clockwise).
# In each step, a certain number of people are skipped and the next person is executed.
# The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom.
# Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle.
# The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

# Input:
# n = 2, k = 1
# Output:
# 2
# Explanation:
# Here, n = 2 and k = 1, then safe position is 2 as the person at 1st position will be killed.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

def solve(person,index,k):

    if len(person) == 1:
        print("safe postion for the person will be ", person[0])
        return

    index = (index+k) % len(person)
    del person[index]
    solve(person,index,k)

    return

def main():

    n = 4
    k = 2

    global person
    person = []
    index =0

    for i in range(1,n+1):
        person.append(i)

    # k-1 index will be called as person count includes the start index
    solve(person,index,k-1)

if __name__ == '__main__':
    main()