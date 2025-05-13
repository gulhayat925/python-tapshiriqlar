Sprint_3a_task

x dəyişəni verilmişdir. Əgər x > 0 olarsa "müsbət", x < 0 olarsa "mənfi", bərabərdirsə "sıfır" çap etsin.
x=int(input())
if x<0:
 print("menfidir")
elif x>0:
 print("musbetdir")
else:
  print("sifirdir")

n rəqəmi cütdürsə "cüt", təkdirsə "tək" çap etsin.

n=int(input())
if n%2==0:
  print("cutdur")
else:
  print("tekdir")

a, b, c rəqəmləri verilmişdir. Ən böyük rəqəmi çap etsin.

a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
  print(a)
elif b>a and b>c:
  print(b)
else:
  print(c)

day dəyişəni 1-7 arası rəqəmdir. Müvafiq həftə gününü (1 = "Bazar ertəsi", ..., 7 = "Bazar") çap etsin, əks halda "Yanlış gün" yazsın.

day=int(input())
if day==1:
  print("Bazar ertesi")
elif day==2:
  print("Cersenbe axsami")

elif day==3:
  print("Cersenbe")
elif day==4:
  print("Cume axsami")
elif day==5:
  print("Cume")
elif day==6:
  print("Senbe")
elif day==7:
  print("Bazar")
else:
  print("Yanlis gun")

temp dəyişəni temperaturdur. Əgər temp < 0 olarsa "soyuq", 0-20 arası olarsa "normal", 20-dən böyükdürsə "isti" çap etsin.

temp=int(input())
if temp<0:
  print("soyuq")
elif temp>20:
  print("isti")
else:
  print("normal")

password adlı string verilmişdir. Əgər uzunluğu 8-dən kiçikdirsə "qısa", 8-12 arasıdırsa "orta", 12-dən böyükdürsə "uzun" çap etsin.

password=input()
if len(password)<8:
  print("qısa")
elif len(password)>12:
  print("uzun")
else:
  print("orta")

x rəqəmi həm 3-ə, həm də 5-ə bölünürsə "3 və 5", yalnız 3-ə bölünürsə "3", yalnız 5-ə bölünürsə "5", heç birinə bölünmürsə "heç biri" çap etsin.

x = int(input())

if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

0-dan 20-yə qədər cüt rəqəmləri çap etsin.

for i in range(0,20):
  if i%2==0:
    print(i)
    i+=1

"Bağda ərik var idi …" stringinin hər elementini for ilə ayrı-ayrılıqda çap edin.

metn = "Bağda ərik var idi …"
for simvol in metn:
    print(simvol)

1-dən 10-a qədər rəqəmləri çap edin, amma 3 xaric.

for i in range(1,10):
  if i==3:
    continue
  print(i)

1-dən başlayaraq ilk 5-ə bölünən rəqəmi tapın və while ilə çap edin (break istifadə edin).

i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1

(1, 3, 5, 7, 9) listində/vectorunda 5-i tapın və indeksini çap edin (break istifadə edin).

list = (1, 3, 5, 7, 9)

for indeks, deyer in enumerate(list):
    if deyer == 5:
        print(indeks)
        break


Sprint_3b_task

salam adlı funksiya yaradın ki, heç bir arqument almadan sadəcə "Salam, Dünya!" çap etsin.

def salam():
    print("Salam, Dünya!")
salam()

kub_hesabla adlı funksiya yaradın ki, bir rəqəm (n) qəbul etsin və onun kubunu qaytarsın.

def kub_hesabla():
  n=int(input())
  print(n**3)
kub_hesabla()

birlesdir adlı funksiya yaradın ki, iki söz qəbul etsin və onları boşluqla birləşdirib qaytarsın.

def birlesdir(soz1, soz2):
    return soz1 + " " + soz2
netice = birlesdir(input(),input())
print(netice)

cap_et adlı funksiya yaradın ki, bir listi arqument olaraq alsın və listin hər elementini for ilə çap etsin.

def cap_et(list):
    for element in list:
        print(element)
my_list = ["ADNSU", "UNEC", "BDU"]
cap_et(my_list)

toplam adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların cəmini qaytarsın.

def toplam(*args):
    return sum(args)
netice = toplam(1, 2, 3, 4, 5)
print(netice)

ortalama adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların ortalamasını qaytarsın (əgər heç bir rəqəm yoxdursa, "Rəqəm yoxdur" qaytarsın).

def ortalama(*args):
    if not args:  # Eğer hiç argüman yoksa
        return "Rəqəm yoxdur"
    return sum(args) / len(args)
print(ortalama(2,4,8))

adlar_rəqəmlər adlı funksiya yaradın ki, istənilən sayda ad və rəqəm cütünü (**kwargs) qəbul edib hər cütü çap etsin (məsələn, "ad: bir, rəqəm: 1").

