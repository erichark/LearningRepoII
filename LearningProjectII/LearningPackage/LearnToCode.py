'''
Created on Mar 4, 2017

@author: Eric
'''


tuple1 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")

array1 = [1,2,3,4,5,6,7,8,9,10,11]
array2 = [12,13,14,15,16,17,18]


array1.extend(tuple1)
print(array1)

array1.remove("a")

print(array1)

array1 = [1,2,3,4,5]
print(array1[1])
print(array1[3])
z=array1[1]+array1[3]
print(z)


print("append and pop")


big_list = ["Mata","Rooney", "lindgard", "martial", "fellani"]
print(big_list)
big_list.pop(9)
print(big_list)
big_list.append("Ibra")
print(big_list)


array1.insert(11, "a")
print (array1)