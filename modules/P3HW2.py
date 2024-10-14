# Alana Allocca
# 09/18/2024
# P3HW2
# Calculate employee OT pay rate using if/else statements

# Get user info
name = input("Enter employee name: ")
hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee pay rate: "))

# Display employee name
print('-----------------------------------\nEmployee name:',name)

# Determine employee pay
if hours > 40: # Has some OT
    reg_pay_amt = 40 * pay_rate
    ot_pay_rate = 1.5 * pay_rate 
    ot_pay_amt = (hours-40) * ot_pay_rate
    ot_hours = hours-40
else: # No OT
    reg_pay_amt = hours * pay_rate
    ot_hours = 0
    ot_pay_amt = 0

# Calc. gross pay
grosspay = reg_pay_amt + ot_pay_amt

print()

# Display headings
print(f"{'Hours Worked':<18}{'Pay Rate':<14}{'Overtime Hours':<20}{'Overtime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<18}")
print('-' * 100)

# Print out the values
print(f"{hours:<18}${pay_rate:<14.2f}{ot_hours:<20}${ot_pay_amt:<18.2f}${reg_pay_amt:<18.2f}${grosspay:<18.2f}")
