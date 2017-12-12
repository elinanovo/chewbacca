with open("Ozhegov2.txt", encoding="utf-8") as f:
    print("Слова длиннее 20 символов","\n")
    for line in f:
        slovo=line.split('|')
        if len(slovo[0])>=20:
            print(line)
