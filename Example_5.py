# Напишите программу, которая принимает на вход координаты двух точек и находит расстонияние между ними в 2D пространетсве
# Пример:
# A (3,6); B(2,1); -> 5,09
import math
print('Расстояние между двумя точками A и B')
x1 = input('Введите координату X точки A:')
y1 = input('Введите координату Y точки A:')
x2 = input('Введите координату X точки B:')
y2 = input('Введите координату Y точки B:')

def distance(x1,y1,x2,y2):
    try:
        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)
    except:
        print('Error: требуется ввести координаты точек')
        x1 = input('Введите координату X точки A:')
        y1 = input('Введите координату Y точки A:')
        x2 = input('Введите координату X точки B:')
        y2 = input('Введите координату Y точки B:')
        return distance(x1,y1,x2,y2)
    print(f'A({x1}{y1}); B({x2}{y2}); -> {round(math.sqrt((x2-x1)**2 + (y2-y1)**2),3)}')

distance(x1,y1,x2,y2)