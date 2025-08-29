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

