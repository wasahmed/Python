# print ('#' * 10)#expression
#######types#######
# price = 10#int
# rating = 4.9 #float
# name = 'string'
# is_valid = True#boolean

########getting input########
# name = raw_input('whatsup ')
# print (name)
#if you use input() than use quotes

# dob = raw_input("birth year: ")
# age = 2020 - int(dob);
# print (age)
# print (type(age))

# pounds = raw_input("Enter lbs: ")
# kilograms = int(pounds) * 0.453592
# print (kilograms)

#######Strings######
# course = "python's course"
# print (course)
# email = '''
#     this is a
#     multiple line
#     string
#
#     cool
# '''
# print (email)
# print (course[0])
# print (course[-1])#last character
# print (course[0:3])
# copy = course[:]
# print (copy)
# print (course[0:-1])

#######Formated Strings############
# first = 'john'
# last = 'smith'
# message = f'{first} [{last}] is a dev'#python 3
# print (message)

#######String Methods#############
# str = "hello world"
# print (len(str))# len is general purpose
# print (str.capitalize())
# print (str.upper())
# print (str)# notice that str is not modified
# print (str.find('lo'))
# print (str.replace('o', 'a'))
# print ('hello' in str)

########Arithmetic Operations#############
#int and floats
# print (10 / 3)
# print (10 % 3)
# print (10 ** 3)
# x = 10
# x+=3
# print (x)
#remember about operator precedence ()exp/mult/div/add/sub

# import math
#
# print (math.ceil(3.6))
# print (math.floor(3.6))
# x = -2.9
# print (round(x))
# print (abs(x))

############if statements##################
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print ("its a hot day")
#     print ('drink water')
# elif is_cold:
#     print ("cold day")
#     print "dress warm"
# else:
#     print "lovely day"
# print ("enjoy")

##########Logical operators##############
# has_high_income = True
# has_good_credit = False
#
# if has_good_credit or has_high_income:
#     print ("eligible for load")
# #AND/OR/NOT

#######Comparison Operators#############
# name = raw_input()
# if len(name) < 3:
#     print "too short"
# elif len(name) > 10:
#     print "too long"
# elif len(name) == 5:
#     print "perfect"
# else:
#     print name

#######while loops######
# while condition:
#       exec
#       increment
# i = 1
# while i <= 3:
#     answer = raw_input("Guess ")
#     if int(answer) == 9:
#         print "correct"
#         break
#     i = i + 1
# else:
#     print "thank you for playing"

# command = ""
# started = False
# while True:
#     command = raw_input("> ").lower()
#     if command == "start":
#         if started == True:
#             print "Car already started"
#         else:
#             started = True
#             print ("Car Started")
#     elif command == "stop":
#         if not started:
#             print ("Car already stopped")
#         else:
#             print ("stopped")
#             started = False
#     elif command == "help":
#         print '''start - to start car
#         stop - to stop car
#         quit - to exit'''
#     elif command == "quit":
#         break
#     else:
#         print "illegal command"
# print "thank you"

#############For Loops################
# for loopvar in obj
# for item in 'Python':
    # print (item)
# for item in ['john', 'snow', 'smith']: #list // could be a list of number (range)
#     print (item)
# prices = [10, 20, 30]#shopping cart items
# total = 0
# for item in prices:
#     total = total + item
# print (total)


#########Nested loops################
#co-ordinates
# for x in range(4):
#     for y in range(3):
#         print (x,y)

#F
# numbers = [5,2,5,2,2]
# for number in numbers:
#     print ("x" * number)

##############Lists##################
# names = ['A', 'B', 'C', 'D']
# print names
# print names[-2]
# print names[2:3] # original list is not modified

# numbers = [2, 6, 9, 12, 15, 18]
# highest = numbers[0]
# for loop

########2D Lists#####################
#matrix
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print (matrix[0][1])
# print matrix
# #good place to use nested loops

###########List methods#############
# numbers = [5, 2, 1, 7, 4]
# numbers.append(20)
# numbers.insert(0,1)
# print numbers
# numbers.remove(5)
# #clear
# numbers.pop()
# numbers.index(2)
# print (50 in numbers)#safer
# numbers.count(5)
# numbers.sort()
# print numbers
# newlist = numbers.copy()

#romove duplicates
# numbers = [2,2,3,3,6,6,5,5]
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print (unique)

##########Tuples##############
#immutable
# numbers = (1, 2, 3)
# numbers[0] = 4

#########Unpacking##############
# coordinates = (1,2,3)
# x,y,z = coordinates#unpacks
# print x
# print y
# print z


#########Dictionaries###########
#key value pairs
# customer = {
#     "name": "john smith",
#     "age" : 30,
#     "is_verified": True
# }
# print customer.get("address", "xyz")
# customer["adress"] = "x"
# print customer

# phonenumber = raw_input("phone: ")
# digits = {
#     "1": "one",
#     "2": "two"
# }
# output = ""
# for digit in phonenumber:
#     output += ' ' + digits.get(digit, "!")
# print output

# message = raw_input(">")
# wordslist = message.split(' ')
# emojis = {
#
# } try on mac

############Functions#######################
#maintainable small chunks
#print()
#input()
# def greet_user(name):
#     print ("hello " + name)
#     print ("welcome")
# greet_user("user")
# #could use keyword arguments instead of positional arguments
#
# def square(number):
#     return number * number
# print square(3)
#no return statement will by default return none

#############Exceptions################
# try:
#     age = int(raw_input('Age: '))#raise exception
#     income = 20000
#     risk = income/age
#     print age
# except ZeroDivisionError:
#     print ("age can not be zero")
# except ValueError:#catch the exception
#     print ("invalid value")


#############Classes#########################
#used to define new types
#eg shopping car
class Point:
    def move(self):
        print ("move")
    def draw(self):
        print ("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print (point1.x)
point2 = Point()
print (point2.x)