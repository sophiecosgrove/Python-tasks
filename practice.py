def near(str1, str2):
    strlist = list(str1)
    strlist2 = list(str2)
    for ch in range(len(strlist)):
        insert = strlist[ch]
        del strlist[ch]
        print(strlist)
        if strlist == strlist2:
            return True
        else:
            strlist.insert(ch, insert)
            continue
    if strlist != strlist2:
            return False
            
    


    

print(near('sleet', 'lets'))