# bittu = {'Phy' : 90, 'Maths': 89, 'Chem' : 92}
# # print(bittu)
# # print(type(bittu))

# # #fatch the value of key value>>
# # print(bittu['Phy'])
# # print(bittu['Chem'])

# # # => get()

# # print(bittu.get('Maths'))
# # print(bittu.get('Chem'))
# # print(bittu.get('Eng')) #.    you noticed one thing when we enter a invalid key value we got "none" not "type error"
# #print(bittu.get('Eng' , 80)) # you noticed one more thing when we enter a new key value and value we got "new value" not "type error"


# #Membership oprater
# print('Maths' in bittu)
# print('Eng' in bittu)
# print('Chem' in bittu)
# print(90 in bittu) # see we can not fatch with the help of value
# print(92 in bittu)



####let's take one more example

sem1_mark = {'Maths' : 80, 'Phy' : 90, 'Chem' : 79 ,'Maths' : 89}    # dist dosn't allow to duplicate key value & it's fatching the value from left tp right. to updare it self
sem2_mark = {'Eng' : 93, 'Hindi' : 87, 'Sans' : 87}
print(sem1_mark)


# ##>>>>>>Update
# sem1_mark.update(sem2_mark)
# print(sem1_mark)

# ##>>>>>>pop(). use for the removing the key value
# sem1_mark.pop('Maths')
# sem2_mark.pop('Hindi')
# print(sem1_mark)
# print(sem2_mark)