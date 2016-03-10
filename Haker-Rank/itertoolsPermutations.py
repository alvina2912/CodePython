from itertools import permutations
s=raw_input().split()
S=''.join(sorted(s[0])).upper()
print S
K=int(s[1])
for i in list(permutations(S,K)):
    print "".join(i)
