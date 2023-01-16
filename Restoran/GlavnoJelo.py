# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:22:11 2020

@author: PC
"""

def loadGlavnoJelo():
    for line in open('glavnojelo.txt', 'r').readlines():
        if len(line) > 1:
            glavno = str2glavnojelo(line)
            glavna.append(glavno)

#upisuje novog glavnog jela u fajl

def saveGlavnoJelo():
    file = open('glavnojelo.txt', 'w')
    for glavno in glavna:
        file.write(glavnojelo2str(glavno))
        file.write('\n')
    file.close()
    

#dodaje glavno jelo u listu

def addGlavnoJelo(glavno):
    glavna.append(glavno)
    

#cita liniju iz fajla i pretvara je u glavno jelo (kljucevima u recniku dodeljuje vrednosti)

def str2glavnojelo(line):
    if line[-1] == '\n':
        line = line[:-1]
    sifra, ime, opis,cena = line.split('|')
    glavno = {
      'sifra': sifra,
      'ime': ime,
      'opis': opis,
      'cena': cena,
     
    }
    return glavno

#priprema string za upisivanje u fajl

def glavnojelo2str(glavno):
    return '|'.join([glavno['sifra'], glavno['ime'], glavno['opis'], 
      glavno['cena']])

#header za ispisivanje podataka o studentima

def formatHeader():
    return \
      "sifra|Ime                            |opis                  |cena \n" \
      

def formatGlavnoJelo(glavno):
    return u"{0:5}|{1:31}|{2:22}|{3:4}".format(
      glavno['sifra'],
      glavno['ime'],
      glavno['opis'],
      glavno['cena'])

#za svako jelo ispisuje po jedan red ispod headera

def formatGlavnaJela(glavnoList):
    result = ""
    for glavno in glavnoList:
        result += formatGlavnoJelo(glavno) + '\n'
    return result

#formatira svako jelo
def formatAllGlavnaJela():
    result = ''
    for glavno in glavna:
        result += u"{0:5}|{1:31}|{2:22}|{3:4}".format(
      glavno['sifra'],
      glavno['ime'],
      glavno['opis'],
      glavno['cena']) +'\n'

    return result
 
#pronalazi pomocu sifre jelo i vraca njegovu cenu    
def findGlavnoJelo(sifra):
    for s in glavna:
        if s['sifra'] == sifra:
            print("Izabrali ste :"+s['ime'])
            return s['cena']
        
#pronalazi sva glavna jela
def findGlavnaJela():
    rezultat=[]
    for s in glavna:
        rezultat.append(s)
    return rezultat 

    
print(__name__)  
glavna = []
loadGlavnoJelo() 