x,y,z='B','T','K'
print(x,y,z)
x=y=z='BTK'

#bir değişkenin tipini öğrenmek için hangi komut kullanılır?
type(x)

# i=i+j kod satırını daha kısa yazabilir misin?
i=0
j=0
i+=j

# b ve c ismindeki iki değişkenin içeriklerini birbirine atayan tek satırlık kodu yazınız
b=0
c=5
print('b=',b,'c=',c)
b,c=c,b
print('b=',b,'c=',c)

#t=20+15-10 ve x=t/4+7 bu işlemler sonucunda x kaç çıkar ekrana yazdırınız.
t=20+15-10
x=t/4+7
print(x)

#Python dilinde komut olarak kullanilan anahtar kelimeler (keywords)degisken ismi olarak kullanilamazlar. Python dilindeki anahtar kelimeleri yazdiran kodlar nelerdir?
import keyword
keyword.kwlist

#b=40 ve c=str(b)+'5' şeklinde verilen kod bloğundan c çıktısı ne olur?
b=40
c=str(b)+'5'
print(c)
type(c)#c değişkeninin veri tipini gösterir







