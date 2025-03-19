# Kullanıcıdan bir metin al (örneğin bir cümle).
# Bu metindeki her kelimenin uzunluğunu bir sözlükte sakla. Anahtarlar kelimeler, değerler ise kelimelerin uzunlukları olsun.
# Sözlüğü ekrana yazdır.
# Bonus: Kelime uzunluklarının ortalamasını hesapla ve ekrana yazdır.
import string 

cümle = str(input("Bir cümle giriniz: "))
cümle = cümle.translate(str.maketrans("", "", string.punctuation))
kelimeler = cümle.split(" ")

def sözlüktesakla(kelimeler):
    sözlük = {}
    for kelime in kelimeler:
        sözlük.update({kelime: len(kelime)})
        if len(sözlük) > 0:
            ortalama_uzunluk = sum(sözlük.values()) / len(sözlük)  # Ortalama hesapla
        else:
            ortalama_uzunluk = 0  # Boş giriş olursa hata almamak için
    return sözlük, ortalama_uzunluk

print(sözlüktesakla(kelimeler))





