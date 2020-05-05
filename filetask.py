file = open('teams.txt' , 'w')

newline = 'This is the first line' + '\n' + 'Scorpions' + '\n' + 'Rovers' + '\n' + 'Rangers'
file.write(newline)

file.close()

file = open('teams.txt', 'r')

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())





file.close()