import time
searchFor=int(input("Enter the item to search for: "))
list=[2,5,6,8,9,13,16,18,19,23,25,28,76,86,99,123,
      146,167,190,215,222,246,279,299,355]

low=0
halfWay=0
high=len(list)-1
found=False
iterations=0
while low<=high and found == False:
    time.sleep(1)
    halfWay=(high+low)//2
    iterations=iterations+1
    print("Iteration = ", iterations)
    print("Halfway= ",halfWay)
    print("Comparing ", list[halfWay],"to ", searchFor)
    if list[halfWay]<searchFor:
       low=halfWay+1
    elif list[halfWay]> searchFor:
        high=halfWay-1
    else:
        print("Found at index", halfWay)
        found=True
if found==False:
    print("Can't find what you were looking for in the list!")
print("This search took ", iterations, "iterations")
        