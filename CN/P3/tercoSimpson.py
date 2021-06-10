from sympy import sympify, diff, Symbol, Rational
import math
intervalo=(4,8)
n = 8
f = "log(x+3)"
class Simp13m:
    def __init__(self, interval, function):

        self.fTemp = sympify(function)
        print(f"f(x) = {self.fTemp}")
        self.fdiffTemp = self.fTemp
        

        string_diff = "f" 
        for i in range(0, 4):
            string_diff += "'"
            self.fdiffTemp= diff(self.fdiffTemp,Symbol('x'))
            print(string_diff+f'(x) = {self.fdiffTemp}')
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

    def error(self,n):
        print()
        highest_fdiff = int (input(f"Digite o valor x no intervalo {self.interval} para o qual f''(x) apresenta o maior valor:"))
        erro = round( ( (self.interval[1]-self.interval[0]) * (self.h**4) * round(self.fdiff(highest_fdiff),7) )/180 ,7)
        print(f"erro =~ ({self.interval[1]}-{self.interval[0]})*(({self.h})^4)*{self.fdiff(highest_fdiff)})/180  = {erro}")
        print()
        return
    def simp13m (self,n):        
        print(f"h = ({self.interval[1]}-{self.interval[0]})")
        self.h = Rational((self.interval[1]-self.interval[0])/n).limit_denominator(100)
        print(f"h = {self.h}")
        print()

        print_string = f'x =~ ({self.h})/3*(({self.f(self.interval[0])})'
        sum = round(self.f(self.interval[0]),7)
        for i in range(1,n):
            if i%2 == 0:
                print_string += f'+2*({self.f(self.interval[0]+i*self.h)})'
                sum += 2*round(self.f(self.interval[0]+i*self.h),7)
            else:
                print_string += f'+4*({self.f(self.interval[0]+i*self.h)})'
                sum += 4*round(self.f(self.interval[0]+i*self.h),7)
        print_string += f'+({self.f(self.interval[1])}))'
        sum+= round(self.f(self.interval[1]),7)
        response = round(self.h * sum/3,7)
        print(f"{print_string} = {response}")
        
        self.error(n)
        return 
simpson = Simp13m(intervalo,f)
simpson.simp13m(n)
