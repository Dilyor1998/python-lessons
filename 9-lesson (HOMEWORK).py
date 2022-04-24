# # 9-Lesson (Homework)

# ichimliklar = ['aroq','kola','piva','kanyak','vino']
# for ichimlik in ichimliklar:
#     print(f"{ichimlik} ichish zarar tashang\n")
# print("yuqorida sikl 5 marta takrorlarndi")


# toq_sonlar = range(11,100,2)
# for toq in toq_sonlar:
#     print(f"{toq ** 3} \n")


# kinolar = []
# print("5 ta eng sevimli kinoni kiriting")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1} - kinoni nomi nima: "))
# print(f"sizning sevimli konlaringiz\n {kinolar}\t")
 

# nechta = int(input("bugun nechta odam bn suhbatlashdingiz "))
# ismlar = []
# for sum in range(nechta):
#     ismlar.append(input(f"{sum+1} ning ismi kim edi "))
# print(ismlar)


# a = int(input("nechta kampyuter olishni xoxlaysiz ? "))
# kamp = []
# for sum in range(a):
#     kamp.append(input(f"{sum+1} nomi qanaqa"))
# print(kamp)


# a = int(input("1 dan nechigacha sonlar chiqishini xoxlaysiz "))
# sonlar = []
# for sum in range(a):
#     print(sum+1)


# print("sonlar kvadratini nechidan nechigacha chiqarishni xoxlaysiz ")
# a = int(input("nechidan boshlansin? "))
# b = int(input("nechigacha ? "))
# for sum in range(a,b):
#     print(f"{sum} {sum**2}")

# print("sizda 100.000 som bor")
# pul = 100000
# tel = []
# a = int(input("nechta telefon olishni xoxlaysiz "))
# for n in range(a):
#     tel.append(input(f"{n+1} telning nomi qanaqa "))
#     b = int(input("narxi qancha? "))
#     a = pul - b
#     if a < b:
#         print("sizda pul yetmaydi")