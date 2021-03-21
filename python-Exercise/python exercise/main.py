import random
# print("anas")
#############################################
# frutes=["anas","omar","oday"]
# x,y,z = frutes
# print("my name is "+ x)
# print(y)
##############################################
# x = "awesome"
# def myfunc():
#   print("Python is " + x)
# myfunc()
#################################################
# x="ali"
# def test():
#     print("test for "+ x)
#
# test()
#################################################
# x=1.2
# print(type(x))
# b=int(x)
# print(b)

#print(random.randrange(1, 10))
################################################
# txt = "The best things in life are free!"
# print("best" not in txt)
###################################################
# b = "Hello, World!"
# print(b[:5])
#########################################################3
#b = "Hello, World!"
#print(b[-5:-1])

####################################################
# n = 20
# check = {True: "Not Weird", False: "Weird"}
#
# print(check[
#         n%2==0 and (
#             n in range(2,6) or
#             n > 20)
#     ])
######################################################
# x=30
# test ={True: "anas", False:"omer"}
# print(test[
#      x==20 or x==50
#       ])
###################################################
# i = 1
# while i < 4:
#     print(i, end=" ")
#     i += 1
#######################################################3
# string="anas"
# print(string.upper())
# print(string.lower())
# x = string.count("a")
# y=string.find("a")
# print(y)
# print(x)
########################################################################
# mystring = "Meet Guru99 Tutorials Site.Best site for Python Tutorials!"
# print("The position of Tutorials is at:",
# mystring.find("Tutorials"))
#################################################################
# from datetime import datetime
# name = input('What is your name? \n')
# age = int(input('Enter your age? \n'))
# country =(input('enter your country?\n'))
# hundred = int((100-age) + datetime.now().year)
# print ('Hello %s. You are %s years old. You will turn 100 years old in %s, and you are from %s' % (name, age, hundred,country))


###############################################
# name = input('What is your name? \n')
# print('the text is %s'%(name))
# x1 = name.count("a")
# x2 = name.count("o")
# x3 = name.count("u")
# x4 = name.count("i")
# x5 = name.count("e")
# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
###################################################################

# fname = input('What is your first name? \n')
# lname = input('What is your last name? \n')
#
# firstCharacter = fname[:1].upper()
# lastCharacter = lname[:1].upper()
# print('Hello %s.%s' % (firstCharacter, lastCharacter))
# #print (firstCharacter)
#########################################################################

# string="Allosaurus"
# x1=string[:4]
# x2=string[3:7]
# x3=string[-4:]
# x4=string[2:-1]
# x5=string[-2:]
# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
#############################################################################

# string = len("anas")
# print(string)
####################################################

# my_var = "dark knight"
# print(my_var.title())
#############################################################
# string = "anas melhem"
# print(string.find(" "))
# print(" " in string)
# print("a" in string)
###########################################################
#
# # initializing bad_chars_list
# bad_chars = ["x"]
#
# # initializing test string
# test_string = "Attack on Titan is axxxxxxxxxxxxxJapanese manga series written and illustrated by Hajime" \
#               " Isayama. It is set in a world where humanity lives inside cities surrounded byx" \
#               "xxxxxxxxxxxxxx enormous walls that protect them from gigantic man-eating humanoids r" \
#               "eferred to as Titans; the xxxxxxxxxxxxxxxstory follows Eren Yeager, who vows to exte" \
#               "rminate the Titans after a Titan brings about the destruction of his hometown and the de" \
#               "ath of hisxxxxxxxxxxxxxxxx mother. Attack on Titan has beenxxxxxxxxxxxxxxxxxxx serialized" \
#               " in Kodansha's monthly Bessatsu Shōnen Magazine since September 2009xxxxxxxxxxxxxxxxxx" \
#               " and collected into 33 tankōbon volumes as of January 2021."
#
# # printing original string
# print("Original String : " + test_string)
#
# # using replace() to
# # remove bad_chars
# for i in bad_chars:
#     test_string = test_string.replace(i, '')
#
# # printing resultant string
# print("Resultant list is : " + str(test_string))
########################################################################################
#
# fname = input('What is your first name? \n')
# lname = input('What is your last name? \n')
#
# firstCharacter = fname[:1].upper()
# lastCharacter = lname[:1].upper()
 #print( '%s %s,Hello [%s.%s]' % (fname,lname,firstCharacter, lastCharacter))
##############################################################################
# string = input('Enter the string? \n')
# x = len(string)
#
#
# def f1():
#     x = 2
#     print(string*2)
#
#
# first = string[0:2]
# last = string[-2:]
#
# print('%s%s' % (first,last))
# #print(x)
# # f1()
##########################################################


# def remove_char(char, n):
#     first = char[:n]
#     last = char[n + 1:]
#     return first + last
#
#
# print(remove_char('Python', 0))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))
###########################################################3

# cow = input('Enter number of cow ? \n')
# pigs = input('Enter number of pigs ? \n')
# horses = input('Enter number of horses ? \n')
# goats = input('Enter number of  goats ? \n')
# dogs = input('Enter number of dogs ? \n')
#
# print(' cow is %s \n pigs is %s \n horses is %s \n goats is %s \n dogs is %s \n ' % (cow, pigs, horses, goats, dogs))
######################################################################################################################################

# def odd_indices(lst):
#     return [lst[i] for i in range(len(lst)) if i % 2 != 0]
#
#
# print(odd_indices([4, 3, 7, 10, 11, -2]))
##################################################################3
# # Python Program to Reverse String
# string = input("Please enter your own String : ")
#
# string2 = ''
#
# for i in string:
#     string2 = i + string2
#
# print("\nThe Original String = ", string)
# print("The Reversed String = ", string2)
#############################################################
# txt = "Hello World"[::-1]
# print(txt)
####################################################################################