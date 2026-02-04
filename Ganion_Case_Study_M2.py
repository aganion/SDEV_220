"""
Alicia Ganion
M2 Case Study
This program tests if a student has made the honor roll or Dean's List. I've also added a third option
because it felt sad to just end the program and say nothing to the student if they made neither.
"""

user_last_name = input('Enter your last name or "ZZZ" to quit: ')
if user_last_name != 'ZZZ':
    user_first_name = input('Enter your first name: ')
    user_GPA = float(input('Enter your GPA: '))
else:
    print('End Program.')

if user_GPA > 3.5:
    print(f"{user_first_name} {user_last_name} has made the Dean's List")
elif user_GPA > 3.2:
    print(f"{user_first_name} {user_last_name} has made the Honor Roll.")
else:
    print(f"{user_first_name} {user_last_name} has a GPA of {user_GPA}.")