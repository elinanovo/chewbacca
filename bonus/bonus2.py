print('Введите температуру в градусах Цельсия')
a=input()
if a=='':
    print('Упс, вы ввели пустую строку')
    
else:
    a=float(a)
    F=float()
    F= round ((a*1.8)+32)
    K= round (a+273.15)
    print ('Перевод в градусы Фаренгейта =',F,'\nПеревод в градусы Кельвина =',K)
