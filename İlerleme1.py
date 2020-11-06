a=str(input("Kullanici Adi: "))
print("Hosgeldin",a)
print("Hesap Makinesi icin 1 yaziniz,Maç Skorları icin 2 yaziniz,Hava Durumu İcin 3 yaziniz")
b=int(input())
if(b==1):
    while True:
        print("")
        c=int(input("Bir Sayi Giriniz:"))
        d=int(input("Bir Sayi Daha Giriniz:"))
        e=f=g=h=int()
        e=c+d
        f=c-d
        g=c*d
        h=c/d
        print("Toplam: ",e)
        print("Cıkartma: ",f)
        print("Carpma: ",g)
        print("Bölme: ",h)
elif(b==2):
    print("")
    print("Kahramanmaraşspor 2 : 0 Somaspor")
    print("Akishar Belediye 0(4) : 0(5) Etimesgut")
elif(b==3):
    print("")
    print("Kahramanmaraş 25 derece hafif yağmurlu")
    print("Adana 24 derece ara ara yağmurlu")
    print("Mersin 22 derece Normalden fazla nemli hava ve güneşli")
    print("Gaziantep ortalama 26 derece öğleden sonra yağmurlu")
    print("Kayseri 23 derece güneşli")
else:
    print("Çok Yakında Hizmette...")