def adlar_reqemler(**kwargs):
    for ad, reqem in kwargs.items():
      print(f"ad: {ad}, reqem: {reqem}")
adlar_reqemler(bir=1,iki=2,üç=3)

tip_yoxla adlı funksiya yaradın ki, bir dəyər qəbul edib onun tipini yoxlasın: "mətn", "rəqəm", "başqa" çap etsin.

def tip_yoxla(dəyər):
    if isinstance(dəyər, str):
        print("mətn")
    elif isinstance(dəyər, (int, float)):
        print("rəqəm")
    else:
        print("başqa")
tip_yoxla(5)
tip_yoxla("salam")
tip_yoxla([5,15,34])

yas_kateqoriya adlı funksiya yaradın ki, input()/readline() ilə yaş soruşsun, 18-dən aşağıysa "Gənc", yuxarıdrsa "Yetkin" çap etsin.

def yas_kateqoriya():
    try:
        yas = int(input("Yaşınızı daxil edin: "))
        if yas < 18:
            print("Gənc")
        else:
            print("Yetkin")
    except ValueError:
        print("Zəhmət olmasa düzgün yaş daxil edin!")
yas_kateqoriya()

soz_uzunluq adlı funksiya yaradın ki, input()/readline() ilə istifadəçidən söz alsın və onun uzunluğunu çap etsin.

def soz_uzunluq():
    soz = input("Bir söz daxil edin: ")
    print("Uzunluq:", len(soz))
soz_uzunluq()





Sprint_4a_task

İstifadəçidən iki rəqəm və bir əməliyyat (toplama, çıxma, vurma, bölmə) daxil etməsini tələb edən funksiya yazın. Mümkün xətaları (ValueError, TypeError və s.) idarə edin və müvafiq mesajlar çıxarın. Sonda da "Hesablama bitdi" mesajı çap olunsun.

def hesabla():
    try:
        a = float(input("Birinci rəqəmi daxil edin: "))
        b = float(input("İkinci rəqəmi daxil edin: "))
        əməliyyat = input("Əməliyyatı daxil edin (toplama, çıxma, vurma, bölmə): ").strip()

        if əməliyyat == "toplama":
            print("Nəticə:", a + b)
        elif əməliyyat == "çıxma":
            print("Nəticə:", a - b)
        elif əməliyyat == "vurma":
            print("Nəticə:", a * b)
        elif əməliyyat == "bölmə":
            if b == 0:
                print("0-a bölmək olmaz.")
            else:
                print("Nəticə:", a / b)
        else:
            print("Yanlış əməliyyat.")
    except ValueError:
        print("Rəqəm daxil edin.")
    except Exception as e:
        print("Xəta baş verdi:", e)
    finally:
        print("Hesablama bitdi")
hesabla()

1-dən 50-yə qədər olan rəqəmlərdən yalnız 11ə qalıqsız bölünənlərini list olaraq qaytarın.

bolunenler = [i for i in range(1, 51) if i % 11 == 0]
print(bolunenler)

Verilmiş sözlər siyahısından (["kitab", "qələm", "defter", "silgi"]) hər sözün ilk hərfini list olaraq qaytarın.

sozler = ["kitab", "qələm", "defter", "silgi"]
ilk_herfler = [s[0] for s in sozler]
print(ilk_herfler)

Şəhər adları (["Bakı", "Gəncə", "Sumqayıt"]) və kodları ([12, 22, 18]) siyahılarından {şəhər: kod} dictionary olaraq qaytarın.

seherler = ["Bakı", "Gəncə", "Sumqayıt"]
kodlar = [12, 22, 18]
seher_kod = dict(zip(seherler, kodlar))
print(seher_kod)

Kilometri milə çevirən (mil = km * 0.621371) lambda funksiyası yazın və 5 fərqli dəyər üçün yoxlayın.

km_to_mil = lambda km: km * 0.621371
dəyərlər = [1, 5, 10, 15, 20]
mil_nəticələr = list(map(km_to_mil, dəyərlər))
print(mil_nəticələr)

[100, 200, 300, 400] qiymətlərinə 18% vergi əlavə etmək üçün map() və lambda istifadə edin.

qiymetler = [100, 200, 300, 400]
vergi_əlavə = list(map(lambda x: x * 1.18, qiymetler))
print(vergi_əlavə)

[3, 7, 12] və [2, 4, 6] siyahılarının elementlərini ikiqat artırmaq və sonra cəmləmək üçün map() istifadə edin.

a = [3, 7, 12]
b = [2, 4, 6]
cem = list(map(lambda x, y: (x * 2) + (y * 2), a, b))
print(cem)

[150, 80, 220, 45] siyahısından ən kiçik qiyməti reduce() ilə tapın.

from functools import reduce
reqemler = [150, 80, 220, 45]
en_kicik = reduce(lambda x, y: x if x < y else y, reqemler)
print(en_kicik)


