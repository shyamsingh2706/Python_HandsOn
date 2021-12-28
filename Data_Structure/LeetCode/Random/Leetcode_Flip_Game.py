# https://leetcode.ca/2016-09-18-293-Flip-Game/
#  You are playing the following Flip Game with your friend:
#     Given a string that contains only these two characters: + and -,
#     you and your friend take turns to flip two-consecutive "++" into "--".

#  The game ends when a person can no longer make a move and therefore the other person will be the winner.
#  Write a function to compute all possible states of the string after one valid move.
#  For example, given s = "++++", after one move, it may become one of the following states:

#  [
#    "--++",
#    "+--+",
#    "++--"
#  ]

#  If there is no valid move, return an empty list [].

## using sliding window
def flip_game_SW(signs):
    start = 0
    end = 0
    result = []
    counter = 0
    res = ''

    while end < len(signs):

        if signs[end] == '+':
            counter = counter + 1

        if end - start + 1 < 2:
            end += 1

        elif end - start + 1 == 2:
            if counter == 2:

                for j in range(0, start):
                    res = res + signs[j]

                for i in range(start, end + 1):
                    if signs[i] == '+':
                        res = res + '-'
                    else:
                        res = res + signs[i]

                for j in range(end + 1, len(signs)):
                    res = res + signs[j]

                result.append(res)

            end += 1
            start += 1
            counter -= 1
            res = ''

    return result


## using Restore method

def flip_game(signs):
    result = []
    for i in range(1, len(signs)):
        res = ''
        if signs[i] == '+' and signs[i - 1] == '+':
            res = res + signs[0:i - 1]
            res = res + '--'
            res = res + signs[i + 1:]
            result.append(res)

    return result


def main():
    signs = '++++'
    print("combination for next move is ", flip_game(signs))


if __name__ == "__main__":
    main()