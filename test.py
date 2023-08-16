from helper import *


#x="Bhakti"
#y= 50
z = 3.4
#print(x)
#print("Hello"+x)
#print("It is "+ str(y))
print(f"It is {z}")
print(f"calculate addition between 34 and 69 is {34+69}")

"""def calculation(a,b):
    print(f"addition between {a} and {b} is {a+b}")
    datatype_check_a= a>0  #while True:
    print(type(datatype_check_a))
    if a>b:
        print(f"subtraction between {a} and {b} is {a-b}")
    else:
        print("wrong values")
   # print(c)
    return f"multiplication of {a} and {b} is {a*b}" """""

try:
    new_value1 = ""
    while new_value1 != "exit":
        value1= input("enter value of a:")
        new_value1=int(value1)
        value2= input("enter value of b:")
#new_value2=int(value2)

#while new_value1 != "exit":
       # for new_a,new_b in new_value1,value2.split(","):
        answer=helper.calculation(new_value1,int(value2))
        print(answer)

        dictionary_value = {"value_a":value1[0],"value_b":value2[1]}
        print(dictionary_value)

except ValueError:
    print("exit code !")
#print(value1)
    #input(35,12,"Looks Good!")

#calculation(35,12,"Looks Good!")
