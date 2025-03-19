'''
Kullanıcıdan bir görev listesi al (örneğin "yazı yaz: 2, kod yaz: 5, toplantı: 1" gibi görev ve süreler saat cinsinden, virgülle ayrılmış şekilde).
Bu veriyi bir sözlüğe kaydet: anahtarlar görevler, değerler süreler olsun.
Bir fonksiyon yaz: gorev_analizi(sozluk), bu fonksiyon:
    Toplam süreyi hesaplasın.
    3 saatten fazla süren görevleri bir listeye kaydetsin.
Sonuçları ekrana yazdır: Sözlük, toplam süre, 3 saatten fazla süren görevler.

'''

'''
Örnek Çıktı
Görev listesini girin (görev: süre, virgülle ayırın): yazı yaz: 2, kod yaz: 5, toplantı: 1
Görev listesi: {'yazı yaz': 2, 'kod yaz': 5, 'toplantı': 1}
Toplam süre: 8
3 saatten fazla süren görevler: ['kod yaz']

'''

kac_tane = int(input("Kaç tane görev gireceksiniz: "))
gorev_listesi = {
    input("Görev giriniz:"): int(input("Kaç saat sürecek: "))
    for _ in range(kac_tane)
    }

def gorev_analizi(gorev_listesi):
    toplam_sure = sum(gorev_listesi.values())
    print("Toplam süre", toplam_sure)
    ucsaat = []
    for gorev in gorev_listesi:
        if gorev_listesi[gorev] > 3:
            ucsaat.append(gorev)
    print("Üç saatten fazla süren görevler:",ucsaat)

print(gorev_analizi(gorev_listesi))
