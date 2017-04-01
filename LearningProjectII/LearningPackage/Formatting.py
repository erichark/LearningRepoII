'''
Created on Apr 1, 2017

@author: Eric
'''



def First_Function(listValues="This is the default value"):
    """This prints someones name"""
    print("Hello " + listValues)
    
First_Function()
print(First_Function.__doc__)

a=10
b=5

def Math_Function(a,b,c=1,d=0):
    a+b+c-d



print(Math_Function(a, b, d=6))

def Thinking_Machine(in1=5, in2=10):
    return1=in1+10
    return2=in2+10
    return(return1,return2)

(out1,out2) = Thinking_Machine(10, 20)
print(out1)
print(out2)