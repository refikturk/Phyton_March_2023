#Phyton programa diline giriş.
#Phyton veri tipleri nelerdir?
#Phyton veri tipleri aşağıda belirtilmiştir.
# -> String - birbiri ardına gelen karakterlerin oluşturduğu veri tipleridir.
# -> Rakamsal veri tipleri - integer ve float'tır. integer tam sayıyı , float ise küsürlü rakamları ifade eder.
# -> bool - atandığı değerin sonucunda true veya false olarak dönüş sağlayan mantıksal sorgulama yapan veri tipidir
# -> Dizi tipleri - list, tuple, range

# String nedir? String veri/değişken tipleri sıralı karakterlerden oluşan değişken tipleridir Stringler çift tırnak veya
# tek tırnak içerisinde atanabilir aşağıda birkaç String değişken tipi örneği verilmiştir

str = "Hello World"
print(str)
str1 = 'Hello World'
print(str1)
print(type(str))
print(type(str1))
#Kodlama.io sitesinde bulunan kurs başlıkları string veri tipleri için birer örnektir.
kursAdı = "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium"
print(kursAdı)
print(type(kursAdı))

print("***Rakamsal Veri Tipleri***")

#Rakamsal veri tipleri, tam sayı veya desimal rakamları atayabildiğimiz değişkenlerdir. Phyton programlama dili hangi
#veri atadığımızı otomatik olarak algıladığı için veri tipini belirtmek gerekmez.
#int değerleri
num = 10
print(type(num))
num2 = 10.0
print(type(num2))
#Kodlama.io sitesinde bulunan kurs tamamlama oranları rakamsal veri tipleri için örnek olarak verilebilir.

print("***bool**")
#bool veya boolean şeklinde tabir edilen veri tipleri tanımlanan durumun sonucunun True veya False olarak işleme alınmasını sağlar.
bool1 = True
print(bool1)
print(type(bool1))
bool2 = False
print(bool2)
print(type(bool2))
bool3 = 10 - 2 > 9 # bu değişken 8 > 9 koşulunu sorgulayacağı için bize False şeklinde dönüş yapmasını beklemeliyiz.
print(bool3)

print("***Dizi Tipleri***")
#Dizi tipleri içerisine birden fazla eleman atayabildiğimiz, türlerine göre farlılık gösteren liste türleridir ve index numaraları vardır.
print("List")
#içerisine farklı tiplerde elemanlar atayabildiğimiz ve aynı elamanı birden fazla kabul edebilen bir veri tipidir.
list = ["Kodlama.io", 1, True, "Hello Wordl", True]
list.remove("Kodlama.io") #listeler'de içerisindeki elemanları silmemiz mümkündür.
print(list)
print(len(list))

print("Tuple")
#list'den farklı olarak elemanları dinamik değildir, yani elamanlarını değiştiremeyiz, aynı elemanı birden fazla kabul edebilir.
#oluşturuken () parantez ile oluşturulurlar ve index numarası vardır.
tuple = (1, 2, 3)
print(tuple)

print("Set")
#Set türünde ise index numarası bulunmamaktadır ve elaman tekrarını kabul etmez yani bir eleman sadece bir defa kabul edilir.
#setler {} süslü parentez ile oluşturulur.

japonArabaMarkaları = {"Toyota", "Mazda", "Mitsubishi"}
print(japonArabaMarkaları)
print("Set yapı türlerinde her bir elemana for each loop döngü yapısıyla ulaşabiliriz")
for marka in japonArabaMarkaları:
    print(marka.upper())

#Kodlama.io sitesinde bulunan kur Tüm Kurslar Listelere örnek olarak gösterilebilir.


































