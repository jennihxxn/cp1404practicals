"""
CP1404/CP5632 - Practical
Broken program to determine score status

Pseudocode for broken score

GET score from user

IF score less than 0 OR greater than 100
    PRINT "Invalid score"
ELSE IF score greater than or equal to 90
    PRINT "Excellent"
ELSE IF score greater than or equal to 50
    PRINT "Passable"
ELSE
    PRINT "Bad"
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
   print("Invalid score")
elif score >= 90:
   print("Excellent")
elif score >= 50:
   print("Passable")
else:
   print("Bad")