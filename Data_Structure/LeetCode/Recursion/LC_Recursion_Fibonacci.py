#https://leetcode.com/problems/fibonacci-number/

def fibonacci(N):

    if N < 2:
        return N

    sum = fibonacci(N-1) + fibonacci(N-2)

    return sum

def main():

    print(  " Fibonacci numbers is " , fibonacci(9))

if __name__ == "__main__":
    main()

