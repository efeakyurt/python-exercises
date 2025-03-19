'''
Kullanıcıdan bir alışveriş listesi al (örneğin "elma: 3, muz: 2, armut: 5" gibi ürün ve miktarları virgülle ayrılmış şekilde).
Bu veriyi bir sözlüğe kaydet: anahtarlar ürünler, değerler miktarları olsun.
Bir fonksiyon yaz: alisveris_ozeti(sozluk), bu fonksiyon:
    Toplam ürün sayısını (miktarların toplamı) hesaplasın.
    En fazla miktarda alınan ürünü bulsun.
Sonuçları ekrana yazdır: Sözlük, toplam ürün sayısı, en fazla alınan ürün ve miktarı.

'''

'''
Örnek Çıktı
Alışveriş listesini girin (ürün: miktar, virgülle ayırın): elma: 3, muz: 2, armut: 5
Alışveriş listesi: {'elma': 3, 'muz': 2, 'armut': 5}
Toplam ürün sayısı: 10
En fazla alınan ürün: armut, Miktar: 5

'''


kac_tane = int(input("Kaç tane ürün alacaksınız(Sadece farklı tür ürünleri girin): "))
alisveris_listesi = {
    input("Alınacak Ürün: "): int(input("Miktar: ")) #int(input) yaparak valueları integer olarak alıyorum.  
    for _ in range(kac_tane)
}

def alisveris_ozeti(alisveris_listesi):
    toplam_urun = sum(alisveris_listesi.values())

    en_fazla_urun = max(alisveris_listesi, key= alisveris_listesi.get)
    en_fazla_miktar = alisveris_listesi[en_fazla_urun]

    print("Alışveriş Listesi:", alisveris_listesi)
    print("Toplam Ürün Sayısı:", toplam_urun)
    print(f"En Fazla Alınan Ürün: {en_fazla_urun}, Miktar: {en_fazla_miktar}")

print(alisveris_ozeti(alisveris_listesi))