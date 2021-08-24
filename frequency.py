list1 =[1,2,1,3,4,2,4,4]
def frequency(list): 
    dictionary = {}
    for i in list:
        if (i in dictionary):
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    output={}        
    for key,value in dictionary.items() :
        list2=[]
        for temp_key,temp_value in dictionary.items():
            if value==temp_value :
                list2.append(temp_key)   
        output[tuple(list2)]=value
    print(output)
frequency(list1)       
# {
# [1,2]:2.
# [3]:1.
# [4]:3
# }