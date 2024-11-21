# print a star
print("*")
# For instance if you want to write stars in a row
i = 6
print("*"*i)#first implementation using print statment
# Another implementation using for loop
i = 6
for j in range(i):
    print("*")
# But the output of above program will be printed on next row by each iteration
i = 6
for j in range(i):
    print("*",end="")

print()
# similarly we can improvise and take input from user 
i = int(input("Enter number of Stars : "))
for j in range(i):
    print("*",)

# print Square
n = 5 
for i in range(n):
    for j in range(n):
        print('$',end='  ')
    print()
    
#similary this program can also have input 
n = int(input("Area of Square input : "))# THIS WILL TAKE YOUR GIVEN INPUT AS LENGTH AND BREATH OF THE SQUARE AS LxB
item = input("Item that u want to print in square :")# THIS CAN BE ANYTHING EMOJI ETC
for i in range(n):
    for j in range(n):
        print(item,end='  ')
    print()# Athough this print statment seems useless but it has its significance as it changes the line after each iteration