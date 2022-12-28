import json
#------------------------------------------------------------------------------------------------------------ D E F I N I C E   R O U T E R Ů ----------------------------------------------------------------------------------------------------------------------#
#
#
#
#------------------------------------------------------------------------------------------------------------- G L O B Á L N Í   L I S T Y -------------------------------------------------------------------------------------------------------------------------#
routerlist = {}
neighbours = []
#
#------------------------------------------------------------------------------------------------------------------------ M E N U ----------------------------------------------------------------------------------------------------------------------------------#
#
menu = True
while menu:
    print('Vyber si možnost: ')
    print('1.) Vytvoření routeru') # Vyzve k zadání názvu routeru a jeho souřadnic X a Y - následně všechny tři hodnoty uloží do arraye routers
    print('2.) Najít sousedy') # Porovná souřadnice všech existujících routerů v arrayi routers s vybraným routerem - routery, které mají rozdíly souřadnic na obou osách menší než 100 přidá do arraye neighbors a vypíše je
    print('3.) Vzdálenost mezi routery') # Vyzve k zadání dvou routerů, porovná jejich souřadnice a výpiše vzdálenost vzdušnou čarou
    print('4.) Délka cesty') # Vyzve k zadání routerů jak jdou po sobě - během zadávání počítá cestu trasy a vypisuje vzdálenost vzdušnou čarou a hodnoty spojení
    print('5.) Výpis všech routerů') # Vypíše všechny routery z arraye routers a jejich počet
    print('6.) Souřadnice konkrétního routeru') # Vyzve k zadání routeru a vrátí jeho hodnoty z arraye routers
    vyber = int(input('Vyber možnost: '))
    #-------------------------------------------------------------------------------------------------- Vytvoření routeru se zadáním názvu a souřadnic -------------------------------------------------------------------------------------------------------------#
    if vyber == 1:
        routername = str(input('Zadej název routeru: '))
        coordx = int(input(f"Zadej umístění {routername} na ose X: "))
        coordy = int(input(f"Zadej umístění {routername} na ose Y: "))
        routerlist[routername] = {'routername': routername, 'coordx': coordx, 'coordy': coordy}
        print('Router s názvem',routername,'byl vytvořen na souřadnicích X:',coordx,'Y:',coordy)
    #----------------------------------------------------------------------------------------------------------- Hledání sousedních routerů ------------------------------------------------------------------------------------------------------------------------#
    elif vyber == 2:
        #Proměnná pro opakovní cyklu
        opakovani = int(1)
        #Množství routerů (routeramount) = počet hodnot v globálním arrayi routerlist / 3. Používá se pro určení počtu opakování while cyklu
        pocetrouteru = int(len(routerlist))
        #Volba routeru (routerchoice) je integer použitý k výběru konkrétní hodnoty z globálního arraye routers
        routerchoicea = input('Zadej název prvního routeru: ')
        routerchoiceb = input('Zadej název druhého routeru: ')
        while opakovani == 1:
            # Pokud jsou obě souřadnice následujícího routeru v globálním arrayi routers blíž než 100, přidej tento následující router do globálního arraye neighbours
            routacoordx = routerlist[routerchoicea]['coordx']
            routbcoordx = routerlist[routerchoiceb]['coordx']
            routacoordy = routerlist[routerchoicea]['coordy']
            routbcoordy = routerlist[routerchoiceb]['coordy']
            if abs((routacoordx) - (routbcoordx)) < 100 and abs((routacoordy) - (routbcoordy)) < 100:
                print ('Router', routerlist[routerchoicea],' je sousedem routeru', routerlist[routerchoiceb])
                neighbours.append(routerchoiceb)
                opakovani += 1
            else:
                print ('Router', routerlist[routerchoicea],' neni sousedem routeru', routerlist[routerchoiceb])
                opakovani += 1
    #-------------------------------------------------------------------------------------------------------- Vypsání všech zadaných routerů -----------------------------------------------------------------------------------------------------------------------#
    elif vyber == 5:
        vypisrouteru = json.dumps(routerlist,sort_keys=True, indent=4)
        print(vypisrouteru)
        pocetrouteru = int(len(routerlist))
        print('Celkový počet routerů je: ', pocetrouteru)
    #----------------------------------------------------------------------------------------------------------Vypsání konkrétního routeru--------------------------------------------------------------------------------------------------------------------------#
    elif vyber == 6:
        routerchoice = input('Zadej nazev routeru: ')
        print (routerlist[routerchoice])
    #
    else:
        print('Neplatná volba')
        print(' ')