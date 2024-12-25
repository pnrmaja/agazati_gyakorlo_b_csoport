def feladat1():
    print("I/A, B:")
    het_napja:str=(input("Hét napja:"))
    ora_neve:str=(input("Óra neve:"))
    ertekeles:int =int(input("Értékelés(0-5):"))

    print("I/C:")

    if ertekeles < 0:
        print("Az értékelés nem lehet negatív!")
    elif ertekeles > 5:
        print("5 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")

        print(f"Összefoglaló: '{het_napja}', '{ora_neve}', {ertekeles} érték")