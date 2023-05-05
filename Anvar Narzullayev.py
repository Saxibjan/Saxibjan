import cars as cars

print("5-lesson. Matn bilan ishlash. 22/03/2023")
# ism = "Sohibjon"
# familiya = "Hakimov"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)
# print(ism)
# f-string
# print(f"Salom mening ismim {familiya}. {ism} {familiya}!")

# Unicode character table - This is useful website.

# print("Hello world")
# print("Hello \tworld") # ozroq joy taylash
# print("Hello \nworld") # bitta uzun qator pastga taylash

# print(ism_sharif.upper()) # hamasini katta harflarda yozdiradi
# print(ism_sharif.lower()) # hamma harflarni kkichkina formatda yozdiradi
# print(ism_sharif.title()) # all sentence's words is large
# print(ism_sharif.capitalize()) # only first sentence"s first words is large not all

# meva = "   olma   "
# print(meva)
# print("Men " + meva.lstrip() + " yaxshi ko'raman") # remove right text's space
# print("Men " + meva.rstrip() + " yaxshi ko'raman") # remove left text's space
# print("Men " + meva.strip() + " yaxshi ko'raman") # remove all of the above space in around text
# print("Men " + meva + " yaxshi ko'raman")

# ism = input("Ismingiz nima?\n>>>")
# print("Assalomu alekum " + ism.title


print("6-lesson. Sonlar bilan ishlash. 23/03/2023")
# 553_363_333
# 54.454
# aholi_soni = 7_987_342_232
# print("Aholi soni:",aholi_soni)
# x, y, d = 5, 3, 4
# print(x, d, y)
# ism = "Sohibjon"
# yosh = 19
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)
# print(type(ism))
# print(type(yosh))
# t_yil = int(input("Tug'ilgan yilingizni kiriting"))
# yosh = 2023 - t_yil
# print("Siz " + str(yosh) + " da ekansiz")


print("6-lesson's practise")
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# print("a+b=", a+b)
# print("a-b=", a-b)
# print("axb=", a*b)
# print("a/b=", a/b)


print("7-lesson. Lists. 26/03/2023")
#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'olma']
#print(mevalar)
#narxlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
#print(narxlar)
#sonlar = ['bir', 'ikki', 3, 4, 5]
#ismlar = []

# mevalar [o] = 'anor' --- things changing
# mevalar.append("") --- this method is include only at the end
# mevalar.insert(3, "ananas") --- you can include things by this method which you want to anywere
# del meevalar[1] --- this method can delite you enter things
# mevalar.remove("anjir") --- if you don't know things index you can only write things by remove method without index
# Addiction, this candlelit first thing if there are two or more thingd in the list.
# mahsulot = mevalar.pop() or .pop(1) --- this can extract element and you may or not ask index.

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop()
# print("Men " + mahsulot + " oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

#narhlar = [12000, 18000, 10900, 22000]
#narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
#narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
#narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
#print(narhlar)


# print("7-lesson's practise")
# ismlar = ['Sindor', 'Afzal', 'Sheroz', 'Bekzod']
# print("Salom " + ismlar[0] + " Bugun gashtak bormi?")
# print(ismlar[1] + " bugun gashtakga 32 talikni olib kel!")
# print("Bugun gashtak. " + ismlar[-1] + " 50 000 qarz berib tura olasanmi?")

# sonlar = [1200, 1400, 3500, -650, 64.02]
# sonlar [0] = sonlar[0] + 2000
# sonlar.append(22000)
# sonlar.insert(2, 23000)
# del sonlar[3]
# print(sonlar)

# t_shaxslar = ['Alisher Navoiy', 'Imom Buxoriy', 'Amir Temur', 'Zahiriddin Muhammad Bobur']
# z_shaxslar = ['Shavkat Mirziyoyev', 'Abror Muxtor ali', 'Bill Gates']
# tarixiy = t_shaxslar.pop(1)
# zamonaviy = z_shaxslar.pop(-1)
# print("Men tarixiy shaxslardan " + tarixiy + " bilan, \nzamonaviy shaxslardan esa " + zamonaviy + " bilan suhbat qurishni istar edim." )

# friends = []
# friends.append("sheroz")
# friends.append("Afzal")
# friends.append("John")
# friends.append("Diyor")
# friends.append("Sidor")
# friends.append("Anton")
# friends.remove("Diyor")
# friends.remove("John")
# friends.append("Adash")
# print(friends)
#
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)


print("8-lesson. Sonlar bilan ishlash. 28/03/2023")

# narxlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
# narxlar.sort(reverse =True) #reverse sorting.
# print(narxlar)
#
# mevalar = ['Olma', 'anjir', 'shaftoli', "o'rik", 'olma']
# mevalar.sort() #simple sorting
# print(sorted(mevalar))
#
# sonlar = [2, 5, 56, 23, 56, -45.3, -47.2, 236_463_32]
# sonlar.reverse() # this method can only make reverse.
# print(len(sonlar)) #len it can count all elements in the box
# sonlar = list(range(0, 11)) #it can make how to you want list
# print(sonlar)
#
# juft_sonlar = list(range(0, 20, 2))
# print(juft_sonlar)
# toq_sonlar = list(range(1, 10, 2))
# print(toq_sonlar)
#
# cars = sonlar[:]
# print(cars)
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# toys = list(toys)
# toys.append('deddy')
# print(toys)

