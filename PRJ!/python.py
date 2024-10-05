
# if "a" in mylist:
#     mylist.remove("a")

#     print(mylist)

# if "a" in mylist:
#     print("aaye aaye captain")
# else:
#     print("aaye aaye nahi hai captain")

# mylist.pop(0)

# print(mylist)

# mylist.append("f")


# mylist1 = [1,-2,4,9,4,687]
# mylist1.sort()
# print(mylist1)


# mylist2 = [10,20,30,40]

# mylist1.extend(mylist2)

# print(mylist1)

# mylist1.insert(2,50)

# print(mylist1)

# mylist1.remove(4)

# print(mylist1)

# [-2, 1, 4, 4, 9, 687]
# [-2, 1, 4, 4, 9, 687, 10, 20, 30, 40]
# [-2, 1, 50, 4, 4, 9, 687, 10, 20, 30, 40]
# [-2, 1, 50, 4, 9, 687, 10, 20, 30, 40]

# mylist = [10,20,30,40]
# a= mylist[1:3]
# print(a)

# tuple


# mytuple = ("aaladin", "aaladinchirag", 23)
# print(mytuple)

# mytuple[0] = "aal"

# tuple is immutable

# mytuple = ("a","b","c","d","e","f","g","h")\

# print(mytuple.index("g"))

# b = mytuple[2:5]
# print(b)

# name, age ,city = mytuple

# print(name)

# print(age)

# print(city)

# import sys

# my_list = [0,0,3,"hello", True]
# my_tuple = [0,2,3,"hello", True]

# print(sys.getsizeof(my_list), "bytes")
# print(sys.getsizeof(my_tuple), "bytes")

# import time


# dictionary

# mydict = {"name":"ayush", "age":"5", "city":"jbps"}
# print(mydict)

# mydict["email"] = "ayush@231.com"
# print(mydict)

# mydict.popitem()
# print(mydict)

# print(mydict)

# mydict = {"name":"ayush", "age":"5", "city":"jbps"}
# print(mydict)

# try:
#     print(mydict["name"])

# except:
#     print("error")


# mydict = {"name":"ayush", "age":"5", "city":"jbps"}

# # for value,key in mydict.items():
# #     print(value, key)


# mydict_cpy = mydict
# print

# mydict_cpy["age"] = "10"

# print(mydict)

# print(mydict_cpy)

# mydict = {"name":"ayush", "age":"5", "city":"jbps"}
# mydict_cpy = {"name":"ayu", "age":"25", "city":"indr","email":"myemail"}

# mydict.update(mydict_cpy)

# print(mydict)

# mydict = {3,6,9,36,9,8}
# print(mydict)

# mytuple = {0,7}
# mydict = {mytuple: 15}

# print(mydict)

# sets?
# myset = set()
# myset = {1,2,3,4,}

# odds = {1,3,5,7,9}
# even = {0,2,4,6,8}
# prime ={2,3,5,7}

# u = odds.union(even)
# print(u)

# i = odds.intersection(prime)
# print(i)


# set_a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# set_b =  {0, 1, 2, 4, 6, 8, 9}

# diff = set_a - set_b
# print(diff)

# print(set_a.isdisjoint)
# my_str = '''hell this is ayush gautam
# lorem ipsum dolor lorem30

# print(my_str)'''

# print(my_str)
# from itertools import product
# a= [1,2,3]
# b= [4,5,6,7,8,9]

# prod = product(a,b, repeat =2)
# print(list(prod))


# from itertools import permutations
# a = [1,2,3]
# perm = permutations(a)
# print(list(perm))

# from itertools import combinations, combinations_with_replacement
# a = [1,2,3,4,5,6,7]
# comb = combinations(a,2)
# print(list(comb))

# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))

# from itertools import accumulate
# a = [1,2,3,4,5,6,7]
# acc = accumulate(a)
# print(a)
# print(list(acc))

# [1, 2, 3, 4, 5, 6, 7]
# [1, 3, 6, 10, 15, 21, 28]


# from itertools import groupby

# a = [1,2,3,4,5,6,7]



# lambda function

# add10 = lambda x: x + 10
# print(add10(5))
# def add10_func(x):
#     return x + 10

# mult = lambda x,y: x*y
# print(mult(2,7))


# points20 = [1,2,8,5,5,6,798,32,3]

# print(points20)
# print (sorted(points20))

# a = [99,4,54,5,787,8797,345,4]
# print(sorted(a))

# a = [1,2,3,5,6,7,8,9,]
# b = [7,6,5,4,3,3,4,6]

# print(set(a) & set(b))

# a = [1,2,3,5,6,7,8,9,]
# b = [7,6,5,4,3,3,4,6]

