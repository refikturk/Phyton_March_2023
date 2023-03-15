krediler = ["Hızlı Kredi","Maaşını Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]

#eğer bir dizide kaç eleman olduğunu bilmediğimiz zamanlarda tercih etmemiz gereken döngü tipi
for kredi in krediler:
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])
#belirli sayıda dönmesini istedğimiz döngüler için kullandığımız döngü tipi
for i in range(3,10): 
    print(i)
    
#belirli bir sayıda farklı artırma veya
for i in range(0,10,2): 
    print(i)

for kredi in krediler:
    print("<option>" + kredi+ "</option>")