import json
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plot
mpl.rcParams["font.size"] = 30
plot.style.use('default')
#----------------- L I S T S -------------------#
routerlist = {}
neighbours = []
#
#--------------------------------------------------- M E N U --------------------------------------------------------#
#
menu = True
while menu:
    print('\n#------------- M A I N   M E N U -------------#')
    print('1.) Create router') # Prompts for router name and it's X and Y coordinates, saving these values into routerlist dictionary
    print('2.) Find neighbours') # Prompts for router name and iterates through routerlist dictionary to compare coordinates of other routers, printing whether they are neighbours based on the difference in distance (<100 = neighbour)
    print('3.) Distance between routers') # Prompts for two router names, compares their coordinates and prints the distance between them
    print('4.) Path distance') # Prompts for amount of routers in path and their names - calculates the accumulated distance and prints connection values based on it
    print('5.) List all routers') # Prints all routers from dictionary routerlist, their amount and shows them on a simple 2D grid
    print('6.) Specific router coordinates') # Prompts for router name and prints its coordinates, displaying the router on a simple 2D grid
    choice = int(input('\nChoose an option: '))
    print('\n')
    #---------------------------------------- Creation of a router with name and coordinates ------------------------------------#
    if choice == 1:
        routername = str(input('Input router name: '))
        coordx = int(input(f"Input the coordinates of {routername} on axis X: "))
        coordy = int(input(f"Input the coordinates of {routername} on axis Y: "))
        routerlist[routername] = {'routername': routername, 'coordx': coordx, 'coordy': coordy}
        print('Router with the name',routername,'was created on coordinates X:',coordx,'Y:',coordy)
    #---------------------------------------------------- Looking for neighbours ------------------------------------------------#
    elif choice == 2:
        iteration = int(0)
        routerchoice = input('Input name of the router for which you want to find neighbours: ')
        xdef = routerlist[routerchoice]['coordx']
        ydef = routerlist[routerchoice]['coordy']
        for routername, routerinfo in routerlist.items():
            xnew = routerinfo['coordx']
            ynew = routerinfo['coordy']
            if routerinfo['routername'] == routerchoice:
                print('\n')
            elif abs((xdef) - (xnew)) < 100 and abs((ydef) - (ynew)) < 100:
                print(routerinfo['routername'],'IS a neighbour of', routerchoice)
                print('\n')
            else:
                print(routerinfo['routername'],'is NOT a neighbour of', routerchoice)
                print('\n')
    #---------------------------------------- Path distance and connection values calculation -----------------------------------#
    elif choice == 4:
        iteration = int(0)
        #Default variable for distance
        dst = float(0)
        #Variable for amount of routers in calculated path
        routeramount = int(input('\nInput the amount of routers in the calculated route: '))
        firstrouter = input('Input the name of the next router: ')
        xdef = routerlist[firstrouter]['coordx']
        ydef = routerlist[firstrouter]['coordy']
        #-------------------Cycle for inputting consecutive routers------------------------#
        while iteration < (routeramount - 1):
            iteration += 1
            nextrouter = input(f"Input the name of the next router (number {iteration}): ")
            xnext = routerlist[nextrouter]['coordx']
            ynext = routerlist[nextrouter]['coordy']
            dst = dst + math.sqrt(((abs(xdef - xnext)) ** 2) + (((abs(ydef - ynext)) ** 2)))
            xdef = xnext
            ydef = ynext
        print ('\nLength of direct path between the selected', routeramount,'routers is: ',dst,'meters\n')
        #-----------------------------V A L U E S   C A L C U L A T I O N---------------------------------#
        #
        #VARIABLE FOR DISTANCE IN METERS (default = 25, range 1 - 250)
        lng = dst
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE FOR AMOUNT OF HOPS (default = 0, range = 0 - 1 000)
        hop = routeramount - 1
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE FOR AMOUNT OF RICOCHETS (default = 0, range 1 - 50)
        ric = int(input('Input the ricochet amount (range 0 - 1 000) (default value = 0): '))
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE FOR BOTTLENECK SPEED (default = 100000, range 0 - 500000)
        fre = int(input('Input the bottleneck speed (range 0 - 500 000) (default value = 100 000): '))
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE FOR SPECIFIC SPEED OF ONE-WAY UDP TRANSMISSION (default = 100 000, range 0 - 500 000)
        spd = int(100000)
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE FOR LATENCY (default = 1, range = 1 - 100 000)
        #Each hop = +20 latence
        lat = int(1) + (hop * 20)
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE FOR SIGNAL DAMPING (default = 1, range 1 - 100)
        #Each 1 ricochet = +4 damping
        #Each 10 meters of distance = +1 damping
        nsg = int(1)
        if hop >= 0:
            nsg = nsg + (ric * 4) + (lng / 10)
        else:
            nsg = nsg
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE FOR PACKET LOSS% (default = 0, range 0 - 100)
        #Above 50% damping = each +1% of damping causes +2% packet loss
        los = int(0)
        if nsg > 50:
            los = los + ((nsg - 50) * 2)
        else:
            los = los
        #-------------------------------------------------------------------------------------------------#
        #VARIABLE OF ROUTER SPEED IN KBIT/S (default = 1 000, range 0 - 100 000)
        #The slowest speed of any router in the path = the default speed of transmission
        #Each +1% damping = -1% speed
        #Each +1% of packet loss = -1% of transmission speed
        rsp = int(100000)
        if fre < 100000:
            rsp = fre * (((nsg - 100) * (-1) / 100))  * (((los - 100) * (-1) / 100))
        else:
            rsp = rsp * (((nsg - 100) * (-1) / 100))  * (((los - 100) * (-1) / 100))
        #-------------------------------------------------------------------------------------------------#
        #Results:
        print ('\nPacket loss = ', los,'%')
        print ('Signal damping = ', nsg,'%')
        print ('Transmission speed = ', rsp,'kbps')
        print ('Transmission speed = ', rsp / 8000,'MB/s')
        print ('Latency = ', lat,'ms\n')
    #--------------------------------------------------- Listing all routers ----------------------------------------------------#
    elif choice == 5:
        routeramount = int(len(routerlist))
        print('#------------- L I S T I N G   R O U T E R S -------------#')
        #Cycle iterating through the routerlist dictionary to obtain (key:value) pairs
        for routername, routerinfo in routerlist.items():
            print('\n')
            iteration = int(0)
            for key in routerinfo:
                iteration += 1
                #prints "key : value[key]" for every key in dictionary
                print(key + ':', routerinfo[key])
                if ((iteration % 3) - 1) == 0:
                    routername = routerinfo[key]
                    print(routername)
                elif ((iteration % 3) - 2) == 0:
                    #variable for X axis value
                    xdef = routerinfo[key]
                    print(xdef)
                elif (iteration % 3) == 0:    
                    #variable for Y axis value
                    ydef = routerinfo[key]
                    print(ydef)                
            # -----------"RENDERING" PIECE-----------#
            colors = 10
            sizes = 10
            plot.scatter(xdef, ydef, s=sizes, c=colors, vmin=0, vmax=100)
            plot.title('List of all routers')
            plot.text(xdef, ydef, routername)
        plot.xlim(0, 100)
        plot.ylim(0, 100)
        plot.show()
        print('\nTotal amount of routers is:', routeramount,'\n')
        print('#-----------------------------------------------------#\n')
        
    #-------------------------------------------------- Printing specific router ------------------------------------------------#
    elif choice == 6:
        print('#-- L I S T I N G   S P E C I F I C   R O U T E R --#')
        routerchoice = input('Input router name: ')
        xdef = routerlist[routerchoice]['coordx']
        ydef = routerlist[routerchoice]['coordy']
        print('\n',routerchoice,'is on coordinates X:',xdef,'Y:',ydef)
        #-----------"RENDERING" PIECE-----------#
        colors = 10
        sizes = 10
        fig, ax = plot.subplots()
        ax.scatter(xdef, ydef, s=sizes, c=colors, vmin=0, vmax=100)
        plot.title('Listing of specific router')
        plot.text(xdef, ydef, routerchoice)
        plot.show()
        print('#-----------------------------------------------------#\n')
    #
    else:
        print('Invalid choice')
        print(' ')