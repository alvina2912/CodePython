from abc import ABCMeta,abstractmethod

class Human(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def run(self):
        print "running..."

class Robot(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def vacuum(self):
        print "vacumming...!"

class Cyborg(Human,Robot):

    def run(self):
        print "Human can run..!"

    def vacuum(self):
        print "Robot can vacuum"

obj=Cyborg()
obj.run()
obj.vacuum()
