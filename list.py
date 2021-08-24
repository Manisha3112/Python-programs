list1 = ['aajith', 'arjun', 1998, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
list1[2] = 2001               #Update list
list1.insert(1, 'akshara')    #Insertion
print ("New value in index 2 : ", list1[2])
del list2[2]                  #Delete list
print ("After deleting value at index 2 : ", list2)
print("length: ",len(list2))  #Length
print(['python'] * 4)         #Repitation
print(3 in [1, 2, 3] )        #Membership
list3=['hi','hello','what']    
list3.sort()                 #Sorting
print(list3)
list3.reverse()              #REversing
print(list3)  
list3.remove('hi')
print ("list3 : ", list3)    #Removing
aList = [123, 'xyz', 'abc', 'abc', 123];#Count
print ("Count for 123 : ", aList.count(123))
print ("Count for abc : ", aList.count('abc'))
for value in [1,2,3] : 
    print (value,end=' ')        #Iteration 