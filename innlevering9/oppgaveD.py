# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:21:07 2021

@author: jonna
"""



        
class test :
    def __init__(self, spørsmål, alt, svar1):
        self.alt = alt
        self.svar1 = svar1
        self.spørsmål = spørsmål
 
    
    def __str__(self):
        spørsmål = f"{self.spørsmål}\n"
        for i in range(len(self.alt)):
            spørsmål += f"{i}. {self.alt[i]}\n"
        return spørsmål
    
    
    def svar(self,sp1):
        if self.svar1== int(sp1):
            return True
        else:
            return False
            
    def korrekt_svar_tekst(self):
        korrekte_svar = self.alt[self.svar1] 
        return f"korrekt svar er {korrekte_svar}\n"   
    
def les_fil():
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as txt_fil:
        spørs_liste = list()
        for linje in txt_fil:
            strippet = linje.split(":")
            svar1 = strippet[2].strip("[]\n").split(",")
            spørsmål1 = test(strippet[0], svar1, int(strippet[1] ))
            spørs_liste.append(spørsmål1) 
        return (spørs_liste)  


if __name__ in "__main__":
    sp1 = input("skriv inn navn:")
    sp2 = input("skriv inn navn:")    
    korrekte_svar = 0
    korrekte_svar2 = 0
    spørs_liste = les_fil()


    for sporsmalene in spørs_liste:
            print(str(sporsmalene))

            bruker1_svar = input(f"{sp1} svar: ")
            if sporsmalene.svar(bruker1_svar):
                print("Korrekt!")
                korrekte_svar += 1
            else:
                print("Feil!")
                print(f"Du har {korrekte_svar} riktige \
                      av {len(spørs_liste)} mulige.")

            bruker2_svar = input(f"{sp2} svar: ")
            if sporsmalene.svar(bruker2_svar):
                print("Korrekt!")
                korrekte_svar2 += 1
            else:
                print("Feil!")
                print(f"Du har {korrekte_svar} riktig \
                      av {len(spørs_liste)} mulige.")    
            print(sporsmalene.korrekt_svar_tekst())
