import Knapsack_0_1_SubSet_Sum

### If Subset can be devided into 2 equal set , the sum of the input list has to be even number
### If not a even number , we can straight away result false
### If Even Number , we can call Sub set sum logic for total sum / 2 to find if we have a set matching with this sum.
### If not , other half wont be valid anyways.
### https://www.geeksforgeeks.org/partition-problem-dp-18/

def Kanpsack_0_1_Equal_Sum(Input_list):

    sum=0
    for i in Input_list:
        sum += i

    if sum%2 != 0 :
        return False
    else:
        return Knapsack_0_1_SubSet_Sum.SubSet_Sum_DP_Tabulation(Input_list,sum//2,len(Input_list))


def main():

    Input_numbers = input('Enter Your Input Array as list of "," seperated numbers : ' )
    input_list = Knapsack_0_1_SubSet_Sum.initialize_list(Input_numbers)
    if (Kanpsack_0_1_Equal_Sum(input_list) == True):
        print("Can be divided into two subsets of equal sum")
    else:
        print("Can Not be divided into two subsets of equal sum")


if __name__ == "__main__" :
    main()