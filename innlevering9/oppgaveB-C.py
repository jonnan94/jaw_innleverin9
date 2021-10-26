# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:39:57 2021

@author: jonnan
"""



class millioner :
    def __init__(self, spørsmål, alt, svar1):
        self.alt = alt
        self.svar1 = svar1
        self.spørsmål = spørsmål
        
    
    def __str__(self):
        spørsmål = f"""{self.spørsmål}
        1. {self.alt[0]}
        2. {self.alt[1]}
        3. {self.alt[2]}"""
        return spørsmål
    
    
    def svar(self,svaret):
        if str(self.svar1) == str(svaret):
            print("stemme d")
        else:
            print("feil")


if __name__ in "__main__":
    spørsmål = "når åpnet norge opp etter corona?"
    alt = ["1945","2021","2032" ]
    svar = "2"
    

    test = millioner(spørsmål, alt, svar)
    print(str(test))
    svaret= input("svar: ")
    test.svar(svaret)
    
    spørsmål = "i hvilke måne har vi 17 mai?"
    alt = ["januar","mai","alle" ]
    svar = 3
    

    test = millioner(spørsmål, alt, svar)
    print(str(test))
    svaret= input("svar: ")
    test.svar(svaret)