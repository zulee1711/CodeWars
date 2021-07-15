array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if bool(i) == True:
            count += 1
        else:
            pass
    return count

print(count_sheeps(array1))