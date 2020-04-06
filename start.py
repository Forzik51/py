import random
# a = 10  #int
# print(a, type(a))

# a = 10.6  #Float
# print(a, type(a))

# a = True  #bool
# print(a, type(a))

# a = "Bill"  #str
# print(a, type(a))


# name = input("Your name")
# age = int(input("Your age"))
# print(name, type(name))
# print(age, type(age))

# if a > b and b > c:
#     print("a")
# elif a > b or

# km = int(input("Your km"))
# met = km * 1000
# print(met)

# suma = int(input("Your suma"))
# valuta = int(input("Your valuta \n 1 = $ \n 2 = eur \n 3 = rur"))
# kurs = int(input("Your kurs"))
# if valuta == 1:
#     print(suma / kurs)
# elif valuta == 1:
#     print(suma / kurs)
# elif valuta == 1:
#     print(suma / kurs)

# shlah = int(input("Your shlax"))
# palne = int(input("Your palne"))
# cina = int(input("Your cina"))
# print(suma / kurs)

# a = random.randrange(-20, 10)
# print(a)
# b = random.randrange(-20, 10)
# print(b)
# c = random.randrange(-20, 10)
# print(c)

# if a == b and a == c:
#     print("rivni")
# elif a != b and a != c:
#     print("ne rivni")

# exit = False

# while not exit:
#     a = int(input("1 number"))
#     b = int(input("2 number"))
#     chois = int(input("1. Add\n2. min\n.3 Div\n4. mno\n5. Exid\n"))
#     if chois == 1:
#         print(a+b)
#     elif chois == 2:
#         print(a-b)
#     elif chois == 3:
#         print(a/b)
#     elif chois == 4:
#         print(a*b)
#     elif chois == 5:
#         exit = True

god = int(input("enter god"))

if god > 23 and god <= 24 or god >= 0 and god < 6:
    print("good night")
elif god > 9 and god <= 20:
    print("good day")
elif god > 20 and god <= 23:
    print("good evening")
elif god >= 6 and god <= 9:
    print("good morning")

exit = False
while not exit:
    chois = int(input("1. в дюйми\n2. в сантиметри\n3. Exid\n"))
    a = int(input("enter number"))
    if chois == 1:
        print(a / 2.54)
    elif chois == 2:
        print(a * 2.54)
    elif chois == 3:
        exit = True

exitt = False
while not exitt:
    chois = int(input("1. в градуси\n2. в варингейт\n3. Exid\n"))
    t = int(input("enter number"))
    if chois == 1:
        print((t - 32) * 5/9)
    elif chois == 2:
        print((t * 9/5) + 32)
    elif chois == 3:
        exitt = True


a = random.randrange(-20, 10)
b = random.randrange(-20, 10)
c = random.randrange(-20, 10)
d = random.randrange(-20, 10)
e = random.randrange(-20, 10)
f = random.randrange(-20, 10)
g = random.randrange(-20, 10)
h = random.randrange(-20, 10)
dob = a * b * c * d * e * f * g * h
suma = a + b + c + d + e + f + g + h
print("dob =>",dob)
print("ar =>", suma / 8)


max = -20
min = 100
for number in range(7):
    t = random.randint(-10, 30)
    print("T: ", t)
    if max < t:
        max = t
    if min > t:
        min = t
print("Count =", max)
print("Count =", min)