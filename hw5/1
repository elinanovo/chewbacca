# Вариант7
letters=input()
if letters == '' : 
         print ('упс, вы ввели пустую строку')
         
else:
         wordlist= letters.split(' ')
         print (wordlist)
         i=0
         with open("slova.txt", "w", encoding="utf-8") as f:
                  f.write ('')
         while i <=7:
             stroka = str ("%s %s \n" % (wordlist[i], wordlist[i+1]))
             with open("slova.txt", "a", encoding="utf-8") as f:
                  f.write (stroka)
             i=i+2
with open("slova.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)            
              

