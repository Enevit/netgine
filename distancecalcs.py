import math
###################################################################################################
# DEFINICE PROMĚNNÝCH #
###################################################################################################
#-------------------------------------------------------------------------------------------------#
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
#Cyklus
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