# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, arr: list[int]) -> int:

        left_index = 0
        right_index = len(arr) - 1
        max_water = 0

        while right_index > left_index:
            # take min height building maong both and calculate water
            height = min(arr[right_index], arr[left_index])
            water = height * (right_index - left_index)
            max_water = max(water, max_water)

            # while ever is smaller, move that index forward and recalculate water volume
            if arr[right_index] > arr[left_index]:

                left_index += 1

            else:
                right_index -= 1

        return max_water

def main() :

    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    total_collected_water  = s.maxArea(height)
    print ( "Total collected water will be : ", total_collected_water)

if __name__ == "__main__":
    main()