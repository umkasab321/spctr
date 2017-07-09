set title "this is test"
set grid
set xrange [-15.0:15.0]
set yrange [ -30.0:300.0]
set size ratio 10.0
set grid
agree = 31 * pi /64
a1 =  -1 * pi / 2
x11 = -8
y11 =  tan(agree) * (x11 + 13)
#y11 = 0
x12 =  (13 * tan(agree) + x11 * tan(2 * agree - a1) - y11) / (tan(agree) + tan(2 * agree - a1))
#x12 = 13 * (tan(agree) - tan(agree * 2 - a1)) / (tan(agree) + tan(2 * agree - a1))
y12 =  -1 * tan(agree) * (x12 - 13)
plot tan(agree) * (x + 13)
replot -1 * tan(agree) * (x - 13)
replot tan(2 * agree  - a1) * (x - x11) + y11
replot tan(a1 - 4 * agree) * (x - x12) + y12

a2 = a1 - 4 * agree
x21 =  (-1 * 13 * tan(agree) - x12 * tan(a2) + y12) / (tan(agree) - tan(a2))
y21 =  tan(agree) * (x21 + 13)
x22 =  (13 * tan(agree) + x21 * tan(2 * agree - a2) - y21) / (tan(agree) + tan(2 * agree - a2))
y22 =  -1 * tan(agree) * (x22 - 13)
replot tan(2 * agree  - a2) * (x - x21) + y21
replot tan(a2 - 4 * agree) * (x - x22) + y22

a3 = a2 - 4 * agree
x31 =  (-1 * 13 * tan(agree) - x22 * tan(a3) + y22) / (tan(agree) - tan(a3))
y31 =  tan(agree) * (x31 + 13)
x32 =  (13 * tan(agree) + x31 * tan(2 * agree - a3) - y31) / (tan(agree) + tan(2 * agree - a3))
y32 =  -1 * tan(agree) * (x32 - 13)
replot tan(2 * agree  - a3) * (x - x31) + y31
replot tan(a3 - 4 * agree) * (x - x32) + y32
pause -1
