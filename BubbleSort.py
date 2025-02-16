list = [4,6,2,9,1,0,7,8, 99, 123,76,-2, 1000,3]

# buffer variable
buffer=0
#list length
length=len(list)

for count in range(0,length,1):
    index=0
    while index<length-1:
        if list[index]>list[index+1]:
            #Preform a swap
            buffer=list[index]
            list[index]=list[index+1]
            list[index+1]=buffer
        index=index+1
            
        
print("The list is, ",list)