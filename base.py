#!/usr/bin/env python3

TEST = "145"
a = 16
b = 8

def filter(x : int):

    if x>64:
        u=x-55
    else:
        u=x-48
    return u

def val_from_string(text : str, base : int=10 ):

    ret = 0
    raw = [filter(ord(x)) for x in TEST]
    raw.reverse()

    for index,nb in enumerate(raw):
        ret += nb * (base**index)

    return ret

x = val_from_string(TEST, 8)

print(x,type(x))
