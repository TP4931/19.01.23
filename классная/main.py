#Определите среднее значение всех элементов последовательности, завершающейся числом 0.
x=1
y=0
d=0#количество
while x!= 0:
    x=int(input())
    y=y+x
    if x!=0:
        d = d+1
print(y/d)