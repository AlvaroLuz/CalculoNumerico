from sympy import sympify, diff, Symbol, Rational, integrate
import math
interval=(2,5)
f = "sin((-sqrt(3)*(x**2))+2)"
class Quadratura:
    def __init__(self, interval, function):
        self.fTemp = sympify(function)
        
        self.f = lambda x : self.fTemp.subs(Symbol('x'), x)
        
        fintTemp = integrate(self.fTemp, Symbol('x'))
        
        self.fint = lambda x : fintTemp.subs(Symbol('x'), x)
        
        self.dx = Rational((interval[1]-interval[0])/2)
        self.a = interval[0]
        self.b = interval[1]
        
    def error(self):
        print()
        integral = round(self.fint(self.b),7) - round(self.fint(self.a),7)
        erro = round(abs(integral-self.quadratura),7)
        print(f'erro = |{integral}-{self.quadratura}| = {erro}')
        print()
        return
    def quadratura (self):  
        t = "sqrt(3)/3"
        t = sympify(t)
        print(f't1 = 1/2 * ({self.a} + {self.b} + (-{t})*({self.b}-{self.a}))')
        print(f't2 = 1/2 * ({self.a} + {self.b} + ({t})*({self.b}-{self.a}))')
        f1 = self.f(1/2*(self.a+self.b + (-t)*(self.b-self.a)))
        f2 = self.f(1/2*(self.a+self.b +  t  *(self.b-self.a)))
        quadratura =self.dx*(round(f1,7)+round(f2,7))
        self.quadratura = round(quadratura,7)
        print(f'x =~ {self.dx}*({self.fTemp.subs(Symbol("x") , Symbol("t1"))}+{self.fTemp.subs(Symbol("x"),Symbol("t2"))}) = {self.quadratura}')
        self.error()
        return 
gauss = Quadratura(interval,f)
gauss.quadratura()
