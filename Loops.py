direction = input('do you want to go up or down? ')

if direction == 'up':
    top_number = int(input('enter top number: '))
    for i in range(top_number + 1):
        print(i)
if direction == 'down':
    bottom_number = int(input('enter number below 20: '))
    count = 1
    for i in range(bottom_number,20):
        print(20 - count)
        count += 1
