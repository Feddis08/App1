import time
#Hallo
print ('!!!System check!!!')
print ('!!!System check!!!')
print ('!!!System check!!!')
time.sleep(2)    

try:
    system = open("password.txt", "r")
except:
    print('Error Code: 1')
    exit()

try:
    system = open("quiz.txt", "r")
except:
    print('Error Code: 2')
    exit()

try:
    system = open("Exit.txt", "r")
except:
    print('Error Code: 8')
    exit()

try:
    from Taschenrechner import getTaschenrechner
except:
    print('Error Code: 3')
    exit()

try:
    from ErrorManager import getError
except:
    print('Error Code: 4')
    exit()

try:
    from quiz import getQuiz
except:
    print('Error Code: 5')
    exit()

try:
    from Loading import getLoading
except:
    print('Error Code: 6')
    exit()

try:
    from Exit import getExit
except:
    print('Error Code: 7')
    exit()

pwFile = open("password.txt", "r")
pw = pwFile.read()
	
password = input('Password: ')
if password == pw :
    i = 1
    while i <= 10:
        try:
            getLoading () 
            print ('Copyright by Felix Riemer')
            time.sleep(1)
            exit1 = open('Exit.txt', 'r')
            exit2 = exit1.read()
            if exit2 == 'y' :
                print('Exit')
                i = 11
                exit()
            print('!Taschenrechner: 1')
            print('!Story: 2')
            print('!Text: 3')
            print('!Password Manager: 4')
            print('!Error Manager: 5')
            print('!Quiz Game: 6')
            time.sleep(1)

            p = input('app: ')
            if p != '1' and p != '2' and p != '3' and p != '4' and p != '5'  and p != '6' :
                getExit ()
                systemT = 0
            if p == '1' :
                getTaschenrechner ()
                getExit ()     
            if p == '2' :
                time.sleep(0.5)
                print('Story')
                time.sleep(1)
                name = input('Name1: ')
                time.sleep(0.5) 
                dieb = input('Name2: ')
                print('Hallo ' + name + ', wie geht es dir?')
                q = input('Next') 
                print('Nicht gut, ' + dieb + ' hat mich bestohlen.') 
                q = input('Next')   
                print('Ach, so!!!')       
                q = input('Next') 
                getLoading()

            if p == '3' : 
                time.sleep(1)

                try:
                    Text1 = open("text1.txt", "r").read ()
                    text2 = open("text2.txt", "r").read ()
                    Text3 = open("text3.txt", "r").read ()
                    Text4 = open("text4.txt", "r").read ()
                    Text5 = open("text5.txt", "r").read ()
                    print( Text4)
                except:
                    print('Error Code: 01')
                    getLoading ()     
                print('Text ')
                time.sleep(0.5)
                print('File1: 1')
                print('File2: 2')
                print('File3: 3')
                print('File4: 4')
                print('File5: 5')
                TexteInput = input('File: ') 
                if TexteInput == '1' :
                    ttt = open("text1.txt", "r").read ()
                    print(ttt)
                    Text11 = open("text1.txt", "w")
                    neu1 = input('Eingabe: ')
                    Text11.write(neu1)
                    Text11.close()
                    getLoading ()

                if TexteInput == '2' :
                    print(Text2)
                    Text22 = open("text2.txt", "w")
                    Text2 = input('Eingabe: ')
                    Text22 = Text22.write(Text2)
                    Text22.close()
                    getLoading ()

                if TexteInput == '3' :
                    print(Text3)
                    Text33 = open("text3.txt", "w")
                    Text3 = input('Eingabe: ')
                    Text33 = Text33.write(Text3)
                    Text33.close()
                    getLoading ()

                if TexteInput == '4' :
                    print(Text4)
                    Text44 = open("text4.txt", "w")
                    Text4 = input('Eingabe: ')
                    Text44 = Text44.write(Text4)
                    Text44.close()
                    getLoading ()

                if TexteInput == '5' :
                    print(Text5)
                    Text55 = open("text5.txt", "w")
                    Text5 = input('Eingabe: ')
                    Text55 = Text55.write(Text5)
                    Text55.close()
                    getLoading ()

                try:
                    Text1 = open("text1.txt", "r").read ()
                    text2 = open("text2.txt", "r").read ()
                    Text3 = open("text3.txt", "r").read ()
                    Text4 = open("text4.txt", "r").read ()
                    Text5 = open("text5.txt", "r").read ()
                except:
                    print('Error Code: 3')
                    getLoading ()  

            if p == '4' :
                pwe = input('old Password: ')
                if pwe == pw :
                    pwe = input('new Password: ')
                    pwFile = open("password.txt", "w")
                    pw = pwFile.write(pwe)
                    getLoading ()

            if p == '5' :
                getError ()

            if p == '6' :
                getQuiz ()
                getLoading ()

        except:
            print('Error wait')
            time.sleep(0.5)
            getExit ()
            time.sleep(0.5)
            getLoading ()
