#1.	Write a Python Program to find sum of array?

import logging as lg
import sys
lg.basicConfig(filename='assignments.log',level='DEBUG',format='%(levelname)s %(asctime)s %(name)s %(message)s')
lg1=lg.getLogger("ass7_1")
def array_sum(l):
    try:
        return sum(l)
    except Exception as e:
        lg1("error occured at line number",sys.exc_info()[2].tb_lineno)
        lg1.exception(e)
l=[2,3,4,5]
lg1.info(f"The sum of the array is:{array_sum(l)}")

#2.	Write a Python Program to find largest element in an array?
lg2=lg.getLogger("ass7_2")
def largest_ele(l):
    try:
        return max(l)
    except Exception as e:
        lg2.info(f"Error occured at linenumber :{sys.exc_info()[2].tb_lineno}")
        lg2.exception(e)
lg2.info(f"The largest element if an array is :{largest_ele(l)}")


#3.	Write a Python Program for array rotation?
import logging as lg
import sys
lg.basicConfig(filename='assignments.log',level='DEBUG',format='%(levelname)s %(asctime)s %(name)s %(message)s')
lg3=lg.getLogger("ass7_3")


class not_array():
    pass


def array_rotation(l,n,typ):
    '''This function will rotate the array left or right . The left rotate will remove the elements from the front and place it in the back.
    The right rotate will remove the elements from the end and add the elements to the beginning.
    '''
    try:
        if type(l)!=list:
            raise not_array("The given input is not an array")
        else:
            lg3.info(f"The given input array is:{l}")
        if typ=='left':
            temp=[]
            for i in range(n):
                temp.append(l.pop(0))
            l.extend(temp)
        elif typ=='right':
            temp=[]
            for i in range(n):
                temp1=(l.pop(-1))
                l.insert(0,temp1)
        lg3.info(f"The array after {typ} rotation is :{l}")
        return l
    except not_array as e:
        lg3.error(e)
    except Exception as e:
        lg3.info("Error occurred in the line number: ",sys.exc_info()[2].tb_lineno)
        lg3.exception(e)


array_rotation([1,2,3,4,5],3,'left')

#4.	Write a Python Program to Split the array and add the first part to the end?
import logging as lg
import sys
lg.basicConfig(filename='assignments.log',level='DEBUG',format='%(levelname)s %(asctime)s %(name)s %(message)s')
lg4=lg.getLogger("ass7_4")


def split_array(n,k):
    lg4.info(f"The input array is : {n}, and the position from which it has to be split is {k}")
    try:
        l1=len(n)
        b=n[k::1]

        a=b+n[:k]

        return a
    except Exception as e:
        lg4.exception(e)

lg4.info(f"The final array is : {split_array([1,2,4,5,6,7],3)}")


# 5.	Write a Python Program to check if given array is Monotonic?

import logging as lg
import sys

lg.basicConfig(filename='assignments.log',level='DEBUG',format='%(levelname)s %(asctime)s %(name)s %(message)s')
lg5=lg.getLogger("ass7_5")
def monotonic(l):
    try:
        start=l[0]<l[1]

        for i in range(len(l)-1):

            if (l[i]<l[i+1])==start:


                continue
            else:

                return "The given Array is not monotonic"

        return "The given array is monotonic"

    except Exception as e:
        lg5.info(f"Error occurred in line number:{sys.exc_info()[2].tb_lineno}")
        lg5.error(e)

lg5.info(monotonic([1,2,6,4,5]))

