# Dagger Allocca
# 09/11/2024
# P2LAB2
# Use a dictionary to store and use user information

# Create the dictionary
cars = {'Camaro':18.21,'Prius':52.36,'Model S':110,'Silverado':26}

# Get all keys from dictionary
keys = cars.keys()

# Print all keys
print(keys)

print()

# Get user input and assign to variable, and tell the user the mpg
user_car = input('Enter a vehicle to see its MPG: ')
print('The',user_car,'gets',cars[user_car],'MPG.')

print()

# Get more user input to do some math with
miles = int(input('How many miles will you drive the ' + user_car + '? '))
gallons = miles / cars[user_car]

print()

print(round(gallons,2),'gallon(s) of gas are needed to drive the',user_car,
miles,'miles.')