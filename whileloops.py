num = 10


while num > 0:
    print('There are', num, 'green bottles hanging on the wall'
    , num, 'green bottles hanging on the wall and if 1 green bottle should accidentally fall')
    num = num - 1
    bottles = int(input('How many green bottles will there be? '))
    if  bottles == num:
         print('There will be', num, 'new bottles hanging on the wall')
    else:
        while bottles != num:
            bottles = int(input('How many green bottles will there be? '))
print('There are no green bottles hanging on the wall')
