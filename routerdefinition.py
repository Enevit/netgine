import json
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plot
mpl.rcParams["font.size"] = 30
plot.style.use('default')
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
    print('\n#------------- H L A V N Í   M E N U -------------#')
    print('1.) Vytvoření routeru') # Vyzve k zadání názvu routeru a jeho souřadnic X a Y - následně všechny tři hodnoty uloží do dictionary routerlist
    print('2.) Najít sousedy') # Porovná souřadnice dvou vybraných routerů - pokud mají rozdíly souřadnic na obou osách menší než 100 přidá druhý router do dictionary neighbours
    print('3.) Vzdálenost mezi routery') # Vyzve k zadání dvou routerů, porovná jejich souřadnice a výpiše vzdálenost vzdušnou čarou
    print('4.) Délka cesty') # Vyzve k zadání routerů jak jdou po sobě - během zadávání počítá cestu trasy a vypisuje vzdálenost vzdušnou čarou a hodnoty spojení
    print('5.) Výpis všech routerů') # Vypíše všechny routery z dictionary routerlist a jejich počet
    print('6.) Souřadnice konkrétního routeru') # Vyzve k zadání routeru a vrátí jeho hodnoty z dictionary routerlist
    vyber = int(input('\nVyber možnost: '))
    print('\n')
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
        opakovani = int(0)
        #Množství routerů (routeramount) = počet hodnot v globálním arrayi routerlist / 3. Používá se pro určení počtu opakování while cyklu
        pocetrouteru = int(len(routerlist))
        #Volba routeru (routerchoice) je integer použitý k výběru konkrétní hodnoty z globálního arraye routers
        routerchoice = input('Zadej název routeru pro který chceš najít sousedy: ')
        xdef = routerlist[routerchoice]['coordx']
        ydef = routerlist[routerchoice]['coordy']
        for routername, routerinfo in routerlist.items():
            xnew = routerinfo['coordx']
            ynew = routerinfo['coordy']
            if routerinfo['routername'] == routerchoice:
                print('\n')
            elif abs((xdef) - (xnew)) < 100 and abs((ydef) - (ynew)) < 100:
                print(routerinfo['routername'],'je sousedem routeru', routerchoice)
                print('\n')
            else:
                print(routerinfo['routername'],'neni sousedem routeru', routerchoice)
                print('\n')
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
        #-------------------Cyklus pro zadání dalších routerů------------------------#
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
        #---------------------------------------------------------------------------#
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
        pocetrouteru = int(len(routerlist))
        print('#------------- V Ý P I S   R O U T E R Ů -------------#')
        #cyklus iterující skrz hlavní slovník, routername a routerinfo jsou random proměnný, který takhle v páru způsobují vypisování tuples (párů key:value) ze slovníku
        for routername, routerinfo in routerlist.items():
            print('\n')
            opakovani = int(0)
            for key in routerinfo:
                opakovani += 1
                #vytiskne "key : value[key]" za každej key v hlavním dictionary
                print(key + ':', routerinfo[key])
                if ((opakovani % 3) - 1) == 0:
                    routername = routerinfo[key]
                    print(routername)
                elif ((opakovani % 3) - 2) == 0:
                    #proměnná kam se zapíše hodnota X
                    xdef = routerinfo[key]
                    print(xdef)
                elif (opakovani % 3) == 0:    
                    #proměnná kam se zapíše hodnota Y
                    ydef = routerinfo[key]
                    print(ydef)                
            # -----------VYKRESLOVACÍ SOUČÁST-----------#
            colors = 10
            sizes = 10
            #fig, ax = plot.subplots()
            #fig = plot.figure()
            #ax = fig.add_subplot()

            plot.scatter(xdef, ydef, s=sizes, c=colors, vmin=0, vmax=100)
            #Nastavení chování zobrazených os - xlim je jejich rozsah, xticks je rozsah popisu číslování os (proč by tohle někdo chtěl jako parametr?)
            #plot.set(xlim=(0, 100), xticks=np.arange(0, 100),
                   #ylim=(0, 100), yticks=np.arange(0, 100))
            plot.title('Výpis všech routerů')
            plot.text(xdef, ydef, routername)
        plot.xlim(0, 100)
        plot.ylim(0, 100)
        plot.show()
        print('\nCelkový počet routerů je:', pocetrouteru,'\n')

        
        print('#-----------------------------------------------------#\n')
        
    #----------------------------------------------------------------------------------------------------------Vypsání konkrétního routeru--------------------------------------------------------------------------------------------------------------------------#
    elif vyber == 6:
        print('#-- V Ý P I S   K O N K R É T N Í H O   R O U T E R U --#')
        routerchoice = input('Zadej název routeru: ')
        xdef = routerlist[routerchoice]['coordx']
        ydef = routerlist[routerchoice]['coordy']
        print('\n',routerchoice,'je na souřadnicích X:',xdef,'Y:',ydef)
        #-----------VYKRESLOVACÍ SOUČÁST-----------#
        colors = 10
        sizes = 10
        fig, ax = plot.subplots()

        ax.scatter(xdef, ydef, s=sizes, c=colors, vmin=0, vmax=100)
        #Nastavení chování zobrazených os - xlim je jejich rozsah, xticks je rozsah popisu číslování os (proč by tohle někdo chtěl jako parametr?)
        ax.set(xlim=(0, 100), xticks=np.arange(0, 100),
               ylim=(0, 100), yticks=np.arange(0, 100), label = (routerchoice))
        plot.title('Výpis konkrétního routeru')
        plot.text(xdef, ydef, routerchoice)
        plot.show()

        #print (routerlist[routerchoice])
        print('#-----------------------------------------------------#\n')
    #
    else:
        print('Neplatná volba')
        print(' ')