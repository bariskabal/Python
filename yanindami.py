def arkadas(liste):

    if liste.index("Fatih") == liste.index("Vural")+1:
        return True
    if liste.index("Fatih") == liste.index("Vural")-1:
        return True
    return False
print(arkadas(["Ali","Fatih","Yavuz","Vural"]))