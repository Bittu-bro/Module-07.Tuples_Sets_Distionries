s1 = {1,2,3,4}
s1.add(-1)
print(s1, type(s1))

###frozen set - immutable set
fs1 = frozenset(s1)
print(fs1, type(fs1))


# ###Add
# fs1.add(40)                    #Frozen set dosn't allow (any write function) some function like Add, Remove and Discard
# print(fs1, type(fs1))


frozen_set_01 = ({3,4,6,0,2})
frozen_set_02 = ({3,0,5,7,8,9,2})
print(frozen_set_01 - frozen_set_02)      #Diffrence function
print(frozen_set_01 & frozen_set_02)       #Intersection function
print(frozen_set_01 | frozen_set_02)      #Union function
