#HakerRank
#A Discrete Mathematics professor has a class of NN students. Frustrated with their lack of discipline,
#he decides to cancel class if fewer than KK students are present when class starts.
#Given the arrival time of each student, determine if the class is canceled.



import sys
t = int(raw_input().strip())
count=0
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    print n, k, a
    for i in a:
        if a[i]<0:
            count=count+1
    if count>=k :
        print "Class Cancle "
    else :
        print "Class not cancle"
           
