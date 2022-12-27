#-------------------------------------T O   D O---------------------------------------------------#
# 1.) Zadávání názvu pro každej router -> přidat do části pro výpočet vzdálenosti
# 2.) Funkce pro hledání sousedů -> if distance < x přidej souseda do neighbours
# 3.) 
#
#
#
#
#
#
#
#
import math
#-------------------------------Z A D Á N Í   R O U T E R Ů---------------------------------------#
#VÝCHOZÍ PROMĚNNÁ PRO OPAKOVÁNÍ CYKLU PRO VÝPOČET VZDÁLENOSTI
opakovani = int(0)
#VÝCHOZÍ PROMĚNNÁ PRO VZDÁLENOST
dst = float(0)
#Definice souřadnic výchozího routeru
xprev = int(0)
yprev = int(0)
#OSA X Router 1 (výchozí = 0, rozsah 1 - 100)
xprev = int(input('Zadej umístění výchozího Routeru na ose X: '))
#OSA Y Router 1 (výchozí = 0, rozsah 1 - 100)
yprev = int(input('Zadej umístění výchozího Routeru na ose Y: '))
#PROMĚNNÁ MNOŽSTVÍ ROUTERŮ 
routeramount = int(input('Zadej množství dalších routerů v cestě včetně cílového: '))
#Cyklus pro zadání dalších routerů
while opakovani < routeramount:
    opakovani += 1
    #OSA X Router 1 (výchozí = 0, rozsah 1 - 100)
    xnew = int(input(f"Zadej umístění Routeru {opakovani} na ose X: "))
    #OSA Y Router 1 (výchozí = 0, rozsah 1 - 100)
    ynew = int(input(f"Zadej umístění Routeru {opakovani} na ose Y: "))
    dst = dst + math.sqrt(((abs(xnew - xprev)) ** 2) + (((abs(ynew - yprev)) ** 2)))
    xprev = xnew
    yprev = ynew
print ('Délka přímé cesty mezi zadanými', routeramount + 1,'routery je: ',dst,'metrů')
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
hop = routeramount + 1
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
print ('Ztrátovost packetů = ', los,'%')
print ('Útlum = ', nsg,'%')
print ('Rychlost přenosu = ', rsp,'kbps')
print ('Rychlost přenosu = ', rsp / 8000,'MB/s')
print ('Latence = ', lat,'ms')