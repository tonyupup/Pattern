#!/usr/bin/env python

class Proxy:
    def __init__(self,obj):
        self._obj=obj

    def __getattr__(self,attr):
        print("Call Proxy{}".format(attr))
        return getattr(self._obj,attr)


class Test:
    def __init__(self):
        self.i=0

    def print(self):
        print("xxxx:{}".format(self.i))


if __name__=='__main__':
    t=Test()
    demo=Proxy(t)
    demo.print()

    demo.i=1
    demo.print()


