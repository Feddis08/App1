def getError () :
    import time
    print('This is the error manager ' )     
    time.sleep(0.5)
    print('')
    print('Code: 1, The passwordfile(password.txt) is missing!') 
    print('Code: 2, The quizfile(quiz.txt) is missing!')
    print('Code: 3, One or more of the textfils(text1/2/3/4/5.txt) are missing!')
    q = input('Back to home. ')
if __name__ == '__main__':
    getError ()
