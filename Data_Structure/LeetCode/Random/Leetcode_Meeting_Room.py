# https://leetcode.com/problems/Meeting-Rooms/
#  Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
#  determine if a person could attend all meetings.

#  For example,
#  Given [[0, 30],[5, 10],[15, 20]],
#  return false.

def MeetingRoom(arr: list[int]):

    sort_arr = sorted(arr)
    #print(sort_arr)
    for i in range(1,len(sort_arr)):
        if sort_arr[i][0] < sort_arr[i-1][1]:
            return False

    return True

def main():

    arr =  [[0, 30],[15, 20],[5, 10]]
    res = MeetingRoom(arr)
    print(res)

if __name__ == "__main__":
    main()