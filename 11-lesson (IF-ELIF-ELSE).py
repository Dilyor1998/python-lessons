# # 11- lesson (IF-ELIF-ELSE)

# yosh = int(input("Yoshingiz nechida? >> "))
# if yosh <= 4:
#     print("Sizga kirish tekin")
# elif yosh <= 12:
#     print("Sizga kirish 5.000 so'm")
# else:
#     print("Sizga kirish 10.000 so'm")


# yosh = int(input("Yoshingiz nechida? >> "))
# if yosh <= 4:
#     sum = "bepul"
# elif yosh <= 12:
#     sum = 5000
# elif yosh <= 18:
#     sum = 8000
# else:
#     sum = 10000
# print(f"Sizga kirish {sum} so'm")

## or yoki mantiqi operatori
## and va mantiqi operatori


# kun = input("Bugun qaysi kun? >> ")
# if kun.lower() ==  'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugin ish kuni ")

# kun = input("Bugun qanaqa kun? >> ")
# temp = float(input("Pagoda qanaqa? >> "))
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba' and temp >= 32.5:
#     print("Bgun dam olish kuni \nKetdik cho'milishga")
# elif kun.lower() == 'shanba' or kun.lower() == 'yakshanba' and temp <= 30:
#     print("Bugun dam olish kuni lekin\ncho'milishga bormimiz kun sovuq5")
# else:
#     print("Bugun ish kuni ishga boramiz")

    
# # boolen (True) yoki (False) qaytaradi


# narh = 15000 # mijoz 15000 so'mga taom oldi 
# choy = True # mijoz cho'y sotin oldi
# salat = True # mijoz salat sotin olmadi
# if choy and salat: #mijoz choy va salat sotil olgan bolsa 
#     narh = narh + 10000 # narhga 10.000 so'm qoshamiz
# elif choy or salat: # agar choy yoki salat olgan bolsa 
#     narh = narh + 5000 # narhga 5000 so'm qoshamiz
# print(f"Jami {narh} so'm")


# narh = 15000 # mijzo 15000 so'mga ovqat oldi
# choy = True # 1 yoki 0 qoysa xam boladi
# salat = False # 1 yoki 0 qoysa xam boladi
# kampot = True   # 1 yoki 0 qoysa xam boladi
# non = True # 1 yoki 0 qoysa xam boladi
# assorti = False # 1 yoki 0 qoysa xam boladi
# # quydagi har bir shart alohida tekshiriladi
# if choy: # agar choy olsa
#     print("Mijoz choy oldi\n")
#     narh += 3000
    
# if salat: # agar salat olsa
#     print("Mijoz salat oldi\n")
#     narh += 5000
    
# if kampot: # agar kampot olsa
#     print("Mijoz kompot oldi\n")
#     narh += 10000
    
# if non: # agar non olsa
#     print("Mijoz non oldi\n")
#     narh += 2000
    
# if assorti: # agar assorti olsa
#     print("Mijoz kompot oldi\n")
#     narh += 25000
    
# print(f"sizning xisobingiz {narh} so'm boldi")
    

# in ichida bormi degan manoni beradi 
# menu = ['somsa','palov','kabob','norin','sok','shashlik']
# # 'manti' in menu # menuda manti bormi ? degan manoda 
# ovqat = input("nima ovqat yiysiz? >> ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Bunday ovqat yo'q")    
    
# # not in yoqlikka tekshiradi

# menu = ['somsa','palov','kabob','norin','sok','shashlik']
# # 'manti' in menu # menuda manti bormi ? degan manoda 
# ovqat = input("nima ovqat yiysiz? >> ")
# if ovqat.lower() not in menu:
#     print("Bunday ovqat yo'q")    
# else:
#     print("Buyurtma qabul qilindi")
   
   
# solishtrish ?

# menu = ['somsa','palov','kabob','norin','sok','shashlik']
# buyurtmalar = ['osh','somsa','manti','kabob']  
# for taom in buyurtmalar: # buyurtma ichidagi har bir taom
#     if taom in menu:# agar menuda osha taom bolsa bolsa 
#         print(f"Menuda {taom} bor\n") # taom bor deb chiqar
#     else: # aks holda 
#         print(f"Kechirasiz menuda {taom} yo'q\n") # taom yoq deb chiqar 