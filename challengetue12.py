def all_even(number):
    num_str = str(number)
    digit_bool = []
    for i in num_str:
        if int(i) % 2 == 0:
            digit_bool.append(True)
        else:
            digit_bool.append(False)
    return digit_bool

mylist = [i for i in range(1000, 3001) if all(all_even(i))]
    
    

print(','.join([str(i) for i in mylist]))


