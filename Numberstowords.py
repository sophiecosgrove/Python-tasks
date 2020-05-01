number = int(input('Enter a number: '))

singles = {1:'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
6:'Six', 7 : 'Seven', 8: 'Eight', 9: 'Nine'}
teens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
18 : 'Eighteen', 19: 'Nineteen'}

if number - 10 < 0:
    print( "-".join(singles[number]))
if number > 100:
    print(singles[number/100], 'hundred')
else:
    print(teens[number])

 
