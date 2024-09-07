#!/usr/bin/env python3

def num(x : int):

    if x>64:
        u=x-55
    else:
        u=x-48
    return u

def val_from_string(text : str, base : int=10 ):

    ret = 0
    raw = [num(ord(x)) for x in text]
    raw.reverse()

    for index,nb in enumerate(raw):
        ret += nb * (base**index)

    return ret

def val_to_string(val : int, b : int):
   
    CHAR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = ""
    q=1
    while(q>0):
        q,r= val//b,val%b
        ret += CHAR[r]
        val=q
    return ret[::-1]

def changement_de_base(rep_a, a, b):
    
    val = val_from_string(rep_a,a)
    print(val)
    ret = val_to_string(val,b)
    print(ret)

changement_de_base('10',10,2)
