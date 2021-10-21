# https://leetcode.com/problems/factorial-trailing-zeroes/

def factorial(N):

    if N < 2:
        return N

    Fact = N * factorial(N-1)

    return Fact


def trailing_zeros(factorialResult):

    toString = str(factorialResult)
    trailingZeroes = 0

    for i in reversed(toString):

        if i != '0':
            break
        else:
            trailingZeroes += 1

    return trailingZeroes

def main():

    fact_rslt = factorial(9)
    print(  " factorial is " ,factorial(9) )
    print(  " factorial trailing 0 is " ,trailing_zeros(fact_rslt) )


if __name__ == "__main__":
    main()

