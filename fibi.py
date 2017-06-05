import turtle as tr
x,y=1,1
while x<500:
    z=x+y
    tr.circle(-x,90)
    tr.circle(-y,90)
    x,y=y,z