print("8-lesson's practise")
# country = ['Egypt', 'Germany', 'Swiden', 'America', 'Russio', 'Uzbekistan', 'Latvia']
# print("Country's member= ", len(country))
# print(sorted(country))
# print(sorted(country, reverse=True))
# print(country)
# country.reverse()
# print(country)
# country.sort()
# print(country)
# country.sort(reverse=True)
# print(country)
# j_sonlar =list(range(120,1200,2))
# print(j_sonlar)
# print(sum(j_sonlar))
# print(max(j_sonlar)-min(j_sonlar))
# print(len(j_sonlar))
# print(j_sonlar[:20])
# print(j_sonlar[-20:])
# print(j_sonlar[530:550])
# taomlar = ['palov', 'halisa', "sho'rva", 'shashlik', 'grechka']
# nonushta = taomlar
# print(taomlar)
# nonushta.append('xurmo')
# nonushta.append('salat')
# nonushta.remove('grechka')
# nonushta.remove('shashlik')
# nonushta = tuple(nonushta)
# print(nonushta)


print("9-lesson. For takrorlash operatori-Tsikl. ")
#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
#for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, sizni 20-dekabr kuni nahorga oshga taklif qilamiz")
#    print('Hurmat bilan Palonchilar oilasi\n')

#sonlar = list(range(1,11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng")

#sonlar = list(range(11))
#sonlar_kvadrati = [] # it helpful for us in order to we don't want repeat sentences.
#for son in sonlar:  #FOR avtomatic repeating
#    sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print("5-ta eng yaqin do'stingizni kiriting")
#for n in range(5):
#    dostlar.append(input(f"{n + 1} Do'stingizning ismini kiriting:"))
#print(dostlar)


print("9-lesson's practise 1/04/2023")
#ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Husan', 'Odil']
#for ism in ismlar:
#    print(f"Assakomu alekum, {ism} sahifamizga xush kelibsiz")
#print(f'Kod {len(ism)}marta takrorlandi')

#sonlar = list(range(11, 100, 2))
#for son in sonlar:
#    print(son**3)

#kinolar = []
#print("5 ta eng sevimli kinoingizni kiriting?")
#for k in range(5):
#    kinolar.append(input(f"{k+1}-kino:"))
#print(kinolar)

#n_people = int(input("Bugun necha kishi bilan suhbat qurdingiz?>>>"))
#ismlar = []
#print("Bugun necha kishi bn suhbat qurdingiz?>>>")
#for n in range(n_people):
#    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:"))
#print(ismlar)


print("10-lesson. IF-ELSE 03/04/2023")
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car != 'gm':
#        print(car.upper())
#    else:
#        print(car.title())


print("10-lesson's practise 08/04/2023")
#login = input("Login kiriting: ")
#if login.lower() == "admin":
#    print("Xush kelibsiz Admin. Foydalanuvchilar ro'yxatini ko'rasizmi? ")
#else:
#    print(f"Xush kelibsiz {login.title()}")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"Sonlar teng: {x}={y}")

# son = float(input("Istalgan sonni kiriting:"))
# print("Manfiy son") if son>0 else print("Musbat son")

# son = float(input("Istalgan sonni kiriting:"))
# print(son**(1/2)) if son>0 else print("Musbat son kiriting: ")


print("11-lesson. Bir nechta shartlarni tekshirish 08/04/2023")
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5_000
# elif yosh<=65:
#     price = 10_000
# elif yosh>=65:
#     price = 8_000
# print(f"Sizga kirish {price} so'm")


# kun = input("Bugun qanday kun? ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bigun ish kuni")


# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")


# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi

# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz

# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz


# narh = 15000  # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# # Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:  # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:  # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:  # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:  # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
#
# print(f"Jami {narh} so'm")


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')


# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]
#
# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")


print("lesson's practise 08/04/2023")
# son = float(input("Juft son kiriting: "))
# if son%2:
#     print("Bu son juft emas")
# else:
#     print("Rahmat")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4 or yosh>=60:
#     price = 0;
# elif yosh<18:
#     price = 10_000;
# else:
#     price = 20_000;
# print(f"Sizning chiptangiz narxi {price}")

# x = float(input("Birinchi sonni kiriting? "))
# y = float(input("Ikkinchi sonni kirirting? "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ["anor", 'uzum', 'olma', 'tarvuz', 'shaftoli',  'o\'rik', 'ananas', 'xurmo', 'anjir', 'gilos']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# bor_mahsulotlar = []
# mavjud_emas = []
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
#     else:
#         print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
#
# foydalanuvchilar = ['Sohibjon', 'anvar', 'Komil', 'so\'rob', 'Anusher']
# login = input("Yangi login tanlang:")
# if login in foydalanuvchilar:
#     print("Login band, yangi login tanlang")
# else:
#     print(f"Xush kelibsiz {login.title()}!")
#
# butun_son = int(input("istalgan butun son kiriting"))
# for n in range(2,11):
#     if not (butun_son%n):
#         print(f"{butun_son} soni {n} ga qoldiqsiz bo'linadi")

# mahsulotlar = ["anor", 'uzum', 'olma', 'tarvuz', 'shaftoli',  'o\'rik', 'ananas', 'xurmo', 'anjir', 'gilos']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
#
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
# import math
# from turtle import*
# def hearta(k):
#     return 15*math.sin(k)**3
# def heartb(k):
#     return 12*math.cos(k)-5*\
#         math.cos(2*k)-2*\
#         math.cos(3*k)-\
#         math.cos(4*k)
# speed(0)
# bgcolor ("black" )
# for i in range (6000):
#     goto(hearta(i)*20,heartb(i)*20)
#     for j in range(5):
#         color ("red")
#     goto(0, 0)
# done()

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")

a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1

    if b == 210:
        break
    t.hideturtle()

turtle.done()