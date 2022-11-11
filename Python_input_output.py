#Declare  & Assign Variables

int_var = 10
float_var = 18.25
string_var = 'ineuron batch2' # or another way "ineuron batch2"
bool_var = True # if we want to assign false then it should be like false

#function in python for output
#Function does what ? They might or might not accept some parameter
print("Hello world !!!")

#Print variable values in python
print('value of int_var = ',int_var," -Result Done !!")
print('value of float_var = ',float_var, " -Result Done !!")
print('value of string_var = ',string_var, " -Result Done !!")
print('value of bool_var = ',bool_var, " -Result Done !!")

# How to check data type of any variable in python
# We can use type() function
print('type of int_var ?', type(int_var))
print('type of float_var ?', type(float_var))
print('type of string_var ?', type(string_var))
print('type of bool_var ?', type(bool_var))

# How to do the type casting in python ?
# int() , float() , string() , bool()
int_var = int_var + 10 # int_var = 10 + 10 and in next step int_var = 20

casted_int_var = float(int_var)
casted_float_var = int(float_var)

print('Int to float typecasting for int_var = ',casted_int_var)
print('Float to Int typecasting for float_var = ',casted_float_var)

numeric_str = "123"
#numeric_str = int(numeric_str) + 50 # is it valid ?? Numeric_str = '123' + 50

numeric_str = int(numeric_str) + 50 # Numeric_str = int("123") + 50 -> 123=50 = 173
print('value of numeric_str = ', numeric_str)

# How to take the inputs in Python ?
# We can use input() function

# name = input()
# age = input()
# print('User name = ',name)
# print('user age= ',age)

# Python file

# Another way to take user input with custom message
name = input('Enter value for name = ')
age = int(input('Enter value for age = '))
print('User name = ',name)
print('user age = ',age)
