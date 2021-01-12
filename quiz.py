def getQuiz () :
    import time
    quizp = 0
    time.sleep(0.5)
    print('Quiz!')
    print('')
                    
    time.sleep(1)
    print('!Quiz Minecraft: 1 ')
    s = input('Ouiz: ')   
    if s == '1' :
        time.sleep(0.5) 
        print('Quiz Minecraft')
        time.sleep(1)
        print('Was ist harter?')
        print()
        time.sleep(0.5)
        print('Eisen: 1')
        print('Holz: 2')
        print('Gold: 3')
        time.sleep(1)
        print('')
        quiz1 = input('Antwort: ')
    if quiz1 != '1' :
        print('Falsch')
        q = input('')
        
    else :
        print('richtig')
        quizp += 1
        q = input('')

    if s == '2' :
        time.sleep(0.5)
        print('Quiz Minecraft')
        time.sleep(1)
        print('Wie viel Weizen braucht man fur Brot?')
        print()
        print('9 Weizen: 1')
        print('6 Weizen: 2')
        print('3 Weizen: 3')
        time.sleep(1)
        quiz2 = input('Antwort: ')
        if quiz2 != '3' :
            print('Falsch')
            q = input('')
         
                    
        else :
            print('richtig')
            quizp += 1
            q = input('')
if __name__ == '__main__':
    getQuiz ()                                               