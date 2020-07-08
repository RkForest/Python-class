

hrs = input("Enter Hours:")
h= float(hrs)
rate = input("Rate:")
r = float(rate)

if h > 40 :
    p = (h-40)*r*1.5 + 40*r
else:
    p = h*r

print(p)

