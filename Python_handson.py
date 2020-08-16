### Program to find next prime number

def isPrime(n):
    # Corner case
    if (n <= 1):
        return False

    # Check from 2 to n-1 
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def find_all_prime_until (m):

    loop = 1
    while True:
        nextnum = m+loop
        if isPrime(nextnum):
            break
        else:
            loop += 1
            continue
    return nextnum

first_input = True
to_be_continue ='Y'


while True:

    to_be_continue = input('you want to continue to find next prime Number (y/n): ')

    if first_input :

             input_number = input('Input a number to find next prime number : ')
             first_input = False
             next_prime = int(input_number)

    if (to_be_continue.upper() == 'Y'):

              new_next_prime = find_all_prime_until(next_prime)
              print(f" next prime number for input number {next_prime} is {new_next_prime}")
              next_prime = new_next_prime
    else:
              print("Thank you !!! ")
              break