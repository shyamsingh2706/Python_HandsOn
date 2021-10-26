# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order


def solve(digits, op='', res=[] ):

    dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

    if  len(digits) == 0:
        res.append(op)
        return

    for ch in dict[digits[0]]:
        solve(digits[1:], op+ch, res)

    return res

def main():

    arr ="23"
    print("Letter Combinations of a Phone Number is " , solve(arr))

if __name__ == "__main__" :
    main()