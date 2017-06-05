import turtle as tr
C=["yellow","orange","red","green","cyan","blue","purple"]
x,i=5,0
tr.width(5)
while x<200:
    tr.pencolor(C[i%7])
    tr.circle(-x,90)
    x+=5
    i+=1
