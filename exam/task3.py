print("Введите слово")
a=input()
while a!='':
    with open("Ozhegov2.txt", encoding="utf-8") as f:
        for line in f:
            slovo=line.split('|')
            if  a== slovo[0]:
                print(slovo[0],'—',slovo[3],'—',slovo[1])
                break
    a=input()
    
            #if a!==slovo[0]:
                #print("Ожегов такого слова не знает")
                #break

print("Упс, вы ничего не ввели")
