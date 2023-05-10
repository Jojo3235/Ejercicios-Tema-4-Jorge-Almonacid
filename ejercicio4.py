# Desarrollar un algoritmo numérico iterativo que permita calcular el método de la bisección de una función f(x).

# Desarrollar un algoritmo numérico iterativo que permita calcular el método de la secante de una función f(x).

# Desarrollar un algoritmo numérico iterativo que permita calcular el método de Newton-Raphson de una función f(x).

#  Comparar los tres algoritmos anteriores para resolver la siguiente función: x3 + x +16 = 0, respecto de la cantidad de iteraciones necesarias por cada método para converger. ¿Cuánto es la diferencia en decimales entre las distintas soluciones?

import math
def bisection(f, x_a, x_b, eps=None, steps=10):
    # The bisection method cannot be applied
    if fun(x_a) * fun(x_b) >= 0:
        print("The bisection method cannot be applied")
        return None
    
    # Calculate number of stepds base on eps
    if eps is not None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
    # The bisection method
    for n in range(steps + 1):
        x_m = (x_a + x_b) / 2
        
        if f(x_m) == 0:
            return x_m
        
        if f(x_a) * f(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
    
    return (x_a + x_b) / 2

def secant(fun, x_a, x_b, steps=50):
    # El método de la secante no se puede aplicar
    if fun(x_a) * fun(x_b) >= 0:
        print('El método de la secante no se puede aplicar')
        return None
    
    # El método de la secante 
    for n in range(steps + 1):
        # Cálculo de la secante
        x_n = x_a - fun(x_a)*(x_b - x_a)/(fun(x_b) - fun(x_a))
        
        if fun(x_n) == 0:
            return x_n
        
        if fun(x_a) * fun(x_n) < 0:
            x_b = x_n
        else:
            x_a = x_n
    return x_n

def newton_raphson(f, f_prime, x_0, eps=None, steps=10):
    # Calculate number of stepds base on eps
    if eps is not None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
    # The newton-raphson method
    for n in range(steps + 1):
        x_m = x_0 - f(x_0) / f_prime(x_0)
        
        if f(x_m) == 0:
            return x_m
        
        x_0 = x_m
    
    return x_m

def fun(x):
    return x**3 + x + 16

def main():
    print("Bisección")
    print(bisection(fun, -10, 10))
    print("Secante")
    print(secant(fun, -10, 10))
    print("Newton-Raphson")
    print(newton_raphson(fun, lambda x: 3*x**2 + 1, 10))
    print(f"diferencia entre bisección-secante: {bisection(fun, -10, 10) - secant(fun, -10, 10)}")
    print(f"diferencia entre bisección-newton: {bisection(fun, -10, 10) - newton_raphson(fun, lambda x: 3*x**2 + 1, 10)}")
    print(f"diferencia entre secante-newton: {secant(fun, -10, 10) - newton_raphson(fun, lambda x: 3*x**2 + 1, 10)}")

if __name__ == "__main__":
    main()