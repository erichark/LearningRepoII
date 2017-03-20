'''
Created on Mar 4, 2017

@author: Eric
'''
from LearningPackage.Functions import FirstFunction

tuple1 = ("j","a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

array1 = [1,2,3,4,5,6,7,8,9,10,11]
array2 = [12,13,14,15,16,17,18]

list1=["a","b",["aa","ab","ac"]]

list2=list1




#This is a Comment

#===============================================================================
# Oh this is a fun comment block
#===============================================================================


#Setting up a Dictionary 

Dictionary1 = {"GK":"Aayush", "RB":"Danny", "CB":"Dyhey", "LB": "Paul"}
Dictionary2 = {"Aayush":"Senior", "Danny":"Junior", "Dyhey":"Senior", "Paul":"Senior", "CJ":"Sophomore", }

print(Dictionary1)
print(Dictionary1["GK"])
print(Dictionary2[Dictionary1["GK"]])

Dictionary1["GK"] = "CJ"

print(Dictionary1)
print(Dictionary2[Dictionary1["GK"]])

print("GK" in Dictionary1)
print("GK" in Dictionary2)

print(Dictionary1.get("ST"))
print(Dictionary1)