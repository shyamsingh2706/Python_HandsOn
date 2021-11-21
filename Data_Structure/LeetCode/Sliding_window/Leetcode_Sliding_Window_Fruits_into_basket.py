# https://leetcode.com/problems/fruit-into-baskets/
# same as Longest substring as K unique char

# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
    # You only have two baskets, and each basket can only hold a single type of fruit.
    # There is no limit on the amount of fruit each basket can hold.
    # Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    # Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
    # Given the integer array fruits, return the maximum number of fruits you can pick.


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        if len(fruits) == 0:
            return 0

        if len(fruits) == 1:
            return 1

        start = 0
        end = 0

        max_fruits = 0
        temp_fruits = []

        while end < len(fruits):
            temp_fruits.append(fruits[end])

            if len(set(temp_fruits)) < 2:
                max_fruits = max(max_fruits, end - start + 1)
                end += 1
            elif len(set(temp_fruits)) == 2:
                max_fruits = max(max_fruits, end - start + 1)
                end += 1
            elif len(set(temp_fruits)) > 2:
                while len(set(temp_fruits)) > 2:
                    temp_fruits = temp_fruits[1:]
                    start += 1

                end += 1

        return max_fruits

    def totalFruit_tuned_using_hashmap(self, fruits: list[int]) -> int:

        if len(fruits) == 0:
            return 0

        fruits_dict =  {}
        start = 0
        end = 0
        max_fruits = 0

        while end < len(fruits):

            fruits_end = fruits[end]
            fruits_dict[fruits_end] = fruits_dict.get(fruits_end, 0) + 1

            while len(fruits_dict) > 2:

                fruits_start = fruits[start]
                start += 1
                fruits_dict[fruits_start] -= 1
                if fruits_dict[fruits_start] == 0:
                    del fruits_dict[fruits_start]

            max_fruits = max(max_fruits, end - start + 1)
            end += 1

        return max_fruits

def main():

    fruits = [0,1,2,2]
    s = Solution()
    print(s.totalFruit_tuned_using_hashmap(fruits))

if __name__ == "__main__":
    main()


