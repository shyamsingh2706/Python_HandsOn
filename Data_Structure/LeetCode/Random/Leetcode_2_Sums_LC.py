
#https://leetcode.com/problems/two-sum/

class cls_solutions_SubSet_sum () :

    def __init__(self,Input_list,target):
        self.Input_list = Input_list
        self.target = target


    def SubSet_Sum_optimmized(self):

        for idx, val in enumerate(self.Input_list):
            if self.target - val in self.Input_list[idx + 1:]:
                #return [idx, self.Input_list[idx + 1:].index(self.target - val) + (idx + 1)]
                return [idx, self.Input_list.index(self.target - val)]

        return "Invalid Target Input"


    ### Through Kanpsack Approach . find max sum for a given Subset if target limit is defined
    def SubSet_Sum_Recurrsion(self,Input_list,Target,Input_list_len):

            if (Target == 0):
                return 0
            elif ( Input_list_len == 0 ):
                return "Invalid Target Input"

            if Input_list[Input_list_len-1] > Target :
                return SubSet_Sum_Recurrsion(Input_list,Target,Input_list_len-1)
            elif Input_list[Input_list_len-1] <= Target :
                if ( Target - Input_list[Input_list_len-1] in  Input_list ):
                     return (Input_list_len-1,Input_list.index(Target - Input_list[Input_list_len-1]))
                return SubSet_Sum_Recurrsion(Input_list, Target, Input_list_len - 1)


def initialize_list(Input_numbers):

    input_list = []
    for j in Input_numbers.split(','):
        input_list.append(int(j))
    return input_list


def main():

    Input_numbers = input('Enter Your Input Array as "," seperated numbers : ' )
    target = int(input('Enter Your target Sum : '))

    #print(Input_numbers)
    #print(target)
    input_list = initialize_list(Input_numbers)
    Input_list_len = len(input_list)
    #print(len_input_list)
    cls_variable=cls_solutions_SubSet_sum(input_list,target)
    output_indices = cls_variable.SubSet_Sum_optimmized()
    #output_indices = cls_variable.SubSet_Sum_Recurrsion(input_list,target,Input_list_len)
    print(output_indices)

main()