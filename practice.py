jmeno = "Patricie"
vek = 34

print(f"Jmenuji se {jmeno} a je mi {vek} let.")

###

jmeno = input("Zadej své jméno: ")
vek = input("Zadej svůj věk: ")

print(f"Jmenuji se {jmeno} a je mi {vek} let.")

###

jmeno = input("Zadej své jméno: ")
vek = input("Zadej svůj věk: ")

print(f"Jmenuji se {jmeno} a je mi {vek} let.")

vek = int(vek)
print(f"Za 5 let ti bude {vek + 5} let.")

###

jmeno = input("Zadej své jméno: ")
vek = int(input("Zadej svůj věk: "))

print(f"Jmenuji se {jmeno} a je mi {vek} let.")

if vek >= 18:
    print("Jsi dospělý/á.")
else:
    print("Je ti méně než 18 let.")

###

jmeno = input("Zadej své jméno: ")
vek = int(input("Zadej svůj věk: "))

print(f"Jmenuji se {jmeno} a je mi {vek} let.")

if vek <= 12:
    print("Jsi dítě.")
elif vek <= 17:
    print("Jsi teenager.")
elif vek <= 64:
    print("Jsi dospělý/á.")
else:
    print("Jsi senior.")

###

import random

tajne_cislo = random.randint(1, 10)
tip = 0

while tip != tajne_cislo:
    tip = int(input("Hádej číslo od 1 do 10: "))
        
if tip < tajne_cislo:
    print("Moc nízké!")
elif tip > tajne_cislo:
    print("Moc vysoké!")
else:
                                            print("Správně! 🎉")

###

import random

tajne_cislo = random.randint(1, 10)
tip = 0
pokusy = 0

while tip != tajne_cislo:
    tip = int(input("Hádej číslo od 1 do 10: "))
    pokusy += 1
            
if tip < tajne_cislo:
    print("Moc nízké!")
elif tip > tajne_cislo:
    print("Moc vysoké!")
else:
    print(f"Správně! 🎉 Uhodla jsi číslo za {pokusy} pokusů.")

###

import random

znaky = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

delka = int(input("Zadej délku hesla: "))

heslo = ""
for i in range(delka):
    heslo += random.choice(znaky)

print(f"Tvoje nové heslo je: {heslo}")

###

import random

# Možné sady znaků
pismena = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cisla = "0123456789"
specialy = "!@#$%^&*()"

# Uživatel si vybere úroveň složitosti
print("Vyber složitost hesla:")
print("1 - Jen písmena")
print("2 - Písmena a čísla")
print("3 - Písmena, čísla a speciální znaky")

volba = input("Tvoje volba (1/2/3): ")

# Podle volby nastavíme znaky
if volba == "1":
    znaky = pismena
elif volba == "2":
    znaky = pismena + cisla
else:
    znaky = pismena + cisla + specialy

# Uživatel zadá délku hesla
delka = int(input("Zadej délku hesla: "))

# Generování hesla
heslo = ""
for i in range(delka):
    heslo += random.choice(znaky)

print(f"Tvoje nové heslo je: {heslo}")

###

cislo1 = float(input("Zadej první číslo: "))
operace = input("Zadej operaci (+, -, *, /): ")
cislo2 = float(input("Zadej druhé číslo: "))

if operace == "+":
    vysledek = cislo1 + cislo2
elif operace == "-":
    vysledek = cislo1 - cislo2
elif operace == "*":
    vysledek = cislo1 * cislo2
elif operace == "/":
    if cislo2 != 0:
        vysledek = cislo1 / cislo2
    else:
        vysledek = "Nulou nelze dělit!"
else:
    vysledek = "Neznámá operace"

print("Výsledek:", vysledek)

###

while True:
    cislo1 = input("Zadej první číslo (nebo 'konec' pro ukončení): ")
            
    if cislo1.lower() == "konec":
        print("Program se ukončuje. 👋")
        break
                                    
    cislo1 = float(cislo1)
    operace = input("Zadej operaci (+, -, *, /): ")
    cislo2 = float(input("Zadej druhé číslo: "))

    if operace == "+":
        vysledek = cislo1 + cislo2
    elif operace == "-":
        vysledek = cislo1 - cislo2
    elif operace == "*":
        vysledek = cislo1 * cislo2
    elif operace == "/":
        if cislo2 != 0:
            vysledek = cislo1 / cislo2
        else:
            vysledek = "Nulou nelze dělit!"
    else:
        vysledek = "Neznámá operace"

    print("Výsledek:", vysledek)
    print("-" * 20)  # oddělovač