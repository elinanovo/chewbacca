with open("Ozhegov2.txt", encoding="utf-8") as f:
    antonyms=0
    for line in f:
        slovo=line.split('|')
        if len (slovo)>=3:
            if slovo [2]!='':
                #print(slovo[2])
                antonyms+=1
print("Всего антонимов =",antonyms)
            
        
            
       
        
