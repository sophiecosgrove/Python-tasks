

def is_too_hot(temp, issummer):
    if temp >= 60 and temp <= 90 and not issummer:
        return 'Too hot'
    elif temp >= 60 and temp <= 100 and issummer:
        return 'Too hot'
    else: 
        return 'It is not hot'



print(is_too_hot(temp = int(input('Enter a temp: ')), issummer = bool(input('It is summer: True or False: ')) ))