
i = 6
print("1"*i)#first implementation using print statment
# Another implementation using for loop
i = 6
for j in range(i):
    print(i)
# But the output of above program will be printed on next row by each iteration
n=11
for j in range(i,n):
    print(i,end=" ")

print()
# similarly we can improvise and take input from user 
n = int(input("Enter endpoint of numbers : "))
for j in range(n):
    print(i, end=" ")
i += 1

# # print Square
n = 6 
for i in range(n):
    for j in range(n):
        print( i ,end='  ')
    print()
    
#similary this program can also have input 
n = int(input("Area of Square input : "))# THIS WILL TAKE YOUR GIVEN INPUT AS LENGTH AND BREATH OF THE SQUARE AS LxB
item = input("Item that u want to print in square :")# THIS CAN BE ANYTHING EMOJI ETC
for i in range(n):
    for j in range(n):
        print(item,end='  ')
    print()# Athough this print statment seems useless but it has own significance as it changes the line after each iteration
    

# Output 
i = 1
while i <= 5:
    j = 1 
    while j <= i:
      print(i ,end = " ")
      j = j + 1
    print()
    i=i+1

# Output 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5



# in while Loop
i = 1 
j = 1
while(i<=8):
    while(j<=8):
        print( i , end=" ")
        j+=1
    i+=1
    j=1
    print(" ")

# Output 
# 1 1 1 1 1 1 1 1  
# 2 2 2 2 2 2 2 2  
# 3 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5
# 6 6 6 6 6 6 6 6
# 7 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8