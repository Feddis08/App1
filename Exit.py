import time
def getExit () :
    time.sleep(0.5)
    x = input('Exit (y/n): ')
    if x == 'y' :
        print ('Exit')
        exit()
    if x == 'n' :
        print('wait')
        time.sleep(1)
    if x != 'y' and x != 'n' :
        x = input('Exit (y/n): ')

if __name__ == '__main__':
    getExit ()