#!/usr/bin/env python3

import time
import csv

def lect_csv(infile : str, delim : str=';',codec : str='utf-8') -> list[dict]:
    """read csvfile"""
    with open(infile,'r',newline='',encoding = codec) as f:
        reader = csv.DictReader(f,delimiter=';')
        ret = [row for row in reader]
    return ret

def lecture_csv(infile : str, delim : str=';',codec : str='utf-8') -> list[str]:
    """read csvfile"""
    ldict=[]
    with open(infile,'r',encoding = codec) as f:
        desc,*lines = f.read().splitlines()
        for l in lines:
            temp=[(d,i) for d,i in zip(desc.split(delim),l.split(delim))]
            ldict.append(dict(temp))

    return ldict

def lecture(fichier, delimiter = ';', encodage='utf-8'):
    liste_donnees = []
    with open(fichier, 'r', encoding=encodage) as entree:
        labels = entree.readline().strip().split(delimiter)
        for donnee in entree:
            liste_des_infos = donnee.strip().split(delimiter)
            d = {labels[index]:info for index, info in enumerate(liste_des_infos)}
            liste_donnees.append(d)
    return liste_donnees

if __name__ == '__main__':

    tp1 = time.time()

    maliste = lect_csv('nat2020.csv')

    print(time.time() - tp1)
    print(type(maliste))

