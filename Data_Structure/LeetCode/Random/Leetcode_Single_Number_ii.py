# https://leetcode.com/problems/single-number-ii/
# Given an integer array nums where every element appears three times except for one, which appears exactly once.
# Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        def num2bin(num):
            i = 0
            if num < 0:
                num = -num
                count[32] += 1
            while num > 0:
                #print(num)
                num, r = divmod(num, 2)
                #print(num,r,i)
                count[i] += r
                i += 1

        def bin2num(binary):
            mult = 1
            ans = 0
            for i in range(len(binary) - 1):
                #print(binary[i],i,mult)
                #print(mult * binary[i])
                ans += mult * binary[i]
                #print(ans)
                mult *= 2
            return ans


        count = [0] * 33
        #print(count)
        for n in nums:
            num2bin(n)

        #print(count)
        for i in range(len(count)):
            count[i] %= 3

        #print(count)
        res = bin2num(count)
        return res if count[-1] == 0 else -res

def singleNumber(nums: list[int]) -> int:

    ret = 0
    for i in range(32):
        if sum((n >> i) & 1 for n in nums) % 3:
            if i == 31:
                ret -= 2 ** 31
            else:
                ret += (1 << i)
    return ret

def main():

    nums = [2,1,2,1,2,1,99]
    s = Solution()
    res = s.singleNumber(nums)
    print(res)

if __name__ == "__main__":
    main()