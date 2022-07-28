# q1 1.	Write a Python Program to Add Two Matrices?
import logging as lg
import sys

m1=[[1,2,3],[3,4,5],[2,3,4]]
m2=[[2,3,4],[5,6,7],[8,9,0]]
lg.basicConfig(filename='assignments.log',level='DEBUG',format='%(name)s %(asctime)s %(levelname)s %(message)s')
lg1 = lg.getLogger("lg1.ass_8")
class Matrix_addtion_notpossible(Exception):
    pass
def matrix_addition(m1,m2):
    lst=[]
    try:
        if len(m1)==len(m2):
            #print(m1[2][2])
            for i in range(len(m1)):
                ls1=m1[i]
                ls2=m2[i]
                lst1=[]
                if len(ls1)==len(ls2):
                    for j in range(len(ls1)):
                        lst1.append(m1[i][j] + m2[i][j])
                    lst.append(lst1)


                else:
                    raise Matrix_addtion_notpossible("Matrix addition not possible as there is a size mismatch between the matrices")
        else:
            raise Matrix_addtion_notpossible("Matrix addition not possible as there is a size mismatch between the matrices")
    except Matrix_addtion_notpossible as e:
        lg1.error(sys.exc_info())
        lg1.info("Error occured at line number",sys.exc_info()[2].tb_lineno)
    except Exception as e:
        lg1.exception(sys.exc_info())
    #lg1.info("Error occured at line number")
    return lst

lg1.info(f"The sum of matrix addition is: %s" ,matrix_addition(m1,m2))

print("********************************************************************************")

#Q2 2.	Write a Python Program to Multiply Two Matrices?

import logging as lg
import sys

lg.basicConfig(filename="assignments.log",level='DEBUG',format='%(name)s %(asctime)s %(levelname)s %(message)s')
lg1=lg.getLogger("ass8_q2")
m1=[[1,2,3],[3,4,5],[2,3,4]]
m2=[[2,3,4],[5,6,7],[8,9,0]]


class matrix_mul_not(Exception):
    pass


def matrix_multiplication(m1,m2):
    try:
        lg1.info("This function will perform matrix multiplication")
        m1_l=len(m1)
        m1_w=len(m1[0])
        for i in m1:
            if len(i)==m1_w:
                pass
            else:
                raise matrix_mul_not("Matrix multiplication is not possible as it is not a matrix")

        m2_l=len(m2)
        m2_w=len(m2[0])
        for i in m2:
            if len(i)==m2_w:
                pass
            else:
                raise matrix_mul_not("Matrix multiplication is not possible as it is not a matrix")
        lst=[]
        for i in range(m2_l):

            lst1=[]
            for j in range(m2_w):
                sum = 0

                for k in range(m2_l):
                    sum+=m1[i][k]*m2[k][j]
                lst1.append(sum)
            lst.append(lst1)

        #   print("The result of matrix multiplication is:",lst)
        return lst
    except matrix_mul_not as e:
        lg1.error(e)

    except Exception as e:
        lg1.info(f'Error occured at line{sys.exc_info()[2].tb_lineno}')
        lg1.exception(e)

lg1.info(f"The result of matrix multiplication is: {matrix_multiplication(m1,m2)}")


#3.	Write a Python Program to Transpose a Matrix?

import logging as lg
import sys

lg.basicConfig(filename="assignments.log",level='DEBUG',format='%(name)s %(asctime)s %(levelname)s %(message)s')
lg3=lg.getLogger("ass8_q3")
m1=[[1,2,3],[3,4,5],[2,3,4]]



class is_not_matrix(Exception):
    pass


def matrix_transpose(m1):
    try:
        lg3.info("This function will transpose of a matrix")
        m1_l=len(m1)
        m1_w=len(m1[0])
        for i in m1:
            if len(i)==m1_w:
                pass
            else:
                raise is_not_matrix("The given list of list is not a matrix")
        m2_t=[]
        for i in range(m1_l):
            lst=[0 for j in range(m1_w)]
            m2_t.append(lst)


        for i in range(m1_l):
            for j in range(m1_w):
                m2_t[j][i]=m1[i][j]

        return m2_t
    except is_not_matrix as e:
        lg3.error(e)
    except Exception as e:
        lg3.info(f"An error occured at line number:{sys.exc_info()[2].tb_lineno}")
        lg3.exception(e)

lg3.info(f"The transpose of the input matrix is :{matrix_transpose(m1)}")

print("************************************************************")

#4 	Write a Python Program to Sort Words in Alphabetic Order?

import logging as lg
import sys

lg.basicConfig(filename="assignments.log",level='DEBUG',format='%(name)s %(asctime)s %(levelname)s %(message)s')
lg4=lg.getLogger("ass8_q4")

def str_sort():
    try:
        inp1 = input("enter the elements seperated by space")

        lst1 = inp1.split(" ")

        lst1.sort()
        return lst1
    except Exception as e:
        lg4.info(f"Error occurred at line:{sys.exc_info()[2].tb_lineno}")
        lg4.exception(e)

lg4.info(f"Sorted words in list is :{str_sort()}")



#5.	Write a Python Program to Remove Punctuation From a String?

import logging as lg
import sys
import re
lg.basicConfig(filename="assignments.log",level='DEBUG',format='%(name)s %(asctime)s %(levelname)s %(message)s')
lg5=lg.getLogger("ass8_q5")

def remove_punc():
    try:
        inp1 = input("enter the string")
        lg5.info("This is to remove the punctuation in the string")
        lg5.info(f"The input string is :{inp1}")
        out=re.sub(r'[^\w\s]',"",inp1)
        return out
    except Exception as e:
        lg5.info(f"Error occurred at line:{sys.exc_info()[2].tb_lineno}")
        lg5.exception(e)

lg5.info(f"The string after removing punctuation is:{remove_punc()}")


