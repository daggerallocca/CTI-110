# Dagger Allocca
# 09/09/2024
# P1HW2
# Format travel expenses calculator

print('This program calculates and displays travel expenses')

print('')

budget = float(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = float(input('How much do you think you will spend on gas? '))
accomodation = float(input('Approximately, how much do you think you will need for accomodation/hotel? '))
food = float(input('Last, how much do you need for food? '))

print('')

print('-----Travel Expenses-----')
print('Location:',destination)
print(f"${budget:.2f}")

print('')

print('Fuel:',f"${gas:.2f}")
print('Accomodation:',f"${accomodation:.2f}")
print('Food:',f"${food:.2f}")

print('')

total = gas + accomodation + food
balance = budget - total
print('Remaining Balance:',f"${balance:.2f}")