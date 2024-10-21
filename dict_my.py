intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = input()
trantab = str.maketrans(intab, outtab)
str = ''.join([i.lower() for i in input()])
#print(outtab)
print (str.translate(trantab))