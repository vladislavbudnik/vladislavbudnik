import math

x = float(input("Enter x:"))
y = float(input("Enter y:"))

x1 = -1
x2 = 3
y1 = -2
y2 = 1
k = 2
yc = 0
xc = 0
r =  2

if(y > k * x + b):
     if ((x - xc) ** 2 + (y - yc) ** 2 > r ** 2):
           print("Obl.1")
     elif (x1 < x < x2) and (y1 < y < y2):
           print("Obl.3")
     else:
           print("Obl.2")
elif((x - xc) ** 2 + (y - yc) ** 2 > r ** 2):
     if (x1 < x < x2) and (y1 < y < y2):
          print("Obl.7")
     else:           
          print("Obl.8")
elif  (x1 < x < x2) and (y1 < y < y2):
      print("Obl.4")
elif (y > y2):
      print("Obl.7")
else:
      print("Obl.8")
print("End")
