# https://leetcode.ca/all/681.html
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23
import collections


def next_closest_time(time:str) -> str :

    # convert time into Minute for Hour part
    minute = int(time.split(':')[0] ) * 60
    # add Minute part to calculat final minute
    minute = minute + int(time.split(':')[1])

    # create haspmap for a all digits present in given time
    digits = time.split(':')[0] + time.split(':')[1]
    digits_dict = collections.Counter(digits)

    is_valid = False

    # loop through to add a minute and check if its a valid time and all numbers aer same as out input
    while not is_valid:

        # add a min and wrap it up in case of 24 hours are over for e.g. 23:59 next min will be 00:00
        minute= (minute+1) % (24*60)
        # calculate 4 digits for hour and min
        # hour's first digit is minute//60//10
        # hour's secon digit is minute//60%10
        # Second's first digit should be minute%60//10
        # second's second digit will be minute%60%10
        next_time = [minute//60//10,minute//60%10,minute%60//10,minute%60%10]
        counter = 0
        # check if all digitis are part of digit dict
        for i in next_time:
            if str(i) in digits_dict.keys():
                counter += 1

        # if yes , return the time back
        if counter == 4 :
            is_valid = True
            return str(next_time[0]) + str(next_time[1]) + ':' + str(next_time[2]) + str(next_time[3])


def main():

        time = "23:59"
        res = next_closest_time(time)
        print(res)

if __name__ == "__main__":
    main()