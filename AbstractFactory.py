#!/usr//bin/env python
class Mouse:
    def done(self):
        pass

class HpMouse(Mouse):
    def done(self):
        return "This is HpMouse."

class DellMouse(Mouse):
    def done(self):
        return "This is DellMouse."

#keyboard

class KeyBoard:
    def done(self):
        pass

class HpKeyBoard(KeyBoard):
    def done(self):
        return "This is HpKeyBoard."

class DellKeyBoard(KeyBoard):
    def done(self):
        return "This is DellKeyBoard."

class PcFactory:
    def createMouse(self)->Mouse:
        pass

    def createKeyBoard(self)->KeyBoard:
        pass

    def run(self):
        mouse=self.createMouse()
        keyboard=self.createKeyBoard()
        return mouse,keyboard

class HpFactory(PcFactory):
    def createMouse(self)->Mouse:
        return HpMouse()
    def createKeyBoard(self)->KeyBoard:
        return HpKeyBoard()

class DellFactory(PcFactory):
    def createMouse(self)->Mouse:
        return DellMouse()
    def createKeyBoard(self)->KeyBoard:
        return DellKeyBoard()

class Test:
    def __init__(self,factory):
        self.factory=factory()
    def apply(self):
        mouse,key=self.factory.run()
        print(mouse.done())
        print(key.done())

if __name__=='__main__':
    a=Test(HpFactory)
    a.apply()
