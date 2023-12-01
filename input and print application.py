isim= input("isminiz:")
yas= input("yaşınız:")#bu str tipinde bir veri giridisi alır
#int tipinde bir veri girdisi alma daha doğrusu alınan veriyi int'e çevirmek için
yas= int(input("yaşınız:"))

#ekrana yazı yazdırmak
print ('b','t','k')
print ('b','t','k', sep=',')#harfleri hangi işaretle ayıracağını belirtir. burada harfleri virgüllerle ayıracak.
#string bir ifadeyi kaç kere yazacağımız belirtir ekrana 3 defa btk yazar bitişik şekilde
print("btk"*3)

#girdiyi ekrana yazdığımız yazının yanına yazar.
print("yaşınız", end=(''))#parantezin içine yazılan şeyi de ekrana yazdırır.
yas= input()

#aynı print içinde iki kelimeyi alt alta yazadırmak istersek
print("btk\nAkademi")
#bir tab boşluk bırakmak için
print("btk\tAkademi")
