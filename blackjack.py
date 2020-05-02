

int1 = int(input('Enter a number greater than 0: '))
int2 = int(input('Enter a number greater than 0: '))

if int1 > 21 and int2 > 21:
    print(0)
elif int1 > 21 and int2 <= 21:
    print(int2)
elif int2 > 21 and int1 <= 21:
    print(int1)
elif 21 - int1 < 21 - int2:
    print(int1)
elif 21 - int2 < 21 - int1:
    print(int2)
