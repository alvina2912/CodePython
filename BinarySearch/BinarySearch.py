#Binary search

li=[2,500,6,9,10,20,200,20]
#[2, 6, 9, 10, 10, 20, 20, 20, 20, 30, 30, 40, 40, 50, 50, 100, 200, 300, 500]
li.sort()
print li

num=raw_input("Enter a number :")

def BinarySearch(li,num):
    start_index=1
    
    end_index=len(li)-1
    while True:
        middle_index=len(li)/2
        middle_num=li[middle_index]
        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False
        if num==middle_num :
            #print "We found the number"
            return True
        elif num>middle_num:   
            start_index=middle_index
        else: 
            end_index=middle_index
    
       
print (BinarySearch(li,num))
       
        
    
