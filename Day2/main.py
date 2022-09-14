# import cmath
# print(3*(3+3)/3-3)

#BMI Calculator
# height = float(input('Enter your height in m: '))
# weight = float(input('Enter your weight in kg: '))
# bmi = "{:.2f}".format((weight/height**2))
# print(f'Your BMI is {bmi}')

# Day 2 Project: Tip Calculator
print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
percentage_tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
number_of_people = int(input('How many people will split the bill? '))
tip = (total_bill/number_of_people)*percentage_tip/100
total_per_person = round((total_bill / number_of_people) + tip, 2)
print(f"Each person should pay: ${total_per_person}")

