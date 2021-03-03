def sesli_kaldir(cumle):
    sesliHarfler = "aeiıouüöAEIİOÖUÜ"
    yeni = ""

    for i in cumle:
        if i not in sesliHarfler:
            yeni += i
    return yeni


print(sesli_kaldir("of sanane be salak şey"))