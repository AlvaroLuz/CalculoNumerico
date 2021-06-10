import math

def funcx(x):
    return math.e**(x**2) +math.sin(x) -3
def derivada(x): 
    return 2*x*math.e**(x**2) +math.cos(x) 

epsilon = 1e-6
x = -0.8

print("f(x):" + str (funcx(x)))
print("x:"+ str(x) )
xant = x
x = x - (funcx(x)/ derivada(x))
print("f(x):" + str (funcx(x)))
print("x:"+ str(x) )
while(abs(funcx(x))>epsilon):
    xant = x
    x = x -(funcx(x)/ derivada(x))   
    print("f(x):" + str (funcx(x)))
    print("x:"+ str(x) )