# comparison operators
# The result of the comparison operation is always true or false.
# ==      :   {equal to}
#             True if the same, False if different

# !=      :   {not equal}
#             true if different, false if staticmethod

# <       :   {less than}
#             true if the right side is larger

# >       :   {greater than}

# <=      :   [equal to]

# >=      :   [greater than or equal to]    

# print(5 != 2)
# print(5<2)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# if(condition) :
#     Run if the abovecondition is true.
# elif(condition) :
#     run elif the above condition is true.
# else:
#     run if all condition are false.

# if  :always use 1
# elif:use range 0-infinity
# else:use 0 or 1
# if can be used by nesting within if.

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 100-90 :A
# 89-70:B
# 69-60:C
# 59-:D

# score=int(input())

# if(100>= score >= 90) :
#     print ('A')
# elif(89>= score >= 70) :
#     print:('B')
# elif(69>= score >=60) :
#     print('C')
# elif(59>= score >= 0) :
#     print('D')

# print("End")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# age=int(input("Enter your age : "))

# if(11 >= age >= 0) :
#     print("sorry, only over 12 years can watch this movie")

# if(12 <= age) :     # if its infinite
#     print("Good, have fun watching.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# not     :if true, the result is reserved to false. If it is false, the result id reserved to true.
# and     :True if both sides are true, false if one side is false.
# or      : false if both sides are false, true if at least one side is true.
# the execution order is executed in the order of not, and, or.

# print(not(1 ==1))
# print((1 !=5) and (10 <= 15))
# print((6 !=6) or (5 == 3))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# nested if 
# if can be nested

# age= int(input("enter your age:"))
# is_member = input("are you a member? (yes or no):")

# if(age >= 18) :
#     if(is_member == "yes") :
#         print("welcome, adult member!")
#     else:
#         print("adult non- member, please sign up.")
# else:
#     if(is_member == 'yes') :
#         print("welcome, young member!")
#     else:
#         print("young non member, please sign up.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print("Enter 2 numbers")
numbers1=int(input())
numbers2=int(input())

print("what calculation do you want to run?")
print("1:multiply 2:divide 3:add 4:subtract")
calculation=int(input())
if(calculation==1) :
    print("selected multiply",numbers1,"*",numbers2,"=",numbers1*numbers2)
elif(calculation==2) :
    print("selected divide",numbers1,"/",numbers2,"=",numbers1//numbers2)
elif(calculation==3) :
    print("selected add",numbers1,"+",numbers2,"=",numbers1+numbers2)
elif(calculation==4) :
    print("selected subtrat",numbers1,"-",numbers2,"=",numbers1-numbers2)
    
    