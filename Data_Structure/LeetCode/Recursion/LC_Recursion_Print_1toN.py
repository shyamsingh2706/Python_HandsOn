

def print_num(N):

    # base condition
    if N == 1 :
        print(1)
        return

    # hypothesis ( design function for smaller Input )
    print_num (N-1)

    # Induction
    print(N)

def main():

    print_num(7)

if __name__ == "__main__":
    main()