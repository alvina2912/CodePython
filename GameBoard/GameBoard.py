#Game Board

size=int(raw_input("Enter the Dimention :"))

def DrawGameBoard(size):
    for i in range (size):
        print("--- " *size)
        if i <size :
            print("|   "* (size+1) )    
     
DrawGameBoard(size)        