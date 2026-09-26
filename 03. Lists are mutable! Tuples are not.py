# #mutable or immutable

# list are mutable
# string or tuple are immutable


# s1 = "python is fun"
# print(s1)


# s1.replace("python", "java")
# print(s1) # it's dosn't work, because of relace function only can store new value in new variable not in existing value



# s2 = s1.replace("python", "java")
# print(s2)


# t1 = ("Banana", "Popaya" , "Mango")
# t1.append("Apple")   # this append function does't support because of we are try to aprate with tuple
# print(t1)



# l1 = ["Banana", "Popaya" , "Mango"]
# print(l1)
# print((id(l1)))        #lets try to understand with the help of 'memory id'  


# l1.append("Apple")      # this append function does support because of we are try to aprate with list
# print(l1)
# print((id(l1)))          #"memory id" remains same





# # Reassign the value

# l1 = ["Banana", "Popaya" , "Mngo"]
# print(l1)
# print((id(l1))) 

# l1[-1] = "Mango"
# print(l1)
# print((id(l1)))             #it's support opration besause of we are oprating with list! Not tuple




t1 = "Banana", "Popaya" , "Mngo"  '''     "Python is Fun"   '''            # string
t2 = ("Banana", "Popaya" , "Mngo")                                         # tuple
print(t1)
print(t2)



print((id(t1)))
print((id(t2)))


# t1[-1] = "Mango"
# t2[-1] = "Mango"           # it's never be work you can try with both one by one because of they are tuple.



print([t1])
print([t2])


print((id(t1))) 
print((id(t2))) 

