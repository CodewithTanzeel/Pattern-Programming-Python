# n = 5
# for j in range(n):
#     print('*')
# output 
# *
# *
# *
# *
# *



# n = 5
# for j in range(n):
#     print('*', end=' ')
    # Output
    # * * * * *


# n = 5
# for i in range(n):
#   for j in range(n):
#       print('*', end='')

# output
# * * * * * * * * * * * * * * * * * * * * * * * * * 


# n = 5
# for i in range(n):
#   for j in range(n):
#       print('*')

#ouput
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *

# n = 5 
# for i in range(n):# rows 
#    for j in range(n):#coloumn
#       print('*',end=' ')
#    print()
#output
# * * * * *
# * * * * *
# * * * * * 
# * * * * *
# * * * * *

#square parallel bar pattern 

# n = 5 
# for i in range(n):
#    for j in range(n):
#       if (j==0 or j == n-1):
#          print('*',end=' ')
#       if (j==1 or j ==2 or j == 3):
#          print(' ',end=' ')
#    print()


# PLUS sign

# n = 5 
# for i in range(n):
#    for j in range(n):
#       if (i == n//2 or j == n // 2):
#          print('*',end=' ')
#       else:
#          print(' ',end=' ')
#    print()

#ouput :
#     *     
#     *     
# * * * * *
#     *
#     *
 
# X cross sign
# n = 5 
# for i in range(n):
#    for j in range(n):
#       if (i == j or i + j == n-1):
#          print('*',end=' ')
#       else:
#          print(' ',end=' ')
#    print()

# *       * 
#   *   *   
#     *
#   *   *
# *       *


# Hollow square pattern 

# n = 5 
# for i in range(n):
#    for j in range(n):
#       if (i == 0 or i == n - 1 or j == 0 or j == n -1):
#          print('*',end=' ')
#       else:
#          print(' ',end=' ')
#    print()
# output 
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# hollow triangle program
# n = 5
# for i in range(n):
#    for j in range(i+1):
#     print('*',end=' ')
#    print()

#output
# *
# * *
# * * *
# * * * *
# * * * * *

# n = 5
# for i in range(n):
#    for j in range(i+1):
#     if (i == n-1 or j == i or j == 0):
#        print('*',end=' ')
#     else:
#        print(' ',end=' ')

#    print()

# output
# * 
# * * 
# *   *
# *     *
# * * * * *

# n = 5
# for i in range(n):
#    for j in range(i,n):
#     if (i == 0 or j == i or j == n-1):
#        print('*',end=' ')
#     else:
#        print(' ',end=' ')

#    print()

#Ouput
# * * * * *
# *     *
# *   *
# * * 
# *


# Hollow paramid pattern
n = 5
for i in range(n):
   for j in range(i,n):
      print('',end='')
   for j in range(i):
      print('*',end='')
   for j in range(1+i):
      print('*',end='')

   print()

