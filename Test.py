import time

menus = []

from Test2 import menu
menus.append( menu )

from Test3 import menu
menus.append( menu )

def getInterface () :
        print('q for quit')
        i = input('')
        if i == 'q' or i == 'Q':
            exit()
        try:
            i = int(i) - 1
            program = menus[i]['programm']
            program()
        except:
            getInterface ()

def createMenu () :
    x = 0
    print( "------------== MENU ==-------------")
    for menu in menus:
        x = x + 1
        print(menu['name'] + ': ' + str(x))
        

createMenu ()
getInterface ()
