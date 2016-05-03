class C:
  dangerous = 2
c1 = C()
c2 = C()
print c1.dangerous # 2
c1.dangerous = 3
print c1.dangerous # 3
print c2.dangerous # 2
del c1.dangerous
print c1.dangerous # 2
C.dangerous = 3
print c2.dangerous # 2

#instant variable and static variable in python
