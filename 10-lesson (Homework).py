# # 10 lesson (IF-ELSE)
# # Homework

cars = ['tayota','mazda','hyundai','gm','kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())


# name = input("Loginni kiriting >> ")
# if name == 'admin':
#     print(f"Foydalanuvchi royxatini korasizmi {name.title()}")
# else:
#     print(f"xush kelibsiz {name.title()}")


# a = int(input("1-sonni kiriting >> "))
# b = int(input("2-sonni kiriting >> "))
# if a > b :
#     print(f"{a} katta son")
# if b > a :
#     print(f"{b} katta son")
# else:
#     print(f"{a} va {b} teng")


# a = int(input("son kiriting >> "))
# if a > 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")


# a = float(input("Istalgan son kiriting >> "))
# if a > 0:
#     print(a ** (1/2))
# else:
#     print("Musbat son kiriting")


print("Nechi oyda MALIBU olar ekansiz xisoblab koramiz")
print("Malibu narxi 300.000.000 MLN so'm")
a =  int(input("oyligiz qancha? >> "))
if a == 5000000:
    print("Siz 5 yilda Malibu olasiz ")
elif a == 6000000:
    print("siz 4 yil 4 oyda Malibu olasiz")
elif a == 7_000_000:
    print("Siz 3 yilu 6 oyda Malibu olasiz")
elif a == 8_000_000:
    print("Siz 3 yil 1 oy 15 kunda Malibu olasiz ")
elif a == 9_000_000:
    print("Siz 2 yil 9 oyda Malibu olasiz")
elif a == 10_000_000:
    print("Siz 2 yil 6 oyda Malibu olasiz")
elif a >= 11_000_000:
    print("Siz yaqinda qamalasiz poro olmang chunki\n UZB da bunaqa oylik bermaydi")
else:
    print("Bilmadim endi ob qolarsiz")