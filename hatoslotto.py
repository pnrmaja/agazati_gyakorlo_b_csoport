from huzott import Huzott

def feladat3():
    print("III/A, B:")
    with open("huzasok.txt",'r',encoding='utf-8') as file:
        next(file)
        huzott_lista:list[Huzott]=[]
        for x in file:
            huzott_sor:list[str]=x.split("@")
            huzott:Huzott=Huzott(int(huzott_sor[0]),int(huzott_sor[1]),int(huzott_sor[2]),int(huzott_sor[3]))
            huzott_lista.append(huzott)
    print(f"A húzások száma: {len(huzott_lista)}")
    return huzott_lista

def feladat_3c(huzott_lista:list[Huzott]):
    osszeg:float=0
    db:int=0
    

    for x in huzott_lista:
        if x.het == 43:
            osszeg+= x.szam
            db+=1
    
    atlag:float=osszeg/db
    print(f"III/C:")
    print(f"A 43. héten húzott számok átlaga: {atlag:.2f}")

def feladat_3d(huzott_lista:list[Huzott]):
    legnagyobb:Huzott=huzott_lista[0]

    for x in huzott_lista:
        if x.szam > legnagyobb.szam:
            legnagyobb=x
    print(f"Az első legnagyobb kihúzott szám értéke: {legnagyobb}")
    




