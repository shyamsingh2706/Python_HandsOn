
# https://leetcode.com/problems/longest-consecutive-sequence/

# Time complexity dominated by Sorting which will run in O(nLogn)
def solution(arr):

    sorted_arr = sorted(arr)
    print(sorted_arr)

    if len(arr) == 0 :
        return 0
    elif len(arr) == 1:
        return 1

    longestStreak = 1
    currentStreak = 1

    for i in range(1,len(sorted_arr)):

         if sorted_arr[i] != sorted_arr[i-1] and sorted_arr[i] == sorted_arr[i-1] + 1:
             currentStreak += 1
         else:
             longestStreak = max(longestStreak,currentStreak)
             currentStreak = 1

    return max(longestStreak,currentStreak)

# Time complexity dominated by Sorting which will run in O(n)
def solution_optimized(arr):

    longest_streak = 0

    num_set = set(arr)

    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1

    for num in num_set:
        if num-1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

def main():

    arr = [0,3,7,2,5,8,4,6,0,1]

    print("Length of The longest consecutive elements sequence is : " , solution_optimized(arr))

if __name__ == "__main__":
    main()
