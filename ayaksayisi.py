def hayvanlar(tavuk,inek,koyun):

    tavukBacak = tavuk * 2
    inekBacak = inek * 4
    koyunBacak = koyun * 4

    toplam = tavukBacak + inekBacak + koyunBacak

    return toplam

def hayvanlar2(t,i,k):
    return t*2 + (i+k)*4


print(hayvanlar2(2,3,5))  
print(hayvanlar(2,3,5))

