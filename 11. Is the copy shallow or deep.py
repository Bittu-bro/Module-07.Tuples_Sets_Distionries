import copy


# l1 = [2, 4.7 , [2,8,9] , 6 , "Bittu"]
# print(l1) 
# # print(type(l1))
# # print(id(l1))

# #shallow_copy

# l2 = copy.copy(l1)
# print(l2)
# # print(type(l2))
# # print(id(l2))

# # print(l1[-1])
# # print(l2[-1])

# #Now,
# l1[-1] = "Shivam"
# l2[2][0] = 18
# l1[2][1] = 48

# print(f"l1 here {l1} , {id(l1)}") #they have diffrent memory address, because of they have have diffrent memory address they dont't follow each other changes
# print(f"l1 here {l2} , {id(l2)}") # when we try to change inner list of element we got change in both l1 & l2, because of they have same memory addres

# #you can fatch the memory address with the help of these following option
# print(id(l1[2][0]))
# print(id(l2[2][0]))




#if you want to solve this problem then comes in to thr picture "deepcopy"
student01 = {'name' : "bittu" , 'id' : 253 , 'marks' : {'phy' : 79,'mats' : 87, 'chem' : 96}}
#student02 = copy.copy(student01) # in this case we got change in both dist, because of they have same memory addrees
student02 = copy.deepcopy(student01) # in this case we didn't got change in both dist, because of they did not have same memory addrees
student01['marks']['phy'] = 93
print(student01)
print(student02)
