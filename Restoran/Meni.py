# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:55:47 2020

@author: PC
"""
#koristimo sve metode iz radnici,predjelo,glavnojelo,
#dezert i pice
import Radnici
import Predjelo
import GlavnoJelo
import Dezert
import Pice
import matplotlib.pyplot as plt

#radnik se prijavi pa se ispise glavni meni
def main():
    print()
    print( "Kasa restorana")
    print( "====================")
    while not login():
        print( "\nNiste uneli postojece ime i lozinku!")
        
    komanda = '0'
    while komanda != 'X':
        komanda = menu()
        if komanda == '1':
            addPredjela()
        elif komanda == '2':
            listPredjala()
        elif komanda == '3':
            addGlavnaJela()
        elif komanda == '4':
            listGlavnaJela()
        elif komanda == '5':
            addDezerti()
        elif komanda == '6':
            listDezert()
        elif komanda == '7':
            addPica()
        elif komanda == '8':
            listPica()
        elif komanda == '9':
            Racun()
        elif komanda == '10':
            Odnos()
        elif komanda == '11':
            addRadnika()
    print( "Kasa je zatvorena.")
    
def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', 'X'):
        print( "\nUneli ste pogresnu komandu.\n")
        printMenu()
        command = input(">> ")
    return command.upper()

    
def printMenu():
    print( "\nIzaberite opciju:")
    print( "  1 - dodavanje novog predjela")
    print( "  2 - lista predjela")
    print( "  3 - dodavanje novog glavnog jela")
    print( "  4 - lista glavnog jela")
    print( "  5 - dodavanje novog dezerta ")
    print( "  6 - lista dezerta")
    print( "  7 - dodavanje novog pica")
    print( "  8 - lista pica")
    print( "  9 - racun")
    print( "  10 - odnos cena")
    print( "  11 - dodavanje radnika")
    print( "  x - Zatvori kasu")
    
def login():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return Radnici.login(username, password)

def addRadnika():
    print( " Upis novog radnika\n")
    rad = {}
    rad['ime'] = input("Unesite ime >> ")
    rad['prezime'] = input("Unesite prezime >> ")
    rad['username'] = input("Unesite username >> ")
    rad['password'] = input("Unesite password >> ")
    Radnici.addRadnika(rad)
    Radnici.saveRadnika()

def addPredjela():
    print( " Upis novog predjela\n")
    pred = {}
    pred['sifra'] = input("Unesite sifru >> ")
    pred['ime'] = input("Unesite ime >> ")
    pred['opis'] = input("Unesite opis >> ")
    pred['cena'] = input("Unesite cenu >> ")
    Predjelo.addPredjelo(pred)
    Predjelo.savePredjelo()

def listPredjala():
    print(Predjelo.formatHeader())
    print(Predjelo.formatAllPredjela())
    
def addGlavnaJela():
    print( "Upis novog predjela\n")
    glavno = {}
    glavno['sifra'] = input("Unesite sifru >> ")
    glavno['ime'] = input("Unesite ime >> ")
    glavno['opis'] = input("Unesite opis >> ")
    glavno['cena'] = input("Unesite cenu >> ")
    GlavnoJelo.addGlavnoJelo(glavno)
    GlavnoJelo.saveGlavnoJelo()

def listGlavnaJela():
    print(GlavnoJelo.formatHeader())
    print(GlavnoJelo.formatAllGlavnaJela())
    
def addDezerti():
    print( "Upis novog predjela\n")
    dez = {}
    dez['sifra'] = input("Unesite sifru >> ")
    dez['ime'] = input("Unesite ime >> ")
    dez['opis'] = input("Unesite opis >> ")
    dez['cena'] = input("Unesite cenu >> ")
    Dezert.addDezerti(dez)
    Dezert.saveDezert()

def listDezert():
    print(Dezert.formatHeader())
    print(Dezert.formatAllDezerti())
    
def addPica():
    print( "Upis novog predjela\n")
    pic = {}
    pic['sifra'] = input("Unesite sifru >> ")
    pic['ime'] = input("Unesite ime >> ")
    pic['opis'] = input("Unesite opis >> ")
    pic['cena'] = input("Unesite cenu >> ")
    Pice.addPice(pic)
    Pice.savePice()

def listPica():
    print(Pice.formatHeader())
    print(Pice.formatAllPica())

def menuracun():
    printMenuracun()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', 'X'):
        print( "\nUneli ste pogresnu komandu.\n")
        printMenuracun()
        command = input(">> ")
    return command.upper()
    
def printMenuracun():
    print( "\nIzaberite opciju:")
    print( "  1 - izaberi predjelo")
    print( "  2 - izaberi glavno jelo")
    print( "  3 - izaberi dezert")
    print( "  4 - izaberi pice")
    print( "  x - naplati ")
    
def findPredjelo():
    sifra = input("Unesite sifru: ")
    s = Predjelo.findPredjelo(sifra)
    while s == None:
        print("Nije pronadjeno predjelo sa tom sifrom.")
        sifra = input("Unesite sifru: ")
        s = Predjelo.findPredjelo(sifra)
    return s
    
def findGlavnoJelo():
    sifra = input("Unesite sifru: ")
    s = GlavnoJelo.findGlavnoJelo(sifra)
    while s == None:
        print("Nije pronadjeno glavno jelo sa tom sifrom.")
        sifra = input("Unesite sifru: ")
        s = GlavnoJelo.findGlavnoJelo(sifra)
    return s
    

def findDezert():
    sifra = input("Unesite sifru: ")
    s = Dezert.findDezert(sifra)
    while s == None:
        print("Nije pronadjen dezert sa tom sifrom.")
        sifra = input("Unesite sifru: ")
        s = Dezert.findDezert(sifra)
    return s
   

def findPice():
    sifra = input("Unesite sifru: ")
    s = Pice.findPice(sifra)
    while s == None:
        print("Nije pronadjeno pice sa tom sifrom.")
        sifra = input("Unesite sifru: ")
        s = Pice.findPice(sifra)
    return s
    
def Racun():
    suma = 0
    komandar = '0'
    while komandar != 'X':
        komandar = menuracun()
        if komandar == '1':
            suma=suma + int(findPredjelo())
            print("Vas trnutni racun je:",suma)
        elif komandar == '2':
            suma=suma + int(findGlavnoJelo())
            print("Vas trnutni racun je:",suma)
        elif komandar == '3':
            suma=suma + int(findDezert())
            print("Vas trnutni racun je:",suma)
        elif komandar == '4':
           suma=suma + int(findPice())
           print("Vas trnutni racun je:",suma)
    print("Vas racun je:", suma)
    placeno = 0
    placeno += int(input("Unesite sumu: ")) 
    while suma>int(placeno):
        print("Niste uneli dovoljno novca,unesite jos!")
        placeno += int(input("Unesite sumu: "))
    print("Vas kusur je ",int(placeno)-suma)
    
def printMenuodnos():
    print( "\nIzaberite odnos cena:")
    print( "  1 - izaberi predjelo")
    print( "  2 - izaberi glavno jelo")
    print( "  3 - izaberi dezert")
    print( "  4 - izaberi pice")
    print( "  X - vrati se u glavni meni ")
    
def menuodnos():
    printMenuodnos()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4', 'X'):
        print( "\nUneli ste pogresnu komandu.\n")
        printMenuodnos()
        command = input(">> ")
    return command.upper()

def odnosCenaP():
        predjela=Predjelo.findPredjela()
        cena = []
        ime = []
        for i in predjela:
            cena.append(int(i['cena']))
            ime.append(i['ime'])
        cena.sort()
        plt.xlabel('ime')
        plt.ylabel('cena')
        plt.ylim(ymin=150, ymax=900)
        plt.xticks(rotation=90)
        plt.bar(ime, cena)
        plt.show()
        
def odnosCenaG():
        glavna=GlavnoJelo.findGlavnaJela()
        cena = []
        ime = []
        for i in glavna:
            cena.append(int(i['cena']))
            ime.append(i['ime'])
        cena.sort()
        plt.xlabel('ime')
        plt.ylabel('cena')
        plt.ylim(ymin=500, ymax=2000)
        plt.xticks(rotation=90)
        plt.bar(ime, cena)
        plt.show()
        
def odnosCenaD():
        dezerti=Dezert.findDezerte()
        cena = []
        ime = []
        for i in dezerti:
            cena.append(int(i['cena']))
            ime.append(i['ime'])
        cena.sort()
        plt.xlabel('ime')
        plt.ylabel('cena')
        plt.ylim(ymin=60, ymax=400)
        plt.xticks(rotation=90)
        plt.bar(ime, cena)
        plt.show()
def odnosCenaPica():
        pica=Pice.findPica()
        cena = []
        ime = []
        for i in pica:
            cena.append(int(i['cena']))
            ime.append(i['ime'])
        cena.sort()
        plt.xlabel('ime')
        plt.ylabel('cena')
        plt.ylim(ymin=60, ymax=300)
        plt.xticks(rotation=90)
        plt.bar(ime, cena)
        plt.show()
def Odnos():
    komandar = '0'
    while komandar != 'X':
        komandar = menuodnos()
        if komandar == '1':
            odnosCenaP()
        elif komandar == '2':
            odnosCenaG()
        elif komandar == '3':
            odnosCenaD()
        elif komandar == '4':
          odnosCenaPica()
        
            
print(__name__)    
if __name__ == '__main__':
    main()