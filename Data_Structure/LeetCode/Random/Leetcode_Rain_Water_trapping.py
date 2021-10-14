#https://leetcode.com/problems/trapping-rain-water/
#https://www.geeksforgeeks.org/trapping-rain-water/

# here the rain trapping water can be calculated through capturing the max height of building at both end
# Once we get max height building at both end , we have to select the min height among both to calculate the water storage among both
# then we have to minus the height of the building to finally calculate net trapped rain water for a given builing structure

import numpy as np
def trapping_rain_water(arr):

    N = len(arr)
    # calculate Max_right_building_arr for every index
    Max_right_building_arr = []
    Max_right_building_arr = np.full((N),0).tolist()

    # initialize the last element same as initlal array as we dont have any other building after last index , so that the max height
    # Read the previous element of array and compare with previous element of max Right height array
    # save the max height among these 2 into current index into max height array
    # for e.g. In first loop..
    #   org arr             3 0 0 2 0 4
    # org Max Arr           0 0 0 0 0 4
    # revised max arr       0 0 0 0 4 4

    Max_right_building_arr[N-1] = arr[-1]
    for i in range(N-2,-1,-1):
        Max_right_building_arr[i] = max(arr[i],Max_right_building_arr[i+1])

    #print(Max_right_building_arr)

    # calculate the max_left_building_arr for every index
    max_left_building_arr = []
    max_left_building_arr = np.full((N), 0).tolist()

    max_left_building_arr[0] = arr[0]
    for i in range(1, N, 1):
        max_left_building_arr[i] = max(arr[i], max_left_building_arr[i-1])

    #print(max_left_building_arr)
    # Calculate minimum among both to find the hieght upto which water can be stored
    # then minus building height fromt his to calulate net amount of water that can be stored against a given index
    # water = min(Max_right_building_arr ,max_left_building_arr) - building height
    water=[]
    for i in range(0, N, 1):
        water.append( min(Max_right_building_arr[i],max_left_building_arr[i]) - arr[i])

    #print(water)

    total_collected_water = 0
    # Calculate total collected water
    for i in range(0,N,1):
        total_collected_water = total_collected_water + (water[i])

    return total_collected_water

def main() :

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    total_collected_water  = trapping_rain_water(height)
    print ( "Total collected water will be : ", total_collected_water)

if __name__ == "__main__":
    main()