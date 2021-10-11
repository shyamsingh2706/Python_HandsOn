
# Find Unique char in string given next char is always bigger than the previous one.

def Unique_String(X):

    Unique_Str=""
    temp = ""
    for idx,val in enumerate(X):
        if val != temp :
            if ( ord(val) >  ord(X[idx-1]) or temp == "" ) :
                Unique_Str = Unique_Str + val
            temp = val

    return Unique_Str


def main() :

    arr  = "bbaaccceeedd"

    Unique_Str  = Unique_String(arr)
    print(Unique_Str)


if __name__ == "__main__":
    main()