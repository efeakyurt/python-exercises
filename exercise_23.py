'''
Kullanıcıdan bir not defteri bilgisi al (örneğin "Ali: 85, Ayşe: 90, Mehmet: 75" gibi isim ve notlar virgülle ayrılmış şekilde).
Bu veriyi bir sözlüğe kaydet: anahtarlar isimler, değerler notlar olsun.
Bir fonksiyon yaz: not_analizi(sozluk), bu fonksiyon:
Ortalama notu hesaplasın.
80’den yüksek not alan öğrencileri bir listeye kaydetsin.
Sonuçları ekrana yazdır: Sözlük, ortalama not, 80’den yüksek not alan öğrenciler.

'''


'''
Örnek Çıktı:
Not defterini girin (isim: not, virgülle ayırın): Ali: 85, Ayşe: 90, Mehmet: 75
Not defteri: {'Ali': 85, 'Ayşe': 90, 'Mehmet': 75}
Ortalama not: 83.33333333333333
80’den yüksek not alanlar: ['Ali', 'Ayşe']

'''


kac_tane = int(input("Kaç öğrenci için not bilgisi gireceksiniz: "))
ogrenci_listesi = {
    str(input("Öğrenci ismini girin:")): int(input("Öğrenci notunu girin:"))
    for _ in range(kac_tane)
}

def not_analizi(ogrenci_listesi):
    toplam_not = sum(ogrenci_listesi.values())
    ortalama_not = toplam_not / kac_tane
    notlar = ogrenci_listesi.values()
    buyukseksen = []
    for ogrenci in ogrenci_listesi: 
        if ogrenci_listesi[ogrenci] > 80:
            buyukseksen.append(ogrenci)

    print("Ortalama Not:",ortalama_not)
    print("80'den yüksek not alanlar:",buyukseksen)


print(not_analizi(ogrenci_listesi))

