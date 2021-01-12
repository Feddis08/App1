import time
def getTaschenrechner () :
    def getOperands () :
                    
        O1 = int(input('Operand 1: '))
        O2 = int(input('Operand 2: '))
        return [O1,O2]
    time.sleep(1)
    print ('Taschenrechner')
    time.sleep(0.5)
    Ergebnis = 'Error'        
    operator = input('operator (+,-,*,:): ' )
    if operator == '+' :
        opers = getOperands ()
        Ergebnis = opers[0] + opers[1]
    if operator == '-' :
        opers = getOperands ()
        Ergebnis = opers[0] - opers[1]
    if operator == '*' :
        opers = getOperands ()
        Ergebnis = opers[0] * opers[1]
    if operator == ':' :
        opers = getOperands ()
        Ergebnis = opers[0] / opers[1]
    print ('Ergebnis: ' + str(Ergebnis))

if __name__ == '__main__':
    getTaschenrechner ()