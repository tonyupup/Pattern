#!/usr/bin/env python

class Singleton:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            obj=super(Singleton,cls)
            cls._instance=obj
        return cls._instance

class Config(Singleton):
    def __init__(self,path):
        self._path=path


if __name__=='__main__':
    mConfig2=Config("./owner.conf")
    mConfig1=Config("./owner.conf")

    print("mConfig1",mConfig1 ,id(mConfig1))
    print("mConfig2",mConfig2,id(mConfig2))
