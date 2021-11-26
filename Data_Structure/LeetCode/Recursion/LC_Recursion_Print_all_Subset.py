# https://leetcode.com/problems/subsets/
# https://www.tutorialcup.com/leetcode-solutions/subset-leetcode.htm

#Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

#             op    ip
#             ""   "ab"
#       op    ip            op          ip
#      " "   "b"           "a"         "b"   --> a is not considered in left decision tree but considered in right decision tree
#    op    ip   op      op    ip    op     ip
#   " "   " "  "b"     "a"    " "  "ab"   " " --> for each element , either its not considered in left decision tree or its considered in right decision tree

def print_all_subset(arr,output_arr=[],op=''):


    if len(arr) == 0 :
        output_arr.append([op])
        return

    op1 = op  # initialize Both Output of decesion tree as initial output string # for the decesion tree where we are not considering the first element
    op2 = op  # initialize Both Output of decesion tree as initial output string # for the decesion where we are considering the first element

    op2 = op2 + str(arr[0])  # initialize Output2 string with 0th Index as we are considering first element in array and remaining element has to go through decesion tree
    arr= arr[1:] # reset array with remaining element
    print_all_subset(arr,output_arr,op1)
    print_all_subset(arr,output_arr,op2)

    return output_arr

# if it has to go in Array form 
class Solution:
    def subsets(self, nums) :
        res = self.print_all_subset(nums, [], [])
        return res

    def print_all_subset(self, nums, output_arr, op):
        if len(nums) == 0:
            output_arr.append([op][0])
            return

        op1 = op.copy()  # initialize Both Output of decesion tree as initial output string # for the decesion tree where we are not considering the first element
        op2 = op.copy()  # initialize Both Output of decesion tree as initial output string # for the decesion where we are considering the first element

        op2 = op2 + [nums[0]]  # initialize Output2 string with 0th Index as we are considering first element in array and remaining element has to go through decesion tree
        nums = nums[1:]  # reset array with remaining element
        self.print_all_subset(nums, output_arr, op1)
        self.print_all_subset(nums, output_arr, op2)

        return output_arr

def main():

    arr = [1,2,3]
    s = Solution()
    print(s.subsets(arr))

if __name__ == "__main__":
    main()
