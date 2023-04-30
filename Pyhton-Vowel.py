# kullanıcının girdiği metin
metin = input("Bir metin girin: ")

# sesli harflerin listesi
sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']

# metindeki sesli harfleri saymak için sayaç
sesli_sayisi = 0

# metindeki her harf için kontrol yap
for harf in metin:
    # eğer harf bir sesli harfse
    if harf.lower() in sesli_harfler:
        # sesli sayısını artır
        sesli_sayisi += 1

# sonucu ekrana yazdır
print("Metindeki sesli harf sayısı:", sesli_sayisi)
