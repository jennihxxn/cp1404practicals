"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode for sales bonus

GET sales from user
WHILE sales is greater than or equal to 0
    IF sales less than 1000
        calculate bonus as 10% of sales
    ELSE
        calculate bonus as 15% of sales
    PRINT calculated bonus
    GET sales from user again
PRINT "Do next thing."
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
   if sales < 1000:
       bonus = sales * 0.1
   else:
       bonus = sales * 0.15
   print(f"Bonus: ${bonus:.2f}")

   sales = float(input("Enter sales: $"))

print("Do next thing.")