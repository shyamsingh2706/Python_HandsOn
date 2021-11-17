# https://leetcode.com/problems/moving-average-from-data-stream/
# Given a stream of integers and a window size,
# calculate the moving average of all integers in the sliding window.

class MovingAvg():

    def __init__(self,window_size=0):
        self.window_size = window_size
        self.arr = [] # Queue
        self.sum = 0

    def next(self,data=0):

        if  len(self.arr) == self.window_size:
            temp = self.arr.pop(0)  # is queue size is same as window size, pop from queue
            self.sum = self.sum - temp

        self.arr.append(data)
        self.sum = self.sum + data

        return self.sum / len(self.arr)

def main():

    m = MovingAvg(3)
    print(m.next(1))
    print(m.next(10))
    print(m.next(3))
    print(m.next(5))


if __name__ == "__main__":
    main()

