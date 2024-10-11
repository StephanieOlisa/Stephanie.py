print('python is active here')

#data types
#number 1 is of type_____
num1 = 47
num2 = -4567
num3 = 40.4
num4 = 3 + 4j

type_of_num1 = type(num1)
type_of_num2 = type(num2)

print (num1,'is of type', type(num1))
print (num2, 'is of type', type(num2))
print (num3, 'is of type', type(num3))
print (num4, 'is of type', type(num4))

int(num3)
to_int = int(num3)

print (type(to_int))

float(num1)
to_float = float(num1)

print (type(to_float))

complex(num2)
to_complex = complex(num2)

print (type(to_complex))

x = 3
print (type(x))

#variables
y = 'mint chocolate chips'
print (type(y))

y = 'chocolate'
Y = 'mint chocolate chips'
print (y)

x,y,z = 'chocolate', 'vanilla', 'money'
print (x)
print (y)
print (z)

x = y = z = 'rocky road'
print (x)
print (y)
print (z)

ice_cream = 'vanilla', 'cupcake', 'chocolate'
x, y, z = ice_cream
print (x)
print (y)
print (z)

x = 'ice_cream is one of my favourite' + '.'
print (x)

y = 5 + 5
print (y)

x = 'ice_cream'
y = ' is'
z = ' one of my favourite.'
print (x + y + z)

x = 1
y = 2
z = 3
print (x + y + z)

x = 'ice_cream'
y = 2
print (x,y)

#data types
# boolean
to_bool = type (1 > 5)
print (to_bool)
x = 1 > 5
print (x)

x = 1 == 1
print (x)

# strings
string = "i've eaten lots of pizza"
print (string)

a = 'welcome to python bootcamp!'
print (a + a)

# list
a = (1, 2, 3)
print (a)

a = ('cookies', 'pancakes', 'strawberry')
print (a)

ice_cream = ('vanilla', 'cake', 'juice')
print (ice_cream)

tuple_scoops = (1,2,3,4,5,2)
print (type (tuple_scoops))

# lists
a = [1,2,3]
print (a)

A = ['cookie', 'sandwich', 'pie']
print (A)
b = ['vanilla', 3, ['scoops', 'spoon'], 'cake']
print (b)

ice_cream = ['strawberry', 'pie', 'cream']
print (ice_cream)


# sets
daily_pints = {1,2,3}
print (type (daily_pints))

daily_print_log = {1,2,3,4,5,13,14,2}
print (daily_print_log)

wife_daily_print_log = {2,4,6,8,29,15,6,8}
print  (wife_daily_print_log)
print (daily_print_log | wife_daily_print_log)
print (daily_print_log & wife_daily_print_log)
print (daily_print_log - wife_daily_print_log)
print (wife_daily_print_log ^ daily_print_log)

# dictionaries
# key/value pair
dict_cream = {'name': 'Lisa Stephanie','weekly intake': 6, 'favourite ice_cream': ['vanilla']}
print (type(dict_cream))
print (dict_cream)
print (dict_cream.values())
print (dict_cream.keys())
print (dict_cream.items())
print (dict_cream['name'])
dict_cream['name'] = 'Lisa Paul'
print (dict_cream)

dict_cream.update ({'name': 'Lisa Stephanie','weekly intake': 10, 'weight': 100})
print (dict_cream)

del dict_cream ['weight']
print (dict_cream)


# ASSIGNMENT
# 1. What is the significance of indentation in Python?
#Indentation in Python is crucial because it defines the structure of the code,
# especially for control flow elements like loops and conditionals.
# Instead of using braces {}, Python uses indentation to group statements together,
# which enhances code readability and reduces errors.
# Improper indentation will lead to syntax errors.

# 2. How do you write a comment in Python?
# using this hashtag (#) is the way to begin a comment

# 3. Python script to print "Welcome to Python Bootcamp!"
a = 'welcome to python bootcamp!'
print (a)

