#!/usr/bin/env python


class ColorString:
    data={}

    def __new__(cls,src):
        obj=cls.data.get(src)
        if not obj:
            cls.data[src]=object.__new__(cls)
        return cls.data[src]

    def __init__(self,src):
        self.src='\t'.join((src,src,src))

    def draw(self,color):
        print('id:{} \033[{}m{}\033[0m'.format(id(self),color,self.src))

if __name__=='__main__':
    for color in ['1;31','1;32','1;33','1;34','1;35','1;36']:
        ColorString("Hello word").draw(color)
        ColorString("Hello word").draw(color)
        ColorString("Hi word").draw(color)
