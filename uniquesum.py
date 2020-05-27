ans = 0 

def is_unique(int1,int2,int3):
    if int1 != int2 and int1 != int3 and int2 != int3:
        ans = (int1 + int2 + int3)
    elif int1 == int2 and int1 != int3:
        ans = int3
    elif int1 == int3 and int1 != int2:
        ans = int2
    elif int2 == int3 and int2 != int1:
        ans = int1
    else:
         ans = 0
    return ans


#go = is_unique(int1 = int(input('Enter a number: ')), int2 = int(input('Enter a number: ')), int3 = int(input('Enter a number: ')))
#print(go)

