#Определите количество четных элементов в последовательности, завершающейся числом 0.
x=int(input())
y=0
while x!=0:
    if x%2==0:
        y=y+1
    x=int(input())
print(y)