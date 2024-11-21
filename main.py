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