#------------------------------------------------------------------------------------------------------------ D E F I N I C E   R O U T E R Ů ----------------------------------------------------------------------------------------------------------------------#
#
#
#
#------------------------------------------------------------------------------------------------------------- G L O B Á L N Í   L I S T Y -------------------------------------------------------------------------------------------------------------------------#
routers = {}
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
        routeramount = int((len(routerlist))+1)
        routerlist['routerid'] = routeramount
        routername = str(input('Zadej název routeru: '))
        coordx = int(input(f"Zadej umístění {routername} na ose X: "))
        coordy = int(input(f"Zadej umístění {routername} na ose Y: "))
        routerlist['routers'] = {'routername': routername, 'coordx': coordx, 'coordy': coordy}
        print('Router s názvem',routername,'byl vytvořen na souřadnicích X:',coordx,'Y:',coordy)
        print(routerlist)
    #----------------------------------------------------------------------------------------------------------- Hledání sousedních routerů ------------------------------------------------------------------------------------------------------------------------#
    elif vyber == 2:
        #Proměnná pro opakovní cyklu
        opakovani = int(0)
        #Množství routerů (routeramount) = počet hodnot v globálním arrayi routerlist / 3. Používá se pro určení počtu opakování while cyklu
        routeramount = int((len(routerlist))/3)
        #Volba routeru (routerchoice) je integer použitý k výběru konkrétní hodnoty z globálního arraye routers
        routerchoice = int(input('Zadej cislo routeru: '))
        while opakovani <= (routeramount * 3):
            # Pokud jsou obě souřadnice následujícího routeru v globálním arrayi routers blíž než 100, přidej tento následující router do globálního arraye neighbours
            if abs(routers[routerchoice + ((opakovani + 4))] - routers[routerchoice + 1]) < 100 and abs(routers[routerchoice + (opakovani + 5)] - routers[routerchoice + 2]) < 100:
                print ('Router', routers[routerchoice + (opakovani * 3)],' je sousedem routeru', routers[routerchoice])
                neighbours.append(routerchoice)
                opakovani += 3
            else:
                print ('Router', routers[routerchoice + (opakovani * 3)],' neni sousedem routeru', routers[routerchoice])
                opakovani += 3
    #-------------------------------------------------------------------------------------------------------- Vypsání všech zadaných routerů -----------------------------------------------------------------------------------------------------------------------#
    elif vyber == 5:
        print (routerlist)
        #Množství routerů (routeramount) = počet hodnot v globálním arrayi routers / 3
        routeramount = int((len(routers))/3)
        print ('Počet routerů je: ',routeramount)
    #----------------------------------------------------------------------------------------------------------Vypsání konkrétního routeru--------------------------------------------------------------------------------------------------------------------------#
    elif vyber == 6:
        routerchoice = int(input('Zadej cislo routeru: '))
        routernumber = int(0)
        #Když je vybrán router s číslem 1, vrať hodnotu 0 z globálního arraye routers + souřadnice, jinak vyber příslušnou hodnotu z globálního arraye routers + souřadnice
        if routerchoice == 1:
            routernumber = routernumber
        else:
            routernumber = (routerchoice - 1) * 3
        print (routers[routernumber],routers[routernumber + 1],routers[routernumber + 2])
    #
    else:
        print('Neplatná volba')
        print(' ')