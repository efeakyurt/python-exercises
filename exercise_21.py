# Kullanıcıdan bir tam sayı listesi al (örneğin "3, 5, 7, 2" gibi virgülle ayrılmış sayılar).
# Bu sayıları bir listeye kaydet.
# Bir fonksiyon yaz: sayi_analizi(liste), bu fonksiyon:
# Listedeki çift sayıları bir listeye, tek sayıları başka bir listeye ayırsın.
# Çift ve tek sayıların toplamlarını hesaplasın.
# Sonuçları ekrana yazdır: Çift sayılar, tek sayılar, çiftlerin toplamı, teklerin toplamı.

'''
Örnek Çıktı:

Sayıları virgülle ayırarak girin: 3, 5, 7, 2
Çift sayılar: [2]
Tek sayılar: [3, 5, 7]
Çiftlerin toplamı: 2
Teklerin toplamı: 15

'''

sayi_listesi = input("Enter number list separated by comma and a space after it: ").split(", ")
sayi_listesi = [int(sayi) for sayi in sayi_listesi]

def sayi_analizi(sayi_listesi):
    cift_sayilar = []
    tek_sayilar = []
    for sayi in sayi_listesi:
        if sayi % 2 == 0:
            cift_sayilar.append(sayi)
        else:
            tek_sayilar.append(sayi)
    return cift_sayilar, tek_sayilar

cift_sayilar, tek_sayilar = sayi_analizi(sayi_listesi)

print("Çift Sayılar:", cift_sayilar)
print("Tek Sayılar:", tek_sayilar)
print("Çiftlerin Toplamı:", sum(cift_sayilar))
print("Teklerin Toplamı:", sum(tek_sayilar))

