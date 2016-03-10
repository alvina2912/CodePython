from itertools import combinations
s=raw_input().split()
S=s[0].upper()
print S
K=int(s[1])
for i in range(1, K+1):
    l = sorted(list(combinations(S, i)))
    
    print"\n".join(''.join(elems) for elems in l)
