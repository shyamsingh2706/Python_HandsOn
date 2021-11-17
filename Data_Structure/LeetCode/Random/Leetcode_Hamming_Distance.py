# https://leetcode.com/problems/hamming-distance/

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        num1 = '{:032b}'.format(x)
        num2 = '{:032b}'.format(y)
        print(num1,num2)
        # 1   00000000000000000000000000000001
        # 4   00000000000000000000000000000100
        cnt = 0
        for i in range(0, 32):
            if num1[i] != num2[i]:
                cnt += 1
        return cnt

def main():
    x = 1
    y = 4
    s = Solution()
    print(s.hammingDistance(x,y))

if __name__ == "__main__":
    main()
