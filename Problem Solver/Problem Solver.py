# People have many problems but they can solver their problems with this


print('WRITE ALL WITH LOWERCASE')



def funcion():
    word = input('Your problem: ')

funcion()


def funcion_2():
    word_2 = input('Cause of the problem: ')

funcion_2()



def funcion_3():
    word_3 = input('Solution: ')
    if word_3 == 'yes':
        input('Which one: ')
        input('Resources for the solution: ')
        print('Your problem have solution. Congratulations!')
    elif word_3 == 'no':
        print('Let it happen.')

    else:
        word_3 = input('Please input yes or no: ')
        if word_3 == 'yes':
            input('Which one: ')
            input('Resources for the solution: ')
            print('Your problem have solution. Congratulations! You can!')
            funcion_4()
        elif word_3 == 'no':
            print('Let it happen.')

funcion_3()







