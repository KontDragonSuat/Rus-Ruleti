from random import randint
from time import sleep

sira = randint(1,2)
hayat = True
rakip = True

while True:
    ates = 0
    mermi = randint(1, 9)
    print("Oyun Başladı!")
    sleep(0.7)
    print("Silah Hazırlanıyor...")
    sleep(1)
    print("Hangi Oyuncunun Başlayacağını Belirlemek İçin Zar Atılıyor...")
    sleep(2)
    print(f"\n{sira}. Oyuncu Başlıyor!")
    while hayat and rakip:
        if sira == 1:
            sleep(1)
            input("\nSilahı kafanıza doğrulttunuz!\n(Ateş etmek için Enter'a basın)")
            ates += 1
            sleep(1)
            if ates == mermi:
                print("Öldünüz! Kaybettiniz!")
                hayat = False
            else:
                print("Ölmediniz! Şanslısınız! Sıra Rakibinizde!")
                sira = 2
        else:
            sleep(1)
            print("\nRakibiniz Silahı Kafasına Doğrulttu")
            ates += 1
            sleep(1)
            if ates == mermi:
                print("Rakibiniz Öldü! Kazandınız!")
                rakip = False
            else:
                print("Rakibiniz Ölmedi! Sıra Sizde!")
                sira = 1

    sleep(1)
    tekrar = int(input("\nTekrar Oynamak İster Misin?\n(1-Evet 2-Hayır)\n"))
    if  tekrar == 1:
        hayat = True
        rakip = True
    else:
        print("Oyundan Çıkılıyor...")
        break