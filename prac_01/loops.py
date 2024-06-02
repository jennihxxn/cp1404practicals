"""
Pseudocode for loops

FOR i FROM 1 TO 20 step 2
    PRINT i
END FOR

FOR i FROM 0 TO 100 step 10
    PRINT i
END FOR

FOR i FROM 20 TO 1 step -1
    PRINT i
END FOR

GET "Number of stars: " , STORE IN n

FOR i FROM 1 TO n
    PRINT "*"
END FOR

INPUT "Number of stars: " AND STORE IN n

FOR i FROM 1 TO n
    PRINT "*" REPEATED i TIMES
END FOR
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("Number of stars: "))
for i in range(n):
    print("*", end='')
print()

n = int(input("Number of stars: "))
for i in range(1, n+1):
    print("*" * i)