

#int1 = int(input('Enter a number greater than 0: '))
#int2 = int(input('Enter a number greater than 0: '))

def blackjack(int1, int2):
    if int1 > 21 and int2 > 21:
        return 0
    elif int1 > 21 and int2 <= 21:
        return int2
    elif int2 > 21 and int1 <= 21:
        return int1
    elif 21 - int1 < 21 - int2:
        return int1
    elif 21 - int2 < 21 - int1:
        return int2
    elif int1 == 21 and int2 == 21:
        return 0
    
