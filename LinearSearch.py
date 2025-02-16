import time

def linearSearch(list, lookFor):
    found=False #changes to True if the number is found
    index=0 #Incrementor for searching through the list
    while found == False and index < len(list):#looping while number isn't found and there are still numbers in the list
        time.sleep(1)
        print("Searching for ", lookFor, "at index", index)
        if list[index]==lookFor: #compares and checks for the right number
            print("Found at location ", index)
            found=True #Changes found to True to stop the while loop
            #index=index+1
        else:
            time.sleep(1)
            print("Not at index,", index)
            index=index+1 #adds 1 to our incrementor

    
    if found==False:
        print("Sorry, not in list")




linearSearch([1,4,3,7,5,2,9,6], 9)