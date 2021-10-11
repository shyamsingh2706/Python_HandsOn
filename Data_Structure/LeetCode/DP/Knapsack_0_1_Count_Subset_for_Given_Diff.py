import Knapsack_0_1_Count_SubSet_Sum
import Knapsack_0_1_SubSet_Sum

## Same as https://leetcode.com/problems/target-sum/
## To achive target Sum , finally  one Subset will have + value and Other subset will be have - values
## Its same as achieving count of Subset for which difference is given Target/Number.

## For this problem , if S1 - S2 = Target to be achived
## S1 + S2 = Array_Sum is also true. If these 2 equations to be considered ,  S1 = (Target + Array Sum) / 2

## That means we have to find out the count of subset for which target is equal to (Target + Array Sum) / 2
## This will intern result the answer for target Sum OR "Count Subset for a given Differnce problems"


def Kanpsack_0_1_Equal_Sum(Input_list,Target):

    sum=0
    for i in Input_list:
        sum += i

    return Knapsack_0_1_Count_SubSet_Sum.Kanpsack_0_1_Count_SubSet_Sum(Input_list, (Target+sum)//2 , len(Input_list))


def main():

    Input_numbers = input('Enter Your Input Array as list of "," seperated numbers : ' )
    target = int(input('Enter Your target Diff : '))

    input_list = Knapsack_0_1_SubSet_Sum.initialize_list(Input_numbers)
    SubSet_Count = Kanpsack_0_1_Equal_Sum(input_list,target)
    #print(SubSet_Count)

    if (SubSet_Count == 0):
        print ("Can Not be divided into two subsets to achieve target Sum")
    else:
        print("Number of subset to achieve target Diff is : " , SubSet_Count)


if __name__ == "__main__" :
    main()