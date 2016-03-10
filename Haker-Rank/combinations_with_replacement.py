from itertools import combinations_with_replacement
s= raw_input().split()
S=s[0].upper()
K=int(s[1])
print sorted(list(combinations_with_replacement(sorted(S),K)))

for i in sorted(list(combinations_with_replacement(sorted(S),K))) :
    print"".join(i)
