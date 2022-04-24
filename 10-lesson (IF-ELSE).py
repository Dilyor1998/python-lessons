# # 10-lesson (IF ELSE)

# avtolar = ['audi','bmw','volvo','kia','hyundai']

# for avto in avtolar: # avtolar ichidagi har bir avto uchun ...
#     if avto == 'bmw': # agar avto bmw ga teng bolsa
#         print(avto.upper()) #bmw nomini hamma harfini katta harf bn chiqar
#     else: # aks holda
#         print(avto.title()) # avto nomini faqat 1-harfini katta bn chiqar
        

# ism = input("Ismingiz nima? \n>>> ") # foydalanuvchudan ismini soraymiz
# if ism.lower() != 'dilyor': # agar isim Dilyorga teng bolmasa
#     print(f"Uzur {ism.title()} biz Dilyorni kutyabmiz")
# else:
#     print("Salom Dilyor")

# # sonlar bilan ishlash


# javob = float(input("5 x 6 nechiga teng? "))
# if javob != 30: # agar teng bolmasa
#     print("javob xato")
# else:
#     print("javob tog'ri")

# yosh = int(input("Yoshingiz nechida "))
# if yosh >= 18: # katta yoki teng bolsa 
#     print("Mumkin")
# else: # aks holda
#     print("Mumkinmas")
    
# log = input("New login >>> ")
# if len(log) <= 5:
#     print("Login 5 xarfdan ko'p bo'lishi kerek")


# yil = int(input("Tug'ilgan yilingizni kiriting >> "))
# if 2022 - yil < 18:
#     print(f"Yoshingiz {2022 - yil} da ekan")
#     print("Sizga kirish mumkin emas!")
# else:
#     print("Xush kelibsiz ")