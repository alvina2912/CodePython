def findNum(matrix,num):
    for i in range(3):
        for j in range(2,0,-1):
            if num==matrix[i][j]:
                return True
            elif num < matrix[i][j]:
                j-=1
            else:
                i+=1
    return False


matrix=[[]]
matrix=[[int(raw_input()) for i in range(1,4)] for i in range(1,4)]
num=int(raw_input("Enter the number to be found in Matrix :"))
'''matrix[0][0]=1
matrix[0][1]=2
matrix[0][2]=3
matrix[1][0]=4
matrix[1][1]=5
matrix[1][2]=6
matrix[2][0]=7
matrix[2][1]=8
matrix[2][2]=9'''
result= findNum(matrix,num)
print result
