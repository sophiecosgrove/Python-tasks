prime_nums = 0

for i in range(2,10):
    for x in range(2,i):
        if i % x == 0:
            break
    else: 
        prime_nums += 1
                
print(prime_nums)






