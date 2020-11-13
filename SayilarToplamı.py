toplam = 0
print("Kaç İle Kaç Arasındaki Sayilari Toplamak İstersiniz")
print("Not: Seçtiğiniz Sayilar Dahildir")
a=int(input("İlk Sayi "))
b=int(input("İkinci Sayi "))

for sayi in range(a,b+1):
    toplam = sayi + toplam
print("Toplma:",toplam)