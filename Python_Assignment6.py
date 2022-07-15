# Q1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fib(n):

    if n==1:
        return 1
    elif n==2:
        return fib(n-1)+0
    else:
        return fib(n-1)+fib((n-2))


class NegativenumberError(Exception):
    pass

while True:
    try:
        n= int(input("enter the number of fibonaccci sequence required"))
        if(n<1):
            raise NegativenumberError("please enter number greater than 0")
        lst=[]
        for i in range(1,n+1):
            lst.append(fib(i))
        print(lst)
        break
    except NegativenumberError as e:
        print(e)



#Q2.	Write a Python Program to Find Factorial of Number Using Recursion?

def factorial(n):
    try:

        if n==1:
            return n
        else:
            return n * factorial(n - 1)

    except Exception as e:
        print(e)
print(factorial(5))

# 3.	Write a Python Program to calculate your Body Mass Index?
import logging as lg
lg.basicConfig(filename='test3.log',level=lg.DEBUG,format='%(name)s %(asctime)s %(levelname)s %(message)s')
class NoNegative(Exception):
    pass
def bmi():
    bmi=0
    while True:
        height=float(input("please enter your height in inches"))
        weight=float(input("please enter your weight in pounds"))
        try:
            if height<0 or weight <0:
                raise NoNegative("The height and weight cannot be negative, please enter positive values")
            else:
                bmi=(weight/(height*height))*703
                break
        except NoNegative as e:
            print(e)
    if bmi<18.5:
        lg.INFO("you are underweight")
    elif bmi<20:
        lg.INFO("you are normal")
    elif bmi<30:
        lg.info("you are overweight")
    else:
        lg.info("you are obese")

    return bmi

lg.info("your bmi is: %s",bmi())

# 4.	Write a Python Program to calculate the natural logarithm of any number?

import math
import sys
def logn(n):
    try:
        return math.log(n)
    except ValueError:
        print("we are getting",sys.exc_info()[1],"in line number ",sys.exc_info()[2].tb_lineno)
    except Exception as e:
        print("we are getting",sys.exc_info()[1],"in line number ",sys.exc_info()[2].tb_lineno)


print(logn(32))

#5.	Write a Python Program for cube sum of first n natural numbers?

import logging as lg
import sys
lg.basicConfig(filename='test3.log',level=lg.DEBUG,format='%(name)s %(asctime)s %(levelname)s %(message)s')

def cube(n):
    try:
        sum=0
        for i in range(1,n+1):
            sum+=i**3
        return sum
    except Exception as e:
        lg.info("facing error %s in line number",sys.exc_info()[1],sys.exc_info()[2].tb_lineno)

n=int(input("enter the natural number"))
lg.info("the sum of cube of first %s natural numbers is %s",n,cube(n))
