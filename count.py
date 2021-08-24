list1 =[1,2,1,3,4,2,4,4]

def frequency(list1):  
    dictionary = {}
    for i in list1:
        if (i in dictionary):
            dictionary[i] += 1
        else:
            dictionary[i] = 1
            
    print("{")
    for key, value in dictionary.items():
        list2=[]
        for tempKey,tempValue in dictionary.items():
            if value==tempValue :
                list2.append(tempKey)
        print(list(set(list2)), end =":")
        print ("%d"%(value),end=".\n")         
    print("}")
frequency(list1)        
# {
# [1,2]:2.
# [3]:1.
# [4]:3
# }