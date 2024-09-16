# Dagger Allocca
# 09/09/2024
# P1HW2
# Travel expenses calculator

print('This program calculates and displays travel expenses')

print('')

budget = (input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = (input('How much do you think you will spend on gas? '))
accomodation = (input('Approximately, how much do you think you will need for accomodation/hotel? '))
food = (input('Last, how much do you need for food? '))

print('')

print('-----Travel Expenses-----')
print('Location:',destination)
print(f'{budget:<10.2} value')

print('')

print('Fuel:',f'${gas:.2f}')
print('Accomodation:',f'${accomodation:.2f}')
print('Food:',f'${food:.2f}')

print('')

total = gas + accomodation + food
balance = budget - total
print('Remaining Balance:',balance)


