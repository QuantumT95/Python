def printsquare(n, s):
  i = 0
  while (i < n):
    print(s*(2*n))
    i += 1

n = int(input("this is n: "))
s = input("this is s: ")

printsquare(n, s)





def linear(m, b):
  for i in range(-10, 11):
    y = float(m*x)+b
    print(i, y)

slope = float(input("Enter a slope: "))
b = float(input("Enter a y-intercept: "))

linear(slope, b)