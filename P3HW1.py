# Alana Allocca
# 09/18/2024
# P3HW1
# Use if/else/elif statements with a variable

grades = []
print('-----Enter grades for the following tests-----')

print('')

grades.append(float(input('Enter grade for Module 1: ')))
grades.append(float(input('Enter grade for Module 2: ')))
grades.append(float(input('Enter grade for Module 3: ')))
grades.append(float(input('Enter grade for Module 4: ')))
grades.append(float(input('Enter grade for Module 5: ')))
grades.append(float(input('Enter grade for Module 6: ')))

print('')

average = sum(grades)/len(grades)

print('-------------------Results-------------------')

print(f"Lowest Grade: {min(grades):.2f}")
print(f"Highest Grade: {max(grades):.2f}")
print(f"Sum of Grades: {sum(grades):.2f}")
print(f"Average: {average:.2f}")

# calc. letter grade using if/else/elif

if average >= 90:
    let_grade = "A"
elif average >= 80:
    let_grade = "B"
elif average >= 70:
    let_grade = "C"
elif average >= 60:
    let_grade = "D"
else:
    let_grade = "F"

print('---------------------------------------------')
print('Your grade is:',let_grade)
