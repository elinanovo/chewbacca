print('Ведите ваше секретное послание')
a=input()
if a=='':
    print ('Упс, вы ничего не ввели')
else:
    slovo=list(a)
    if slovo[0]=='a'or slovo[0]=='e'or slovo[0]=='i'or slovo[0]=='u'or slovo[0]=='y'or slovo[0]=='o':
        secret1=a+'way'
        print (secret1)
    
    else:
        i=1
        while slovo[i]!='a'and slovo[i]!='e'and slovo[i]!='i'and slovo[i]!='u'and slovo[i]!='y' and slovo[i]!='o':
            i+=1
        secret1=slovo[i:]
        secret2=''.join(secret1)
        secret2=str(secret2)
        secret3=str(''.join(slovo[:i]))
        secret=secret2+secret3+'ay'
        print ('На поросячьей латыни это -',secret)