# 4. Program that takes a user's name as input and prints a personalized greeting


# 5. Rules for naming variables in Python:
# Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# The rest of the name can contain letters, numbers, or underscores.
# Variable names are case-sensitive (e.g., age and Age are different).
# Reserved words (like def, class, if) cannot be used as variable names.

# 6. How do you assign multiple values to multiple variables in a single line?
a, b, c = 5, 10, 15
print (a, b, c)

# 7. Declare variables of different types (integer, float, string) and print their values:
#data types
#number 1 is of type integer
num1 = 47
num2 = -4567
num3 = 40.4
num4 = 3 + 4j

Type_of_num1 = type(num1)
Type_of_num2 = type(num2)

print (num1,'is of type', type(num1))
print (num2, 'is of type', type(num2))
print (num3, 'is of type', type(num3))
print (num4, 'is of type', type(num4))

# 9. How do you convert a string to an integer in Python?
int(num3)
to_int = int(num3)

print (type(to_int))

float(num1)
to_float = float(num1)

print (type(to_float))

complex(num2)
to_complex = complex(num2)

print (type(to_complex))

x = 3
print (type(x))

# 8. Program to swap the values of two variables:
k = 'cookies'
print (k)
K = 'mango'
print (K)
# 10. What is the difference between an integer and a float in Python?
# Integer: A whole number without a fractional part, e.g., 5, 100.
# Float: A number that has a decimal or fractional part, e.g., 5.0, 100.75.

# 11. Program to perform basic arithmetic operations on two numbers:
p = 10.5
q = 15.8

print(p + q)
print(p - q)
print(p * q)
print(p / q)


# 12. Program to concatenate two strings and print the result:
A = ['cookie', 'sandwich', 'pie']
print (A)
B = ['vanilla', 3, ['scoops', 'spoon'], 'cake']
print (b)

ice_cream = ['strawberry', 'pie', 'cream']
print (ice_cream)

#Temperature Converter (Celsius to Fahrenheit and vice versa)
celsius = 37

fahrenheit = (celsius * 1.8) + 32

print("%.2f celsius = %.2f fahrenheit" %(celsius, fahrenheit))

# 2. BMI Calculator
height = float(input('enter height in inches:'))
weight = float(input('enter weight in 1bs'))

def BMI(height, weight):
     bmi = weight/(height**2) * 456
     if (bmi < 15):
         return 'severely underweight', bmi

     elif (bmi >= 15 and bmi < 17.5):
         return 'underweight', bmi

     elif (bmi >= 17.5 and bmi < 24):
         return 'healthy', bmi

     elif (bmi >= 25 and bmi < 29):
         return 'overweight'

     elif (bmi >= 30):
         return 'obese', bmi

quote, bmi = BMI(height, weight)
print('your bmi is: {} and you are: {}'.format(bmi, quote))

# 3. Personal Finance Manager
def personal_finance_manager():
    print('Personal Finance Manager')

    # Input income
    income = float(input('Enter your total monthly income:'))

    # Input expenses (multiple categories)
    rent = float(input('Enter your rent expense: '))
    groceries = float(input('Enter your groceries expense: '))
    utilities = float(input('Enter your utilities expense: '))
    transportation = float(input('Enter your transportation expense: '))
    other_expenses = float(input('Enter any other expenses: '))

    # Calculate total expenses and net savings
    total_expenses = rent + groceries + utilities + transportation + other_expenses
    net_savings = income - total_expenses

    # Output the result
    print(f'Your total expenses are: ${total_expenses:.2f}')
    print(f'Your net savings for the month are: ${net_savings:.2f}')

    if net_savings > 0:
        print('You have saved money this month!')
    elif net_savings == 0:
        print('You broke even this month.')
    else:
        print('You have overspent this month.')


# Run the Personal Finance Manager
personal_finance_manager()






