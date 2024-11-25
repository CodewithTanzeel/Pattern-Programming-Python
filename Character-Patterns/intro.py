# Here are the ASCII codes for digits, uppercase alphabets, and lowercase alphabets:

# ### Digits (0–9):
# | Character | ASCII Code |
# |-----------|------------|
# | 0         | 48         |
# | 1         | 49         |
# | 2         | 50         |
# | 3         | 51         |
# | 4         | 52         |
# | 5         | 53         |
# | 6         | 54         |
# | 7         | 55         |
# | 8         | 56         |
# | 9         | 57         |

# ---

# ### Uppercase Alphabets (A–Z):
# | Character | ASCII Code |
# |-----------|------------|
# | A         | 65         |
# | B         | 66         |
# | C         | 67         |
# | D         | 68         |
# | E         | 69         |
# | F         | 70         |
# | G         | 71         |
# | H         | 72         |
# | I         | 73         |
# | J         | 74         |
# | K         | 75         |
# | L         | 76         |
# | M         | 77         |
# | N         | 78         |
# | O         | 79         |
# | P         | 80         |
# | Q         | 81         |
# | R         | 82         |
# | S         | 83         |
# | T         | 84         |
# | U         | 85         |
# | V         | 86         |
# | W         | 87         |
# | X         | 88         |
# | Y         | 89         |
# | Z         | 90         |

# ---

# ### Lowercase Alphabets (a–z):
# | Character | ASCII Code |
# |-----------|------------|
# | a         | 97         |
# | b         | 98         |
# | c         | 99         |
# | d         | 100        |
# | e         | 101        |
# | f         | 102        |
# | g         | 103        |
# | h         | 104        |
# | i         | 105        |
# | j         | 106        |
# | k         | 107        |
# | l         | 108        |
# | m         | 109        |
# | n         | 110        |
# | o         | 111        |
# | p         | 112        |
# | q         | 113        |
# | r         | 114        |
# | s         | 115        |
# | t         | 116        |
# | u         | 117        |
# | v         | 118        |
# | w         | 119        |
# | x         | 120        |
# | y         | 121        |
# | z         | 122        | 


# SINGLE CHARACTER PATTERN 
n = 5
for i in range(n):
    for j in range(i+1):
        print("A",end=' ')
    print()

#ouput
# A 
# A A
# A A A
# A A A A
# A A A A A
# Character increment Pattern
n = 5
p = 65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()

#Output
# A
# B B
# C C C
# D D D D
# E E E E E

# Same code different output 
n = 5
p = 65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
        p+=1
    print()
#Output
# A
# B C
# D E F
# G H I J
# K L M N O

