# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:48:57 2020

@author: PC
"""

def loadPice():
    for line in open('pice.txt', 'r').readlines():
        if len(line) > 1:
            pic = str2pica(line)
            pica.append(pic)

#upisuje novo pice u fajl

def savePice():
    file = open('pice.txt', 'w')
    for pic in pica:
        file.write(pica2str(pic))
        file.write('\n')
    file.close()
    

#dodaje pice u listu

def addPice(pic):
    pica.append(pic)
    

#cita liniju iz fajla i pretvara je u pice (kljucevima u recniku dodeljuje vrednosti)

def str2pica(line):
    if line[-1] == '\n':
        line = line[:-1]
    sifra, ime, opis,cena = line.split('|')
    pic = {
      'sifra': sifra,
      'ime': ime,
      'opis': opis,
      'cena': cena,
     
    }
    return pic

#priprema string za upisivanje u fajl

def pica2str(pic):
    return '|'.join([pic['sifra'], pic['ime'], pic['opis'], 
      pic['cena']])

#header za ispisivanje podataka o picu

def formatHeader():
    return \
      "sifra|Ime                |opis                 |cena \n" \
      
#formatira pice
def formatPice(pic):
    return u"{0:5}|{1:19}|{2:21}|{3:4}".format(
      pic['sifra'],
      pic['ime'],
      pic['opis'],
      pic['cena'])

#za svako pice ispisuje po jedan red ispod headera

def formatPica(picList):
    result = ""
    for pic in picList:
        result += formatPice(pic) + '\n'
    return result

#formatira sva pica
def formatAllPica():
    result = ''
    for pic in pica:
        result += u"{0:5}|{1:19}|{2:21}|{3:4}".format(
      pic['sifra'],
      pic['ime'],
      pic['opis'],
      pic['cena']) +'\n'

    return result
    
#pomocu sifre pronalazi pice i vraca njegovu cenu
def findPice(sifra):
    for s in pica:
        if s['sifra'] == sifra:
            print("Izabrali ste :"+s['ime'])
            return s['cena']
#pronalazi sva pica        
def findPica():
    rezultat=[]
    for s in pica:
        rezultat.append(s)
    return rezultat 


    
print(__name__)  
pica = []
loadPice() 