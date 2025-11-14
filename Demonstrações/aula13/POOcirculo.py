import calculadora as c

# Instanciação
circulo = c.calculadoraCirculo()

# Entrada de dados
raio = float(input("Digite o valor do raio: "))

# Processamento de dados
circunferencia = circulo.circunferencia(raio)
area = circulo.area(raio)

# Saída de dados
print(f'''  Circunferência: {circunferencia:.2f}
            Área: {area:.2f}
            PI: {circulo.PI}
        ''')