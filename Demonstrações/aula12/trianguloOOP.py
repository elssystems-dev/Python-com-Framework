class triangulo:
    # Atributos
    a:int
    b:int
    c:int

    def area(a, b, c):
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p- c))
        return area