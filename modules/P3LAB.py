# Alana Allocca
# 09/18/2024
# P3LAB
# Calculate coins needed for change

# Floor division // gives back the whole number from division

# Modulus % gives you back the remainder from division
#----------------------------------------------------------------------
# Get amount of money from user
change = float(input('Enter an amount of money: $'))

#converting value to an integer
change = int(change * 100)

#determine how much change is needed
dollars = change // 100
change = change - (dollars * 100)

quarters = change // 25
change = change - (quarters * 25)

dimes = change // 10
change = change - (dimes * 10)

nickels = change // 5
change = change - (nickels * 5)

pennies = change

print()

#print the change amounts properly
if dollars > 0:
    if dollars == 1:
        print(f"{dollars} dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print(f"{quarters} quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print(f"{dimes} dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print(f"{nickels} nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print(f"{pennies} penny")
    else:
        print(f"{pennies} pennies")

