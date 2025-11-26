import trianguloOOP as tl

# Instanciar a classe 
trianguloX = tl.triangulo()
trianguloY = tl.triangulo()

# Entrada de dados
print("Digite as medidas do triângulo X")

# ax = ... (no anterior)

# Entrada de dados
trianguloX.a = int(input("Digite a medida a: "))
trianguloX.b = int(input("Digite a medida b: "))
trianguloX.c = int(input("Digite a medida c: "))

trianguloY.a = int(input("Digite a medida a: "))
trianguloY.b = int(input("Digite a medida b: "))
trianguloY.c = int(input("Digite a medida c: "))

# Processamento de dados
areax = trianguloX.area()
areay = trianguloY.area()

# Condicional para verificar qual triângulo é maior
if areax > areay:
    saida = "A área do triângulo X é maior que a área do triângulo Y"
elif areay > areax:
    saida = "A área do triângulo Y é maior que a área do triângulo X"
else:
    saida = "As áreas dos triângulos são iguais"

# Saída de dados
print(f"A área do triângulo X = {areax:.1f}")
print(f"A área do triângulo Y = {areay:.1f}")
print(saida)
