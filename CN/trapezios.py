from sympy import Symbol, diff, sympify,Rational
import math

interval = (1,5)
function = "2/(x+1)"
n=6
erro = 1e-3
class TrapezoidRule:
    def __init__(self, interval, function):        
        self.fTemp = sympify(function)
        print(f"f(x) = {self.fTemp}")
        print(f"f'(x) = {diff(self.fTemp, Symbol('x'))}")
        
        self.fdiffTemp = diff(diff(self.fTemp,Symbol('x')),Symbol('x'))
        print(f"f''(x) = {self.fdiffTemp}")
        print()

        def f(x):
            fTemp = self.fTemp.subs(Symbol('x'), x)
            return fTemp
        def fdiff(x):
            fdiffTemp = self.fdiffTemp.subs(Symbol('x'), x)
            return fdiffTemp
        
        self.h = False
        self.f = f
        self.fdiff= fdiff
        self.interval = interval

    def error(self, n):
        highest_fdiff = int (input(f"Digite o valor x no intervalo {interval} para o qual f''(x) apresenta o maior valor:"))
        err = round(round(((self.interval[1]-self.interval[0])*(self.h**2))/12, 7)*round(self.fdiff(highest_fdiff),7),7)
        print(f"Erro obtido: {err}")
        return 

    def find_m(self,erro):
        highest_fdiff = int (input(f"Digite o valor x no intervalo {interval} para o qual f''(x) apresenta o maior valor:"))
        
        m = round(math.sqrt(((((interval[1]-interval[0])**3)*self.fdiff(highest_fdiff))/(12*erro))),7)
        print (m)
        print (f"m = {math.ceil(m)}")
        return

    def trapm(self, n):
        
        print(f"h = ({interval[1]}-{interval[0]})/{n}")
        self.h = Rational((interval[1]-interval[0])/n).limit_denominator(100)
        print(f"h = {self.h}") 
        print()
        
        print_string = f'x =~ ({self.h})/2*(({self.f(interval[0])})'
        
        soma = round(self.f(interval[0]),7)

        for i in range (1,n):
            print_string += f'+2*({self.f(interval[0]+i*self.h)})'

            soma += 2*round(self.f(interval[0]+i*self.h),7)

        print_string += f'+({self.f(interval[1])}))'

        soma += round(self.f(interval[1]),7) 

        response = round (self.h * soma/2,7)
        print(f"{print_string} = {response}")
        print()
        self.error(n)
        
        return

trapezoid = TrapezoidRule(interval, function)
#trapezoid.trapm(n)
trapezoid.find_m(erro)
