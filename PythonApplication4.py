
def computepay(h,r):
    if h > 40 :
        p = (h-40)*r*1.5 + 40*r
    else:
        p = h*r
    return p

hrs = input("Enter Hours:")
h= float(hrs)
rate = input("Rate:")
r = float(rate)

p = computepay(h,r)

print("Pay",p)