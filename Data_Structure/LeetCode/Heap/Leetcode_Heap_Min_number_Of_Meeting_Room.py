
# https://leetcode.com/problems/meeting-rooms-ii/
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number of conference rooms required.
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2


import heapq
def MeetingRoom(Intervals):

    Intervals.sort()
    meeting_rooms = 1

    # initialize Heap
    # set heap with fist meeting End time
    heap = []
    heap.append(Intervals[0][1])

    #loop through remianing Interval
    for start,end in Intervals[1:]:
        # if current meeting start time is greater than or equal to min end time of previous meetings
        # i.e. Last eneded meeting that has min end time , Min heap will maintain the order
        if heap[0] <= start:
            # means meeting rooms are available
            # pop the last eneded meeting that has min end time
            heapq.heappop(heap)
        # insset the end time as current meetings end time
        # i.e. Block the room again
        heapq.heappush(heap,end)
        # calculate the meeting room numbers
        meeting_rooms = max(meeting_rooms,len(heap))

    return meeting_rooms

def main() :

    Intervals  = [[1, 3], [1, 3], [4, 6], [4, 10], [6, 8], [6, 9], [9, 11]]


    Res = MeetingRoom(Intervals)
    print(Res)


if __name__ == "__main__":
    main()