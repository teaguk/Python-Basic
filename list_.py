# list_eng.py

# variable=["value", value]       => The data type of the value does not matter
# Use in the above form
# list is a collection of data types in order in one variable
# the order of values start from 0 => it is called the index number
# when bringing in the list values, refer to themusing []

# list1=[1, 'cit', True]
# print(list1)
# print(list1[0])     #get list1 index number 0 value
# print(list1[2])
# print(list1[3])      # get index number 3 value. there is index number 3, so an error occures.



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#you can see the index number to modify the value at the index number
#changing the value can be done as if saying the value in a variable
# a=[1, 'cit', True]
# print(a)

# a[1]="hello" #change the value of the index number 1 of a 
# print(a)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# list1=["abc","dfg","hij",123,456 ]
# print(list1)
# print()

# print("Q1. change the first element of list1 to'park'.")
# list1[1] = 'park'
# print(list1)
# print()

# print("Q2. Name the variable'arr' and save the list below.[4,8,12,16,20,24,28,32]")
# arr=[4,8,12,16,20,24,28,32]
# print(arr)
# print()

# print("Q3.change the 4th element of arr to 'cit'")
# arr[1]='cit'
# print(arr)
# print()

# print("Q4. run print(list1)and print(arr)")
# print(arr)
# print(list1)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

for i in range(1, 9, 2):
        print(i)
print()

list1 = [1, 3, 5, 7]
for i in list1:             #can insert a list variable instead of range() in the loop
        print(i)            #get the elements of a list one by one
print()

list2=['a', 'hello','cit', 'coding','A']
for j in list2:
        print(j)
print()