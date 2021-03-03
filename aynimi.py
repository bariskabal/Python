def ayni_mi(kelime):
    if kelime.isupper():
        return True
    elif kelime.islower():
        return True
    else:
        return False

ayni_mi2 = lambda kelime2 : kelime2.isupper() or kelime2.islower()

print(ayni_mi2("baris"))

print(ayni_mi("NABER"))