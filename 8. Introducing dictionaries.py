 #Distionaries=> comma seprated key value : pairs enclosed within {}
#{key_value1 : value1, key_value2 : value2}

groceries = {'milk' : 60, 'sugar' : 60, 'rice' : 80}
print(groceries)
print(type(groceries))
#print(len[groceries]) #=> len function dosn't suppoort dist
#print(groceries[0])   #=> indexing function dosn't suppoort dist

#=> Dist are mutable or immutable
print(groceries['milk'])
#print(groceries['Pluse']). We got "KeyError" 

#####print(groceries[60]) # dist only fatch value with the help of key value.

#Now come to on the topic
groceries['milk'] = 70 
print(groceries)    #.      value updated
groceries['Pluse'] = 110 
print(groceries) #.          value added
