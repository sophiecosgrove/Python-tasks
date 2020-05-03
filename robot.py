

def robot(up, down, left, right):
    if up >= 0:
        up = 0 + up
    if down >= 0:
        y = up - down
    if left >= 0:
        left = 0 - left
    if right >= 0:
        x = left + right
    return int((x ** 2 + y ** 2) **.5)

print(robot(int(input('Enter up: ')), int(input('Enter down: ')), int(input('Enter left: ')), int(input('Enter right:')) ))
