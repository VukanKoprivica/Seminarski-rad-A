# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:23:04 2020

@author: PC
"""

def loadDezert():
    for line in open('dezert.txt', 'r').readlines():
        if len(line) > 1:
            dez = str2dezerti(line)
            dezerti.append(dez)

#upisuje novi dezert u fajl

def saveDezert():
    file = open('dezert.txt', 'w')
    for dez in dezerti:
        file.write(dezerti2str(dez))
        file.write('\n')
    file.close()
    

#dodaje dezert u listu

def addDezerti(dez):
    dezerti.append(dez)
    

#cita liniju iz fajla i pretvara je u dezert (kljucevima u recniku dodeljuje vrednosti)

def str2dezerti(line):
    if line[-1] == '\n':
        line = line[:-1]
    sifra, ime, opis,cena = line.split('|')
    dez = {
      'sifra': sifra,
      'ime': ime,
      'opis': opis,
      'cena': cena,
     
    }
    return dez

#priprema string za upisivanje u fajl

def dezerti2str(dez):
    return '|'.join([dez['sifra'], dez['ime'], dez['opis'], 
      dez['cena']])

#header za ispisivanje podataka o dezertu

def formatHeader():
    return \
      "sifra|Ime              |opis                        |cena \n" \
      
#formatira dezert
def formatDezerti(dez):
    return u"{0:5}|{1:17}|{2:28}|{3:4}".format(
      dez['sifra'],
      dez['ime'],
      dez['opis'],
      dez['cena'])

#za svaki dezert ispisuje po jedan red ispod headera

def formatDezert(dezList):
    result = ""
    for dez in dezList:
        result += formatDezerti(dez) + '\n'
    return result

#formatira sve dezerte
def formatAllDezerti():
    result = ''
    for dez in dezerti:
        result += u"{0:5}|{1:17}|{2:28}|{3:4}".format(
      dez['sifra'],
      dez['ime'],
      dez['opis'],
      dez['cena']) +'\n'

    return result
    
#pronalazi dezert pomocu sifre i vraca njegovu cenu
    
def findDezert(sifra):
    for s in dezerti:
        if s['sifra'] == sifra:
            print("Izabrali ste :"+s['ime'])
            return s['cena']
#pronalazi sve dezerte        
def findDezerte():
    rezultat=[]
    for s in dezerti:
        rezultat.append(s)
    return rezultat 


    
print(__name__)  
dezerti = []
loadDezert() 