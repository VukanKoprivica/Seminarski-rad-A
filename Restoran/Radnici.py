# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:04:19 2020

@author: PC
"""

# radnici.py

#funkcionalnost radnika
#radnici se ucitavaju iz fajla u recnik
#kljucevi u recniku su ime, prezime, username i password

#radnik mora da se uloguje - proverava se da li uneti username i password postoje

#proveravanje username i password
def login(username, password):
    for rad in radnici:
        if rad['username'] == username and rad['password'] == password:
            return True
    return False
    
def loadRadn():
    for line in open('radnici.txt', 'r').readlines():
        if len(line) > 1:
            rad = str2rad(line)
            radnici.append(rad)
   #upisuje novog radnika u fajl             
def saveRadnika():                
    file = open('radnici.txt', 'w')
    for rad in radnici:
        file.write(rad2str(rad))
        file.write('\n')
    file.close()
#cita liniju iz fajla i pretvara je u radnika (kljucevima u recniku dodeljuje vrednosti)
def str2rad(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, username, password = line.split('|')
    rad = {
      'ime': ime,
      'prezime': prezime,
      'username': username,
      'password': password
    }
    return rad

#priprema string za upisivanje u fajl
    
def rad2str(rad):
    return '|'.join([rad['ime'], rad['prezime'], rad['username'], rad['password']])

#dodaje radnika u listu
def addRadnika(rad):
    radnici.append(rad)

radnici = []
loadRadn()