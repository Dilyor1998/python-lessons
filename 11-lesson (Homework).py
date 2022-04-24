# # 11-lesson (Homework)

# a = int(input("Juft son kiriting >> "))
# if a % 2 == 0:
#     print("Raxmat")
# else:
#     print("Bu juft son emas")

# a = int(input("Yoshingiz nechida? >> "))
# if a <= 4 or a >= 60:
#     print("Sizga kirish bepul")
# elif a < 18:
#     print("Sizga kirish 10.000 so'm")
# elif a >= 18:
#     print("Sizga kirish 20.000 so'm")


# print("2 ta son kiriting")
# a = float(input("1-sonni kiriting >> "))
# b = float(input("2-sonni kiriting >> "))
# if a > b:
#     print(f"{a} > {b}")
# elif b > a:
#     print(f"{a} < {b}")
# else:
#     print(f"{a} = {b}")

# print("5 ta mahsulot kiriting nima kerak ")
# mahsulotlar = ['nos','sok','anor','anjir','tel','cola','fanta','pepsi']
# savat = []
# for tavar in range(5):
#     savat.append(input(f"{tavar+1} kerak narsani kiriting >> "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"dukonda {mahsulot} bor")
#     else:
#         print(f"dukonda {mahsulot} yo'q")


# mahsulotlar = ['nos','sok','anor','anjir','tel','cola','fanta','pepsi']
# savat = []
# bor_mahs = []
# yoq_mahs = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni qoshing >> "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahs.append(mahsulot)
#     elif mahsulot not in mahsulotlar:
#         yoq_mahs.append(mahsulot)
        
# print(f"dukonimizda quydagi mahsulotlar yo'q{yoq_mahs}\n")
# print(f"dukonimizda quydagi mahsulotlar bor{bor_mahs}\n")
        

# login  = ['dilyorbek','donyorbek','azamatbek','xamidjon','shoxruxxon']
# a = input("Login kiriting >> ")
# if 8 > len(a):
#     print("8 ta harf bolishi kerak")
# elif a in login:
#     print("bunaqa mavjud")
# else:
#     print("xush kebsan")
        
        
# a = int(input("Istalgan butun son kiriting"))
# for b in range(2,11):
#     if a % b == 0:
#         print(f"{a} soni {b} ga qoldiqsiz bo'linadi")