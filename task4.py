#В базе одного магазина электроники есть список видеокарт компании NVIDIA разных поколений. Для удобства в списке вместо полных
#названий хранятся только числа, они обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт,
#и в итоге самые старшие поколения разобрали за пару дней.
#Напишите программу, которая удаляет из этого списка видеокарт наибольшие элементы.
#Пример:

#Кол-во видеокарт: 5
#1 Видеокарта: 3070
#2 Видеокарта: 2060
#3 Видеокарта: 3090
#4 Видеокарта: 3070
#5 Видеокарта: 3090

#Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
#Новый список видеокарт: [ 3070 2060 3070 ]

a_list = []
a=0
n=int(input("Кол-во видеокарт: "))
while (a<n):
 a_list.append(int(input()))
 print(a+1,"Видеокарта:", a_list[a])
 a=a+1
print(a_list)
b_list = []
c=int(3090)
for x in a_list:
  if x<c:
    b_list.append(x)
print(b_list)