# hill pattern Loop Basic

i = 1
while i <= 5:
    j = 0
    while j < 5 - i:
        print(" ",end=" ")
        j += 1
    p = 0
    while p < i:
        print("*",end=" ")
        p += 1
    j = 1 # Start from 1 to avoid duplicating the peak
    while j < i:
        print("*",end=" ")
        j += 1
    i += 1
    print() 

#Output:
#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *




