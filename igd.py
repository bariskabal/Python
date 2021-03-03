
class personel():
    def __init__(self,nitelik):
        self.nitelik=nitelik
        self.index=-1

    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if(self.index<len(self.nitelik)):
            return self.nitelik[self.index]
        else:
            self.index=-1
            raise StopIteration

baris = personel(["C#","Java","Python"])
iterator = iter(baris)
print(next(iterator))

for i in baris:
    print(i)


    def öncekiyle_carp():
        for i in range(1,6):
            yield i* (i-1)
    generator = öncekiyle_carp()
    print(generator)
    iterator = iter(generator)
    print(next(iterator))
    print(next(iterator))

    def ornek_decorator(fonk):
        def wrapper():
            print("öncesi")
            fonk()
            print("sonrası")
        return wrapper

    @ornek_decorator
    def selam():
        print("merhaba")

    selam()
