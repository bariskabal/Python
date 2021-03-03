def yuzyil(yil):
    yuzyil = yil//100
    if(yil%100>0):
        yuzyil+=1
    return "{s}. yüzyıl".format(s=yuzyil)
    

print(yuzyil(2000))