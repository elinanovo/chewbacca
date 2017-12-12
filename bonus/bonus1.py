print('Введите число')
a=input()
summa=0
m=0
while a !="":
        a=int(a)
        summa=summa+a
        m+=1
        print(summa, a)
        print('Введите число')
        a=input()
if a =="":
    average=summa/m
    print('Среднее арифметическое=', average)
