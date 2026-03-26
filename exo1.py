import math
def f(x):
    return math.exp(x)+3*(x**(1/2))-2
def trouver_intervalle(debut, fin, pas):
    x = debut
    i = 0
    while abs(f(x)-f(x+pas)) > pas and x < fin:
        if f(x)*f(x + pas) < 0:
            x = x
        else:    
            x += pas
            i = i+1
            print(i)
            print(x ,x+pas ,"f(x)=" ,f(x))
    return None
     
intervalle = trouver_intervalle(0, 10, 0.001)
