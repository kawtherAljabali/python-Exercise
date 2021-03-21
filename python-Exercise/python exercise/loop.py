# for i in range(1500,2701):
#     if (i%7==0 and i%5==0):
#         print(i)
##################################
# n=5
# m=10
# for i in range (1,6):
#     print("*"*i)
# for i in range(6,10):
#     print("*" * (m-i))
#######################################
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# #print(numbers)
# odd=0
# even=0
# for i in numbers:
#
#     if i % 2 == 0:
#         even+=1
#
#     else:
#         odd+=1
#
# print(odd)
# print(even)
###########################################3
# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x)
#################################################33

# n=1
# x=1
# x*n=x*n+x*(n-1)
# print(x*n)
# n+=1
###################################
# def fibo(num):
# a,b = 0, 1
# for i in xrange(0, num):
# yield "{}:: {}".format(i + 1,a)
# a,b = b, a + b
# for item in fibo(10):
# print item
#####################################
# str = "Python 3.2"
# d=l=k=0
# for i in str:
#     if i.isdigit():
#         d=d+1
#     elif i.isalpha():
#         l=l+1
#     else:
#         k=k+1
#
# print("Letters", l)
# print("Digits", d)
# print("else", k)
##################################
# str = "Python 3.2"
# d=l=k=0
# for i in str:
#     d=d+1
# else:
#     l=l+1
# print("Letters", d)
# print("Digits", l)
#####################################3
# import re
#
# password = input("Input your password: ")
# x = True
# while x:
#     if (len(password) < 6 or len(password) > 12):
#         break
#     elif not re.search("[a-z]", password):
#         break
#     elif not re.search("[0-9]", password):
#         break
#     elif not re.search("[A-Z]", password):
#         break
#     elif not re.search("[$#@]", password):
#         break
#     elif re.search("\s", password):
#         break
#     else:
#         print("Valid Password")
#         x = False
#         break
#
# if x:
#     print("Not a Valid Password")
###################################################
