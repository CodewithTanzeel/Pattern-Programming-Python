# Basic For loops
n = 5 
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
 
# In while loops

i = 5 
while i >= 1:
    j = 1 
    while j<= i:
      print("*",end = " ")
      j = j + 1
    print()  
    i = i - 1