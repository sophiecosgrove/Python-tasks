def sortingwords(string1):
    splitwords = string1.split(',')
    splitwords.sort()
    return splitwords

print(sortingwords(input('Enter a word: ')))
