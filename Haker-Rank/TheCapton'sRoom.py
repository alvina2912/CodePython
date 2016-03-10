k=int(raw_input("Enter Size of each group :"))
roomNumList=map(int,raw_input().split())
print roomNumList
'''for i in range(len(roomNumList)):
    if roomNumList.count(roomNumList[i]) is not k:
        print "Room num :",roomNumList[i]'''
a=sum(roomNumList)*k
b=sum(set(roomNumList))
print"a=",a
print"b=",b
print"a-b",((a-b)/k)/k
