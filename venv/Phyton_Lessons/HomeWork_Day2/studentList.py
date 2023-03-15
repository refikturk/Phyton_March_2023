#Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
#Bu öğrenci kayıt sistemine;
#Aldığı isim soy isim ile listeye öğrenci ekleyen
#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
#Listeye birden fazla öğrenci eklemeyi mümkün kılan
#Listedeki tüm öğrencileri tek tek ekrana yazdıran
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
#fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

#Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

print("*****kodloma.io Yazılım Geliştirme Kampı Öğrenci Listesi*****")

ogrenciListesi = []
# Öğrenci eklemek için ogrenciEkle methodu oluşturulmuş olup parametresiz bir method oluşturulmuştur
# parametreli methodlarda oluşturulabilir.
def ogrenciEkle ():
    adı = input("Öğrencinin adını giriniz: ")
    soyadı = input("Öğrencinin soyadını giriniz: ")
    adıSoyadı = f"{adı} {soyadı}"
#print(adıSoyadı)
    if ogrenciListesi.__contains__(adıSoyadı):
        print("Bu isimde başka bir öğrenci var" , {adıSoyadı})
        ogrenciListesi.remove(adıSoyadı)
        print("ogrenciListesi" , ogrenciListesi)
    else:
        ogrenciListesi.append(adıSoyadı)
        print("Öğrenci Listesi:" , ogrenciListesi)

#Bu method ile yeni öğrenci kaydı sorusuna evet şeklinde cevap verildiği müddet yeni kayıt oluşturulacaktır.
def cokluOgrenciEkle():
    yeniKayıt = "Evet"
    while yeniKayıt.__eq__("Evet"):
        ogrenciEkle()
        yeniKayıt = input("Yeni öğrenci kaydı olacak mı Evet/Hayır : ")


#Bu method ile öğrenci isimlerini tek tek yazdırmak için for each loop kullanarak listemizin her bir elemanına
#ulaşabileceğiz.
def printStudentNames():
    for ogrenci in ogrenciListesi:
        print(ogrenci)

#Öğrenci numarasının öğrencinin bulunduğu index numarası olarak ele aldığımızda öğrenci numarası ve öğrenci adını yazdıralım.
def studentNumber():

    id = 0
    for ogrenci in ogrenciListesi:
        print(ogrenci , "Öğrenci Numarası: " , id )
        id = id + 1
        
ogrenciEkle()
cokluOgrenciEkle()
printStudentNames()
studentNumber()





























