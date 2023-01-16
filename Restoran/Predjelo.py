# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 16:12:07 2020

@author: PC
"""


def loadPredjelo():
    for line in open('predjelo.txt', 'r').readlines():
        if len(line) > 1:
            pred = str2predjelo(line)
            predjela.append(pred)

#upisuje novo predjelo u fajl

def savePredjelo():
    file = open('predjelo.txt', 'w')
    for pred in predjela:
        file.write(predjelo2str(pred))
        file.write('\n')
    file.close()
    

#dodaje predjelo u listu

def addPredjelo(pred):
    predjela.append(pred)
    

#cita liniju iz fajla i pretvara je u predjelo (kljucevima u recniku dodeljuje vrednosti)

def str2predjelo(line):
    if line[-1] == '\n':
        line = line[:-1]
    sifra, ime, opis,cena = line.split('|')
    pred = {
      'sifra': sifra,
      'ime': ime,
      'opis': opis,
      'cena': cena,
     
    }
    return pred

#priprema string za upisivanje u fajl

def predjelo2str(pred):
    return '|'.join([pred['sifra'], pred['ime'], pred['opis'], 
      pred['cena']])

#header za ispisivanje podataka

def formatHeader():
    return \
      "sifra|Ime                          |opis                                   |cena \n" \
      
#formatira predjelo
def formatPredjelo(pred):
    return u"{0:5}|{1:29}|{2:39}|{3:4}".format(
      pred['sifra'],
      pred['ime'],
      pred['opis'],
      pred['cena'])

#za svako predjelo ispisuje po jedan red ispod headera

def formatPredjela(predList):
    result = ""
    for pred in predList:
        result += formatPredjelo(pred) + '\n'
    return result

#formatira sva predjela
def formatAllPredjela():
    result = ''
    for pred in predjela:
        result += u"{0:5}|{1:29}|{2:39}|{3:4}".format(
      pred['sifra'],
      pred['ime'],
      pred['opis'],
      pred['cena']) +'\n'

    return result
#pronalazi odredjeno predjelo po sifri i vraca njegovu cenu    
def findPredjelo(sifra):
    for s in predjela:
        if s['sifra'] == sifra:
            print("Izabrali ste :"+s['ime'])
            return s['cena']
        
#pronalazi sva predjela    
def findPredjela():
    rezultat=[]
    for s in predjela:
        rezultat.append(s)
    return rezultat 
    
print(__name__)  
predjela = []
loadPredjelo() 