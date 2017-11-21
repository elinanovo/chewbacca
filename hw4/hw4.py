#ВАРИАНТ 7
with open ("text.txt", encoding = "utf-8") as f:
    text = f.read()
print (text, " ")
lines = text.splitlines()
lines_bez_pustyh= list (filter(lambda x: len(x)>0,lines))
total = len(lines_bez_pustyh)
number=0
for line in lines:
    line=line.split (" ")
    if len(line)>=5:
        number=number+1
        print(line, len(line))
answer=(number/total)*100
print ( 'всего строк=', total ,'строк, где 5 или больше слов=', number, 'процент таких строк=', answer,  sep = '\n')
      


