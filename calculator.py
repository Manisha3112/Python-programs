import json
file=open('cal.json',)
input =json.load(file)
def add(value):
    return value[0]+value[1]
def sub(value):
    return value[0]-value[1]    
def mul(value):
    return value[0]*value[1]  
def div(value):
    return value[0]/value[1]              
output={
    "add":add,
    "sub":sub,
    "mul":mul,
    "div":div
}    
for data in input['calculations']:
    values=[]
    for element in data['value']:
        values.append(element)
    print(output[data['operation']](values))        

       