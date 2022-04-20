# # # 14-dars uyga vazifa 
# # # Lug'at 

# # 1-lesson
# family = {
#     'father':'Xamid','age': 51 , 'date':1971,'city':'beruniy',
#     'mather':'Gulsara','old' : 51 , 'datee':1972,'town':'beruniy'  
#     }

# print(f"otamning ismi {family['father']}, {family['date']}-yilda {family['city']} shaxarda tug'ilgan hozrda {family['age']} yoshda")
# print(f"onamning ismi {family['mather']}, {family['datee']}-yilda {family['town']} shaxrida tug'ilgan hozrda {family['old']} yoshda")

# # 2-lesson

# dishes = {
#     'Dilyor':'karchka borak',
#     'Donyor':'mayak borak',
#     'Dilafruz':'palov',
#     'Gulsara':'shashlik',
#     'Xamid':'kurtik'
#     }

# dish = dishes ['Xamid']
# print(f"Xamidning yaxshi korgan taomi {dish}")

# # 3-lesson


# dictionary = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat",
#     'del':'ochirish metodi',
#     'title':'brinchi xarfni katta qilish metodi'
#     }
# print(dictionary['title'])

# # # 4-lesson


# kalit = input("Kalit so'z kiriting:").lower()
# print(dictionary.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = dictionary.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")