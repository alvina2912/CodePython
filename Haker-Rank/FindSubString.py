str=raw_input()
substr=raw_input()
count=0
for i in range(len(str)):
    j=i+len(substr)
    if str[i:j]==substr:
        count=count+1
print count