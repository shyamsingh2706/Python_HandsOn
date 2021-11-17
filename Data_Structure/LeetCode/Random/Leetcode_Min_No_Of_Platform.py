
# https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
#  For example, consider the above example.

# arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
# dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}

# All events are sorted by time.
# Total platforms at any time can be obtained by
# subtracting total departures from total arrivals
# by that time.

#  Time      Event Type     Total Platforms Needed
#                                at this Time
#  9:00       Arrival                  1
#  9:10       Departure                0
#  9:40       Arrival                  1
#  9:50       Arrival                  2
#  11:00      Arrival                  3
#  11:20      Departure                2
#  11:30      Departure                1
#  12:00      Departure                0
#  15:00      Arrival                  1
#  18:00      Arrival                  2
#  19:00      Departure                1
#  20:00      Departure                0
#
# Minimum Platforms needed on railway station
# = Maximum platforms needed at any time
# = 3


def findPlatform(arr, dep, n):

    # Sort arrival and
    # departure arrays
    arr.sort()
    dep.sort()

    # plat_needed indicates
    # number of platforms
    # needed at a time
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in
    # merge sort to process
    # all events in sorted order
    while (i < n and j < n):

        # If next event in sorted
        # order is arrival,
        # increment count of
        # platforms needed
        if (arr[i] <= dep[j]):

            plat_needed += 1
            i += 1

        # Else decrement count
        # of platforms needed
        elif (arr[i] > dep[j]):

            plat_needed -= 1
            j += 1

        # Update result if needed
        if (plat_needed > result):
            result = plat_needed

    return result


def main() :

    arr  = [900,940,950,1100,1500,1800]
    dep  = [910,1200,1120,1130,1900,2000]
    n = len(arr)

    Min_No_of_platform = findPlatform(arr,dep,n)
    print(Min_No_of_platform)


if __name__ == "__main__":
    main()
