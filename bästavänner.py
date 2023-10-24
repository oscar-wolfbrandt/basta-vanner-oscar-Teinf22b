"""
Detta är en lista som man kan läga in saker, man kan även redigera och ta bort.
__author__  = Oscar Schmerer Wolfbrandt
__version__ = 1.0.0
__email__   = oscar.schmererwolfbrandt@elev.ga.ntig.se
"""

import os
from colors import bcolors
loop = True
list = []
os.system("cls")

while loop == True:
    go = True
    go2 = True
    tag = False
    fel1 = False
    #meny
    print(bcolors.CYAN+"-----------------------------------------------------------------------\n                          Välkomen till listan\n\n                Skriv något för att läga till det \n                skriv # och ett nummer (t.ex #1) för att ändra / ta bort\n                Tryck enter eller q för att gå utt\n-----------------------------------------------------------------------\n"+ bcolors.WHITE+"du har",len(list),"saker i listan")
    if len(list) == 0:
        print("det fins inga saker i din lista")

    #skriver utt listan 
    for x in range(0 , int(len(list))):
        print(x+1,")",list[x])

    #tar in namn 
    do = input(bcolors.CYAN+"----------------------------------------------------------------------- \n"+bcolors.WHITE+":")

    #quit funktion och tar bort #
    try:
        if do == "":
            break
        elif do == "q":
            break
        elif do == "Q":
            break
        if "#" == do[0]:
            do = do.replace("#","")    
            tag = True
            go2 = True
        elif "#" not in do: 
            os.system("cls")
            list.append(do)
            go2 = False
    
        #ändra, ta bort och lägg till        
        if do.isdigit:    
            try:
                if go2 == True:

                    #chekar om användares nummer är giltigt genom att kola om nummret finns i listan och om nummret är posetivt 
                    if int(do) > len(list):
                        os.system("cls")
                        print(bcolors.RED+"nummret finns inte i listan"+bcolors.WHITE)
                        go = False
                    elif int(do) < len(list) + 1:
                        go = True
                    if int(do) < 0:
                        go = False
                        os.system("cls")
                        print(bcolors.RED+"Skriv ett posetivt tal"+bcolors.WHITE)
                    elif int(do) > 0:
                        go = True

                        #funtion för att ändra eller ta bort via anvendarens input 
                        for l in range(0,len(list) + 1):
                            if int(do) == l:
                                do2 = input("Vill du ta bort("+bcolors.GREEN+"enter"+bcolors.WHITE+") eller ändra("+bcolors.GREEN+"skriv något"+bcolors.WHITE+"):")
                                if do2 == "":
                                    list.pop(int(do) - 1)
                                    os.system("cls")
                                elif do2.isalpha:
                                    list.insert(int(do) - 1 ,do2)
                                    list.pop(int(do))
                                    os.system("cls")
            #läger till ord 
            except:
                if tag == True:
                    do = "#" + do
                list.append(do)
                os.system("cls")
    #fel funktin
    except:
        os.system("cls")
        print("något gick fel")
