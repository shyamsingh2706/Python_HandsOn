
#https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

def calculate_min_platform(X,Y):

    Max_no_platform = 1
    Curent_platform_Count = 0

    Arrival_time = X[0]
    Departure_time = Y[0]

    if (len(X)== 1 and len(Y) == 1 ) :

        return Max_no_platform

    for i in range(1,len(X)):

        cur_arv = X[i]
        curr_dep = Y[i]

        if X[i] > Arrival_time and  X[i] < Departure_time :
            Curent_platform_Count += 1
            Departure_time = max(Y[i],Departure_time)
            Arrival_time = max(X[i], Arrival_time)
            Max_no_platform = max(Curent_platform_Count,Max_no_platform)
        else:
            Departure_time = max(Y[i], Departure_time)
            Arrival_time = max(X[i], Arrival_time)

    return Max_no_platform


def main() :

    arr  = [900,940,950,1100,1500,1800]
    dep  = [910,1200,1120,1130,1900,2000]

    Min_No_of_platform = calculate_min_platform(arr,dep)
    print(Min_No_of_platform)


if __name__ == "__main__":
    main()