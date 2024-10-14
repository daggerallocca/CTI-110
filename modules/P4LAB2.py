# Alana Allocca
# 09/25/2024
# P4LAB2
# Write code that displays information to users using loops.

run_again = ""

while run_again != "no":
    user_num = int(input("Enter an integer: "))
    print()
    if user_num < 0:
        print("This program does not handle negative numbers.")
    else:
        for num in range(12):
            print(f"{user_num} * {num+1} = {user_num * (num+1)}")
    print()
    run_again = input("Would you like to run the program again? ")
    print()

print("Goodbye.")
