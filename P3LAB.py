# Alana Allocca
# 09/18/2024
# P3LAB
# Calculate coins needed for change

# Floor division // gives back the whole number from division

# Modulus % gives you back the remainder from division
#----------------------------------------------------------------------
# Get amount of money

amount = float(input('Enter the amount of money as a float: '))
print(amount)

#convert value to an integer. last 2 digits are still change
int_amount = int(amount * 100)
print(int_amount)
