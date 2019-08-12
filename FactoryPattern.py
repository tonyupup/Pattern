#!/usr/bin/env python
class Mouse:
    def done(self):
        pass

class DellMouse(Mouse):
    def done(self):
        return "This is DellMouse."

class HpMouse(Mouse):
    def done(self):
        return "This is HpMoude."

class MouseFactory:
    def createMouse(self)->Mouse:
        pass

class HpMouseFactory(MouseFactory):
    def createMouse(self)->Mouse:
        return HpMouse()

class DellMouse(MouseFactory):
    def createMouse(self)->Mouse:
        return DellMouse()

class Test:
    def __init__(self,Factory):
        self.factory=Factory()
    def apply(self):
        mouse=self.factory.createMouse()
        print(mouse.done())

if __name__=='__main__':
    a=Test(HpMouseFactory)
    a.apply()

