import time
def getLoading () :
    
    print('Error, wait')
    e = ''
    x = 0
    for x in range(10) :
        i = 9
        i -= x
        i /= 20
        e += '/'
        time.sleep(i)
        print('Loading: ' + e)
if __name__ == '__main__':
    getLoading ()


    
    