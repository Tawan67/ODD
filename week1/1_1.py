print("*** Rabbit & Turtle ***")
print("Enter Input : ",end='')
d, Vr, Vt, Vf = input().split(" ")
d = int(d)
Vr = int(Vr)
Vt = int(Vt)
Vf = int(Vf)
t=d/(Vt-Vr)
df=t*Vf
print("{:.2f}".format(df))