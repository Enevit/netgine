import json
import math
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
    print('1.) Vytvoření routeru') # Vyzve k zadání názvu routeru a jeho souřadnic X a Y - následně všechny tři hodnoty uloží do dictionary routerlist
    print('2.) Najít sousedy') # Porovná souřadnice dvou vybraných routerů - pokud mají rozdíly souřadnic na obou osách menší než 100 přidá druhý router do dictionary neighbours
    print('3.) Vzdálenost mezi routery') # Vyzve k zadání dvou routerů, porovná jejich souřadnice a výpiše vzdálenost vzdušnou čarou
    print('4.) Délka cesty') # Vyzve k zadání routerů jak jdou po sobě - během zadávání počítá cestu trasy a vypisuje vzdálenost vzdušnou čarou a hodnoty spojení
    print('5.) Výpis všech routerů') # Vypíše všechny routery z dictionary routerlist a jejich počet
    print('6.) Souřadnice konkrétního routeru') # Vyzve k zadání routeru a vrátí jeho hodnoty z dictionary routerlist
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
    #------------------------------------------------------------------------------------------------------ Výpočet délky cesty a hodnot spojení -------------------------------------------------------------------------------------------------------------------#
    elif vyber == 4:
        #VÝCHOZÍ PROMĚNNÁ PRO OPAKOVÁNÍ CYKLU PRO VÝPOČET VZDÁLENOSTI
        opakovani = int(0)
        #VÝCHOZÍ PROMĚNNÁ PRO VZDÁLENOST
        dst = float(0)
        #PROMĚNNÁ MNOŽSTVÍ ROUTERŮ 
        routeramount = int(input('\nZadej množství routerů v počítané cestě: '))
        firstrouter = input('Zadej název výchozího routeru: ')
        xdef = routerlist[firstrouter]['coordx']
        ydef = routerlist[firstrouter]['coordy']
        #Cyklus pro zadání dalších routerů
        while opakovani < (routeramount - 1):
            opakovani += 1
            #OSA X Router 1 (výchozí = 0, rozsah 1 - 100)
            nextrouter = input(f"Zadej název dalšího Routeru (číslo {opakovani}): ")
            xnext = routerlist[nextrouter]['coordx']
            ynext = routerlist[nextrouter]['coordy']
            #OSA Y Router 1 (výchozí = 0, rozsah 1 - 100)
            #ynew = int(input(f"Zadej umístění Routeru {opakovani} na ose Y: "))
            dst = dst + math.sqrt(((abs(xdef - xnext)) ** 2) + (((abs(ydef - ynext)) ** 2)))
            xdef = xnext
            ydef = ynext
        print ('\nDélka přímé cesty mezi zadanými', routeramount,'routery je: ',dst,'metrů\n')
        #
        #
        #
        #
        #
        #-----------------------------V Ý P O Č E T   H O D N O T-----------------------------------------#
        #PROMĚNNÁ ROUTERU (výchozí = router1)
        rtr = 'router1'
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ VZDÁLENOSTI V METRECH (výchozí = 25, rozsah 1 - 250)
        lng = dst
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ POČTU HOPŮ (výchozí = 0, rozsah = 0 - 1 000)
        hop = routeramount - 1
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ POČTU ODRAZŮ (výchozí = 0, rozsah 1 - 50)
        ric = int(input('Zadej počet odrazů od objektů (rozsah 0 - 1 000) (výchozí hodnota = 0): '))
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ BOTTLENECK RYCHLOSTI (výchozí = 100000, rozsah 0 - 500000)
        fre = int(input('Zadej bottleneck rychlost (rozsah 0 - 500 000) (výchozí hodnota = 100 000): '))
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ KONKRÉTNÍ RYCHLOSTI PŘI UDP přenosu (výchozí = 100 000, rozsah 0 - 500 000)
        spd = int(100000)
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ LATENCE (výchozí = 1, rozsah = 1 - 100 000)
        #Každý hop = +20 latence
        lat = int(1) + (hop * 20)
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ ÚTLUMU (výchozí = 1, rozsah 1 - 100)
        #Každý 1 odraz = +4 útlum
        #Každých 10 metrů vzdálenosti = +1 útlum
        nsg = int(1)
        if hop >= 0:
            nsg = nsg + (ric * 4) + (lng / 10)
        else:
            nsg = nsg
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ ZTRÁTOVOSTI PACKETŮ (výchozí = 0, rozsah 0 - 100)
        #Nad 50% útlumu = každý +1% útlumu +2% ztrátovosti
        los = int(0)
        if nsg > 50:
            los = los + ((nsg - 50) * 2)
        else:
            los = los
        #-------------------------------------------------------------------------------------------------#
        #PROMĚNNÁ RYCHLOSTI PŘENOSU ROUTERU V KBIT/S (výchozí = 1 000, rozsah 0 - 100 000)
        #Nejnižší rychlost routeru po cestě = základní rychlost přenosu
        #Každý +1% útlumu = -1% rychlosti
        #Každé +1% ztrátovosti packetů = -1% rychlosti přenosu
        rsp = int(100000)
        if fre < 100000:
            rsp = fre * (((nsg - 100) * (-1) / 100))  * (((los - 100) * (-1) / 100))
        else:
            rsp = rsp * (((nsg - 100) * (-1) / 100))  * (((los - 100) * (-1) / 100))
        #-------------------------------------------------------------------------------------------------#
        #Výpis:
        print ('\nZtrátovost packetů = ', los,'%')
        print ('Útlum = ', nsg,'%')
        print ('Rychlost přenosu = ', rsp,'kbps')
        print ('Rychlost přenosu = ', rsp / 8000,'MB/s')
        print ('Latence = ', lat,'ms\n')
    #-------------------------------------------------------------------------------------------------------- Vypsání všech zadaných routerů -----------------------------------------------------------------------------------------------------------------------#
    elif vyber == 5:
        vypisrouteru = json.dumps(routerlist,sort_keys=True, indent=4)
        print('\nSeznam routerů: \n\n',vypisrouteru,'\n')
        pocetrouteru = int(len(routerlist))
        print('Celkový počet routerů je:', pocetrouteru,'\n')
    #----------------------------------------------------------------------------------------------------------Vypsání konkrétního routeru--------------------------------------------------------------------------------------------------------------------------#
    elif vyber == 6:
        routerchoice = input('Zadej nazev routeru: ')
        print (routerlist[routerchoice])
    #
    else:
        print('Neplatná volba')
        print(' ')