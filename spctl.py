import math as np
print("hello")
agree = 31 * np.pi / 64
a1 =  -1 * np.pi / 2
y11 = 0
x11 = -13
n = 3


x12 = 13 * (np.tan(agree) - np.tan(agree * 2 - a1)) / (np.tan(agree) + np.tan(2 * agree - a1))
y12 =  -1 * np.tan(agree) * (x12 - 13)

print("x12 ", end = "")
print(x12)
print("y12 ", end = "")
print(y12)

a2 = a1 - 4 * agree
x21 =  (-1 * 13 * np.tan(agree) - x12 * np.tan(a2) + y12) / (np.tan(agree) - np.tan(a2))
y21 =  np.tan(agree) * (x21 + 13)
x22 =  (13 * np.tan(agree) + x21 * np.tan(2 * agree - a2) - y21) / (np.tan(agree) + np.tan(2 * agree - a2))
y22 =  -1 * np.tan(agree) * (x22 - 13)
count = 0
for var in range(0, n):
    a2 = a1 - 4 * agree
    x21 =  (-1 * 13 * np.tan(agree) - x12 * np.tan(a2) + y12) / (np.tan(agree) - np.tan(a2))
    y21 =  np.tan(agree) * (x21 + 13)
    x22 =  (13 * np.tan(agree) + x21 * np.tan(2 * agree - a2) - y21) / (np.tan(agree) + np.tan(2 * agree - a2))
    y22 =  -1 * np.tan(agree) * (x22 - 13)

    print("")
    print("-------", end = "")
    print(a2, end = "")
    print(np.tan(a2))
    print("x", end = "")
    print(count + 2, end = "")
    print("1 ", end = "")
    print(x21)
    print("y", end = "")
    print(count + 2, end = "")
    print("1 ", end = "")
    print(y21)
    print("x", end = "")
    print(count + 2, end = "")
    print("2 ", end = "")
    print(x22)
    print("y", end = "")
    print(count + 2, end = "")
    print("2 ", end = "")
    print(y22)

    a1 = a2
    x11 = x21
    x12 = x22
    y11 = y21
    y12 = y22

    count += 1

