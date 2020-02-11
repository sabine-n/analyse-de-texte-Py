#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:10:53 2020

@author: utilisateur
"""
from re import findall, sub

def hascap(s):
    l = s.split()
    lif = []
    for mot in l:
        if 65 <= ord(mot[0]) <= 90 :
            lif += [mot]
    return ' '.join(lif)
            

def inflation(s):
    enum = enumerate(s.split())
    for i in enum:
        if i[1].isnumeric():
            s2 = s.replace(i[1],str(int(i[1])*2))            
    return s2

string = 'Who wants a Banana Smoothie?'
caps = hascap(string)
print(caps, '\n')

price = "Le prix est de 10 euros"
    
print(inflation(price), '\n')

s = "Onze ans déjà que cela passe vite Vous "
s += "vous étiez servis simplement de vos armes la "
s += "mort n‘éblouit pas les yeux des partisans Vous "
s += "aviez vos portraits sur les murs de nos villes"

def lignes2(s,nb_char):
    l_new=[]
    l_fin=[]
    #a = ''
    l = s.split()
    for i in l :
        if len(' '.join(l_new))+len(i) < nb_char:
            l_new.append(i)
        else:
            l_fin.append(' '.join(l_new))
            l_new =[]
    return l_fin

l_n2 = lignes2(s,24)   
print(l_n2, '\n')

def lignes(s, nb_char):
    l = s.split()
    l_new = ['']
    for i in l:
        i += ' '
        if len(l_new[-1]) + len(i) <= 24:
            l_new[-1] += i
        else: 
            l_new.append(i)
    return l_new

l_n = lignes(s,24)
print(l_n, '\n')
        
    #l = [s[i:i + nb_char] for i in range(0, len(s), nb_char)]
    #return l

#s2 = lignes(s,24)
#print(s2, '\n')
#print(len(s2[1]), '\n')

s4 = 'Les 2 maquereaux valent 6.50 euros'
l4 = findall('\-?[0-9]+[\.,,]?[0-9]*',s4)
print(l4, '\n')

def arrondi(s):
    s1 = sub('\.[0-9]+', ' ', s)
    return s1

s5 = "Truncate the numbers 9.88, 77.985 and 3.0"
print(arrondi(s5))