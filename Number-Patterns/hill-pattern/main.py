# Hill Pattern Basic in number
print("This is a  hill pattern in numbers")
n = 5 
for i in  range(n):

    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print(i,end=' ')
    for j in range(i+1):
        print(i,end=' ')
    
    
    print()
    


print("This is a reverse hill pattern in numbers")
n = 5 
for i in  range(n):

    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):  # -1 is important to make both of the decreasing triangle symmetric
        print(i,end=' ')
    for j in range(i,n):
        print(i,end=' ')
    
    
    print()