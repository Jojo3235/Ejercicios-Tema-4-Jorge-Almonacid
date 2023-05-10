import math

def bisection(f, x_a, x_b, eps=None, steps=50):
    # Verifica si el método de la bisección puede aplicarse
    if f(x_a) * f(x_b) >= 0:
        print("El método de la bisección no se puede aplicar.")
        return None
    
    # Calcula el número de pasos en base a eps
    if eps is not None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
    # Implementa el método de la bisección
    for n in range(steps + 1):
        x_m = (x_a + x_b) / 2
        
        if f(x_m) == 0:
            return x_m
        
        if f(x_a) * f(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m
    
    return (x_a + x_b) / 2

def secant(f, x_a, x_b, steps=10000):
    # Verifica si el método de la secante puede aplicarse
    if f(x_a) * f(x_b) >= 0:
        print("El método de la secante no se puede aplicar.")
        return None
    
    # Implementa el método de la secante
    for n in range(steps + 1):
        # Calcula la secante
        x_n = x_a - f(x_a)*(x_b - x_a)/(f(x_b) - f(x_a))
        
        if f(x_n) == 0:
            return x_n
        
        if f(x_a) * f(x_n) < 0:
            x_b = x_n
        else:
            x_a = x_n
    
    return x_n

def newton_raphson(f, f_prime, x_0, eps=None, steps=50):
    # Calcula el número de pasos en base a eps
    if eps is not None:
        steps = math.ceil(math.log(abs(eps)) / math.log(10))
    
    # Implementa el método de Newton-Raphson
    for n in range(steps + 1):
        x_m = x_0 - f(x_0) / f_prime(x_0)
        
        if f(x_m) == 0:
            return x_m
        
        x_0 = x_m
    
    return x_m

def main():
    f = lambda x: x**5 + x**3 + x + 16
    f_prime = lambda x: 5*x**4 + 3*x**2 + 1
    f_2 = lambda x: x**3 + x + 16
    f_2_prime = lambda x: 3*x**2 + 1
    print("Bisección")
    print(bisection(f_2, -10, 10))
    # print(bisection(f, -10, 10))
    
    print("Secante")
    print(secant(f_2, -10, 10))
    # print(secant(f, -10, 10))
    
    print("Newton-Raphson")
    print(newton_raphson(f_2, f_2_prime, 10))
    # print(newton_raphson(f, f_prime, 10))

    # Imprimir la diferencia de los metodos
    print("Diferencia de los metodos")
    print("Biseccion - Secante")
    print(abs(bisection(f_2, -10, 10) - secant(f_2, -10, 10)))
    print("Biseccion - Newton-Raphson")
    print(abs(bisection(f_2, -10, 10) - newton_raphson(f_2, f_2_prime, 10)))
    print("Secante - Newton-Raphson")
    print(abs(secant(f_2, -10, 10) - newton_raphson(f_2, f_2_prime, 10)))

if __name__ == "__main__":
    main()