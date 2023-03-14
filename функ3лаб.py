#0
x1 = int(input("1-ші массивтегі элементтер саны: "))

m1 = []
m2 = []
m3 = []

for i in range(x1):
   m1.append((input()))

s1, s2, s3 = 0.0, 0.0, 0.0

for i in range(x1): #1ші массивтегі элементтер суммасы
   s1 += m1[i]

print("1 ші списоктың суммасы:", s1)
print("2 ші списоктың арифметикалық ортасы:", s1/x1)

x2 = int(input("\n2-ші массивтегі элементтер саны: "))
for j in range(x2):
   m2.append(int(input()))

for j in range(x2):
   s2 += m2[j]

print("2-ші списоктың суммасы:",s2)
print("2-ші списоктың арифметикалық ортасы:",s2/x2)

x3 = int(input("\n3-ші массивтегі элементтер саны: "))
for k in range(x3):
   m3.append(int(input()))

for k in range(x3):
   s3 += m3[k]

print("3-ші списоктың суммасы:",s3)
print("3-ші списоктың суммасы:",s3/x3)

#1
a = int(input())
b = int(input())
for i in range(a, b+1):
    print(i)

#2
a = int(input())
b = int(input())

if a < b:
  for i in range(a, b+1):
    print(i)
else:
     for i in range(a, b-1, -1):
        print(i)

#3
a = int(input())
b = int(input())
for i in range(a-int((a % 2) == 0), b-1, -2):
    print(i)

#4
n = int(input())
k = 0
for i in range(1, n+1):
    k += i
for i in range(n-1):
    k -= int(input())
print("Жоғалған карта: ", k)

#5
n = int(input())
k = 0
for i in range(1, n+1):
    k += i
for i in range(n-1):
    k -= int(input())
print("Жоғалған карта: ", k)
