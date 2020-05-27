import random
def hello():
    mylist = []
    for i in range(5):
       mylist.append(random.randint(100,201))
    return mylist

print(hello())