# Dagger Allocca
# 09/09/2024
# P1HW2
# Travel expenses calculator

print('This program calculates and displays travel expenses')

print('')

budget = int(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas? '))
accomodation = int(input('Approximately, how much do you think you will need for accomodation/hotel? '))
food = int(input('Last, how much do you need for food? '))

print('')

print('-----Travel Expenses-----')
print('Location:',destination)
print('Initial Budget:',budget)

print('')

print('Fuel:',gas)
print('Accomodation:',accomodation)
print('Food:',food)

print('')

total = gas + accomodation + food
balance = budget - total
print('Remaining Balance:',balance)


