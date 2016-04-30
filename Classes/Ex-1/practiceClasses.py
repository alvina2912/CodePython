class BaseCharecter(object):
    def __init__(self,name):
        self.name=name
    def printName(self):
        print self.name

class NonPlayableCharecters(BaseCharecter):
    def __init__(self,name):
        super(NonPlayableCharecters,self).__init__(name)

class PlayableCharecters(BaseCharecter):
    def __init__(self,name):
        super(PlayableCharecters,self).__init__(name)

class Friendly(NonPlayableCharecters):
    def __init__(self,name):
        super(Friendly,self).__init__(name)

class Enemy(NonPlayableCharecters):
    def __init__(self,name):
        super(Enemy,self).__init__(name)
        self.attackDamage=5

class Archer(PlayableCharecters):
    def __init__(self,name,someWeapon):
        super(Archer,self).__init__(name)
        self.someWeapon=Weapon(someWeapon)

class Buther(PlayableCharecters):
    def __init__(self,name,someWeapon):
        super(Buther,self).__init__(name)
        self.someWeapon=Weapon(someWeapon)

class GreenLantern(PlayableCharecters):
    def __init__(self,name,someWeapon):
        super(GreenLantern,self).__init__(name)
        self.someWeapon=Weapon(someWeapon)

class Weapon:
    def __init__(self,someWeapon):
        self.someWeapon=someWeapon

a=Archer("Alvina","bow")
a.printName()
print a.someWeapon.someWeapon
b=Buther("Roger","Sword")
b.printName()
print b.someWeapon.someWeapon
