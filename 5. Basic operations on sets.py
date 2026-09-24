# nums = {3,1,9,3,8}
# print(nums)


# # #Membership oprater

# print(2 in nums)
# print(2 not in nums)

# print(3 in nums)
# print(3 not in nums)

# #Concatenation ?
# nums_1 = {3,9,0}
# #print(nums+nums_1)                      # It's dos't support with set.

# #Repeating ?
# #print(nums*2)                            # It's dos't support with set.



# #sets are mutable or immutable ? 

# #indexing in set
# print(nums[0])                   # It's dos't support with set.


# # #Type casting
# # print(list(nums))
# # print(tuple(nums))



   
# print(len(nums))
# #    Its mutable. and one thing you should have to notice . we got length of set is 4 but we 5 element in our set 
# #we got 4 becasue of set dosn't allow duplicate of element.










# now, we have some good function (add, remove, dicard)

natural_number = {1,2,3,4,5,6,7,8,9,10}
print(natural_number)
print(f"Length of the natural number: {len(natural_number)}")

# ## Add
'''# #natural_number.add(11,12,13,14,15).       #TypeError: set.add() takes exactly one argument (5 given)
# #   you can add only one element at a time '''


# natural_number.add(11)
# print(natural_number)

# natural_number.add(10)  # Whene you try to add something whose already persent then python does't give error to us 
# #They do yield results, but duplication within the set is not permitted; therefore, we do not see any changes in the set.
# print(natural_number)


##Remove
# #natural_number.remove(11,12,13,14,15)   #TypeError: set.remove() takes exactly one argument (5 given)
# #   you can remove only one element at a time 
#natural_number.remove(11) #          We got "KeyError: 11" Because of 11 is not persent in set

# natural_number.remove(10)
# print(natural_number)

##Discard
#natural_number.discard(11,12,13,14,15)   #TypeError: set.discard() takes exactly one argument (5 given)
# #   you can remove only one element at a time 
natural_number.discard(11) #          We got no "KeyError: 11", Even though 11 doesn't exist at all, still...
print(natural_number)


natural_number.discard(10)
print(natural_number)


#summary: The remove function works only with elements that are available in the set, and...
# The `discard` function works regardless of whether the element is present in the set or not.