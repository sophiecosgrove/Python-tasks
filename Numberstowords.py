number = int(input('Enter a number: '))

singles = {1: 'One', 2: 'Two', 3: 'Three',4: 'Four',5: 'Five',
6: 'Six', 7: 'Seven', 8: 'Eight',9: 'Nine'}
teens = {11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
18 : 'Eighteen', 19: 'Nineteen'}
tens = {1: 'Ten', 2: 'Twenty', 3 : 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9 : 'Ninety'}

if number < 10:
    print(singles[number])
elif number > 10 and number < 20:
    print(teens[number])
elif number > 20 and number < 100:
    numberlist = list(number)
    print(tens[numberlist[0]], singles[numberlist[1]])



 
