#Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.

N = int(input("Введите N: "))
list1 = list(range(1, N+1, 2))
print(list1)