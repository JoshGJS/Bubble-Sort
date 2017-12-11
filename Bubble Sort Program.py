
import random

def main():
    numList = []
    
    def listLength():
        global length
        print("")

        try:
            length = int(input("Enter the length of the list (less than 1001, greater than 0):"))

        except:
            print("Invalid input")
            listLength()

        if length > 1000:
            print("The length of the list must be less than 1001.")
            listLength()

        if length < 1:
            print("The length of the list must be greater than 0.")
            listLength()

    listLength()

    try:
        print("")
        showAll = str(input("Do you want to display the list as it is being changed (y/n)?"))
        showAll = showAll.lower()

    except:
        pass

    if length == 1:
        numList.append(random.randint(1,10))

    elif length < 101:
        for i in range(length):
            numList.append(random.randint(1,100))

    elif length < 1001:
        for i in range(length):
            numList.append(random.randint(1,1000))

    else:
        print("Error.")

    if length == 1:
        print("")
        print("This is the list: " + str(numList))
        print("")

    else:
        print("")
        print("This is the list before sorting: " + str(numList))
        print("")
        print("Sorting...")
        print("")

        for repeats in range(length):
            if showAll == "y":
                print("")
                print("Sort " + str(repeats + 1))
                print("")
            
            for pos in range(length - repeats):
                if pos == length - repeats - 1:
                    pass
                
                elif numList[pos] < numList[pos + 1]:
                    pass

                elif numList[pos] > numList[pos + 1]:
                    numList[pos], numList[pos + 1] = numList[pos + 1], numList[pos]

                if showAll == "y":
                    print(str(pos + 1) + ". " + str(numList))

        print("")
        print("This is the list after sorting: " + str(numList))


main()
                
                    
        
        
