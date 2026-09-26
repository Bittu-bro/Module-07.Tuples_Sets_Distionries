# ##==>> cannot use 'list' as a dict key value
# d1 = {[2,4,6] : 12}
# print(d1)


# ##==>> cannot use 'set' as a dict key value
# d2 = {{1,4,3} : 8}
# print(d2)


# ##==>> cannot use 'dist' as a dict key value
# d3 = {{'Bittu' : 20} : 14}
# print(d3)

##>>> Not allowed as a kay value = list, set, dist => these are mutable datatypes

##>>>> allowed as key value = int, float, str, boolean, tuple => these are immutable datatypes

'''thesr are some things you have to remember 
we can use any datatypes in value '''

# d4 = {14 : {'Bittu' : 20}}
# print(d4)
# d5 = {12 : [2,4,6]}
# print(d5)
# d6 = {8 : {1,4,3}}
# print(d6)


student_01 = {'name' : "Bittu", 'id' : 253, 'mark' : {'phy' : 79.3, 'chem' : 94.5,'maths' : 89.6}}
# print(student_01)
# print(type(student_01))
# print(student_01['mark']['maths'])
# print(student_01['mark'][0])


##>>fetch the keys
#key()
print(student_01.keys() , type(student_01))
#values()
print(student_01.values() , type(student_01))
#items()
print(student_01.items() , type(student_01))