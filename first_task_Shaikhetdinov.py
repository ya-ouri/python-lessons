def Dekorator(Uskorenie):
    def obertka():
       Uskorenie(v, v_0, t)
       s = v * t
       print(s)
    return obertka
def Uskorenie(v, v_0, t):
    a = (v - v_0)/t
    return print(a)
try:
    v = int(input('v'))
    v_0 = int(input("v_0"))
    t = int(input("t"))

except ZeroDivisionError:
    print("t = 0!")


Uskorenie = Dekorator(Uskorenie)
Uskorenie()