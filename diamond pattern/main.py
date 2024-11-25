print("This is  Diamond Pattern")
print()
n = 5 
for i in  range(n-1):

    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ') 
    print()
for i in  range(n):

    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):  # -1 is important to make both of the decreasing triangle symmetric
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    
    
    print()
    





