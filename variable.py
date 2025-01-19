# variable
# variable=value
# save the value in variable in the format above.
# = Unlike the meaning of the symbol, the value is simply stored in a variable
# Variable can be whatever as long as you follow the rules below
# 1. Impossible to start with a number
# 2. special characters are not possible exept the symbol"_"
# 3. no spacing
# 4. reserved words not possible

# my_name = "eugenia"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# data types
# str   -> String     => made up of quotes" "  ' '
# float -> float      => no quotes and has a decimal point 
# int    ->integer    =>no quotes and has no decmal point 
# everyday words (english, chinese, korean, etc) without quotes => error 
# a=10    # saves the integer 10 in the variable a
# b='cit'     # saves the string 'cit' in the variable b


# name='python'
# age=20
# height=178

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# print('text' or variable or number)
# the print() function prints the 'text', number, or value of
# the variable inside the bracket and then adds a newline.
# to print multiple items, use a comma (,)
# if you use print () with nothing inside, it prints an empty line

# name='python'
# age=10
# height=140
# print (name)
# print ()        #prints an empty line
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# input('text'or value or variable)
# displys 'text' or the value of the variable, then waits for the keyboard input until enter is pressed
#     'text'or or variable can be left out
# variable= input ('text' or variable)
# usually used in this format, without variable it the input value is not saved
# input() always saves the value as a str data type

# var1 = 2
# var2 = input("insert anything:")
# print(var2)
# print(type(var2))

# var2=int(var2)
# print(type(var2))

# sum=var1+var2
# print(sum)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# type casting 
# str(variable or value )  => converts variable or value to str data type
# float(variable or value) => converts variable or value to float data type
# int(variable or value) => converts variable or value to int data type
# just using them in calculations doesn't change the original variable's data type
# to change the original variable's data type, save it back into the variable [ex. a =int(a)]

# var1=2
# var2='31'
# result=var1+int(var2)
# print(result)
# print(type(var2))
# var2=int(var2)
# print(type(var2))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


print("hello.enter your name")
name=input()
print("welcome" ,name, "enter your age")
age=input()
result= 2025-int(age)
print("you were born in",result,"enter your height")
height=int(input())

two_m=200-height
print("there are", two_m,"cm left until 2m")