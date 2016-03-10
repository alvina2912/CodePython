from itertools import groupby

num=raw_input()
count=1
for key, group in groupby(num):
    print (len(list(group)),int(key)),
