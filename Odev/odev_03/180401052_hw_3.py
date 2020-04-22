"""
İsim : FURKAN YAZGAN
Numara : 180401052
180401052 % 4 Değerinin Sonucu = 0
Kullanılan olasılık : 0 .Uniform Distribution

Uniform Distribution / Tekdüze Dağılım = Olasılık uzayındaki olayların herbirinin gerçekleşme
    olasılıklarının eşit olduğu, yani tüm olasılıkların tekdüze dağılım gösterdiği bir olasılık dağılımı türüdür.

Bu dağılım için olasılık yoğunluk fonksiyonu(probability density function) şu şekilde ifade edilir:

            |1 / (b - a)   ,  a <= x <= b
    f(x)=   |
            |     0        ,  x < a veya x > b

Piecewise methodu ile koşullu fonksiyonumuzu oluşturuyoruz.
syp.plot içinde fonksiyonu hazır olarak çizidiriyoruz.
plt.plot içinde ise fonksiyondaki x değerlerine karşılık gelen f(x)=y değerlerini buluyor
    ve bu veriler baz alınarak fonksiyon çizimi yapıyoruz.
    Burada grafiği idealine daha yakın/benzer yapmak için x'in artış değerlerini olabildiğince küçülttük.
"""
import sympy as sym
from sympy import Symbol,Piecewise,pprint
import sympy.plotting as syp
import matplotlib.pyplot as plt
import numpy as np

a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
fonksiyon = 1/(b-a)

pprint(fonksiyon)

def graphic_with_matplotlib():
    while True:
        lower = 3
        upper = 6
        if lower > upper:

            continue
        else:
            x_values = []
            y_values = []
            for value in np.arange(-10,30,0.1):
                if lower<=value and upper>=value:
                    y = fonksiyon.subs({a:lower, b:upper ,x:value}).evalf()
                    y_values.append(y)
                    x_values.append(value)
                else:
                    y_values.append(0)
                    x_values.append(float(value))
            plt.plot(x_values,y_values)
            plt.show()
        break
graphic_with_matplotlib() #matplotlib ile grafiği çizdiriyor.


def graphic_with_sympy():
    while True:
        n = 3
        v = 6
        if n > v:

            continue
        else:  # syp.plot ile grafiği çizdiriyor.
            syp.plot(Piecewise((0, (x < n) | (x > v)), (fonksiyon.subs({a: n, b: v}), (x >= n) & (x <= v))),
                     (x, -10, 10), title="uniform distribution")

        break


graphic_with_sympy()