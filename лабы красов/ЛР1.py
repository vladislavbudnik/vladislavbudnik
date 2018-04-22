import math

print("Enter coef for sqrt the equation")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

dis = b ** 2 - 4 * a * c
print("Discriminant D = %.2f" % dis)
if (dis > 0):
    x1 = (-b + math.sqrt(dis)) / (2 * a)
    x2 = (-b - math.sqrt(dis)) / (2 * a)
    print("x1 = %.2f\nx2 = %.2f" % (x1, x2))
elif (dis == 0):
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Nope sqrt")
