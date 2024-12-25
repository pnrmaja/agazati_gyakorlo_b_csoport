class Huzott:
    def __init__(self,huzas:int,ev:int,het:int,szam:int):
        self.huzas = huzas
        self.ev = ev
        self.het = het
        self.szam = szam

    def __str__(self):
        return f"{self.szam}, {self.ev}-ben, a {self.het}. héten húzták ki, ez volt a {self.huzas}. húzás."
        