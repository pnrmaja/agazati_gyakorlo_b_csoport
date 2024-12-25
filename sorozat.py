import random
def feladat2():
    print("II/A, B, C:")
    szamok_lista:list[int] =[]
    szamok_lista_str:list[str] = []

    for _ in range(8):

        veletlen_szam:int=int(random.randint(-100,859))
        szamok_lista.append(veletlen_szam)
        szamok_lista_str.append(str(veletlen_szam))
    print(";".join(szamok_lista_str))
    return szamok_lista


def tizzel_oszthatoak_szama(szamok_lista:list[int]):
    db:int = 0
    
    for x in szamok_lista:
       
        if x % 10 == 0:
            db += 1
    
    return db

def konzol_ir(db:int):
    print("II/D, E:")

    print(f"Tízzel osztható számok száma: {db}.")

def fajlba_ir(db:int):
    print("II/F:")
    with open("vegeredmeny.txt",'w',encoding='utf-8') as file:
            file.write(f"Tízzel osztható számok száma: {db}.")

