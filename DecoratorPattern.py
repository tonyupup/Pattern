#!/usr/bin/env python
import random
import  time

def constTime(func):
    def wrap(self,*args,**kwargs):
        start=time.time()
        result=func(self,*args,**kwargs)
        print("Use {}s".format(time.time()-start))
        return result
    return wrap


class Demo:
    def run(self):
        time.sleep(random.randint(0,5))
        print("Demo run done.")
        return 

class Decorator:
    def __init__(self,wrapper):
        self._wrapper=wrapper

    def run(self):
        start=time.time()
        result=self._wrapper.run()
        print("Use {}s.".format(time.time()-start))
        return result

if __name__=='__main__':
    obj=Demo()
    obj=Decorator(obj)
    obj.run()
