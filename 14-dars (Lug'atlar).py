# 14-dars Dictionary (Lugat)
#Dilyor_Toxtabayev

# car_0 = {'model':'BMW','color':'blue'}
# print(car_0['model'])
# print(car_0['color'])


# en_uz = {'car':'Avtoulov','phone':'Telefon','nice':'yaxshi'}
# print(en_uz['car'])
# print(en_uz['phone'])
# print(en_uz['nice'])

# fruits = {'apple':'15000','oranje':'25000','grapes':'16000'}
# print(f"olmaning narhi {fruits['apple']} so'm")

# student = {'name' : 'dilyor toxtabayev' , 'age' : 24 , 'date' : 1998}
# print(f"{student['name'].title()},\
#       {student['date']}-yilda tug'ilgan,\
#       {student['age']} yoshda ")
      
# #yangi kalit soz va qiymat qo'shish
# student ['kurs'] = 4
# student ['fakultet'] = 'infarmatika'
# #kalit soz va qiymatni o'zgartrish
# student['name'] = 'donyor'

# # Bo'sh lug'at va uni toldirish

# students = {}

# students ['name'] = 'dilyor toxtabayev'
# students ['kurs'] = 2
# students ['age'] = 24
# print(students)
# print(f"Talaba {students['name'].title()} {students['kurs']}-kurs")

# # Kalit so'z-qiymatni o'chirib tashlash 

# student = {'name' : 'dilyor toxtabayev' , 'age' : 24 , 'date' : 1998}
# del student ['age'] # istalgan sozni kalit soz yordamida ochirib tashlash
# print(student)

# # royxatni bir necha qatorda yozish

# phones = {
#     'Dilyor':'Iphone 11 pro',
#     'Donyor':'Redmo 12 pro',
#     'Xamid':'Redmi 4X',
#     'Gulsara':'Galaxy A52'
#     }

# # # get () metodi

# phone = phones['Dilyor']
# print(f"Dilyorning telefoni {phone}")

# phone = phones.get('Shoxrux','Bunday ism mavjud emas') ## agar bunaqa ism bolmasa bu foydalanuvchuga kirinadi 
# print(phone)
