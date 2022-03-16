# Hana Farahdiana
# 20051397073
# Praktikum 1

import matplotlib.pyplot as plt
print ("masukkan nilai x1 : ")
x1 = int(input())
print ("masukkan nilai x2 : ")
x2 = int(input())
print ("masukkan nilai y1 : ")
y1 = int(input())
print ("masukkan nilai y2 : ")
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy) :
    steps = abs(dx)
else :
    steps = abs(dy)

xincrement = dx/steps
yincrement = dy/steps

i = 0

xcoordinates = []
ycoordinates = []

while i < steps:
    i +=1
    x1 = x1 + xincrement
    y1 = y1 + yincrement
    print("X1: ",x1,"Y1 :",y1)
    xcoordinates.append(x1)
    ycoordinates.append(y1)

plt.plot(xcoordinates, ycoordinates)

plt.xlabel("Garis X")
plt.ylabel("Garis Y")

plt.title("Algoritma DDA")

plt.show()