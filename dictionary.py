dict = {'Name': 'Manisha', 'Age': 20, 'Department': 'ECE'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
dict['Name'] = 'S Manisha';              # Update
dict['college'] = "SIET"                 # Add new 
print ("dict['Name']: ", dict['Name'])
print ("dict['college']: ", dict['college'])
print ("Length : " , len (dict))
print ("Equivalent String :",str (dict))
print ("Variable Type :" , type (dict))
dict2 = dict.copy()
print ("New Dictionary : ",dict2)
print ("Value : " , dict.get('Age'))
print ("Value : ", dict.keys())
dict.clear() # remove all entries in dict
del dict # delete entire dictionary