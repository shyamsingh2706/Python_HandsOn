# https://leetcode.com/problems/online-stock-span/
# https://www.geeksforgeeks.org/the-stock-span-problem/

# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days.
# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
# then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

from collections import deque

def stock_span(arr):

    stk = deque()
    stock_span =[]


    for i in range(0,len(arr),1 ):

        span_count = 1

        # if stack is empty , consider 1 as default count
        if len(stk) == 0:
            stock_span.append(span_count)

        # if current element is smaller than previous element
        # No consicutive fall in stock price
        # default it to 1
        elif len(stk) > 0 and arr[i] < stk[-1] :
            stock_span.append(span_count)

        # if current stock price is
        # pop Until you find a greater element
        elif len(stk) > 0 and arr[i] >= stk[-1] :
            # create a temp stack to hold the stock price that are being popped
            temp_stk = deque()
            while len(stk) > 0 and arr[i] >= stk[-1]:
                # everytime an element is popped
                # means previous day's price is lower than current
                # increse the span count
                temp_stk.append(stk.pop())
                span_count += 1

            # once captured the span count for a given day for consicutuve fall
            stock_span.append(span_count)

            # Insert back all the stock prices that were popped up while checking above criteria
            while len(temp_stk) > 0:
                stk.append(temp_stk.pop())

        # finally add currnet element in stack
        stk.append(arr[i])

    return (stock_span)

def stock_span_another(arr):

    stk = [] ## Wil capture element in stack and its associated Index
    NGR = [] ## Will capture Index of nearest greater to left element

    for i in range(0, len(arr), 1):

        if len(stk) == 0:
            NGR.append(-1) # capture Index as -1

        elif len(stk) > 0 and arr[i] < stk[-1][0]:
            NGR.append(stk[-1][1]) ## Push Index of the element thats on top

        elif len(stk) > 0 and arr[i] > stk[-1][0]:
            while len(stk) > 0 and arr[i] > stk[-1][0]:
                stk.pop()

            if len(stk) == 0:
                NGR.append(-1)
            else:
                NGR.append(stk[-1][1]) ## Push Index of the element thats on top

        stk.append([arr[i],i]) ## Push the elements and its Index in stack

    #print((NGR))

    Stock_span_days=[]
    # if we minus the index of array vs the index of nearest greater to left element
    # it will return consicutive stock span days
    for i in range(0,len(arr)):
        Stock_span_days.append(i - NGR[i])

    return Stock_span_days

def main() :

    arr = [100,80,60,70,60,75,85]
    stock_span_Arr  = stock_span(arr)
    Stock_span_days_Arr  = stock_span_another(arr)
    print ("stock Span consicutive days are : ", stock_span_Arr)
    print ( "Nearest Smaller Number to left is : ", Stock_span_days_Arr)
if __name__ == "__main__":
    main()