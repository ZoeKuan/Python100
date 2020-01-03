# Author: Kuan time:1/21/2019
# Question 2
# Level 1
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def fact():
    a=int(input("give a number:"))
    d=1
    for i in range(1,a+1):
        d=d*i
    print(i,d)
fact()

# Solution:
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
# x=int(raw_input())
# print fact(x)

# def fact(x):
#     if x==0:
#         return 1
#     return x*fact(x-1)
#
# x=int(input('input:'))
# print(fact(x))
