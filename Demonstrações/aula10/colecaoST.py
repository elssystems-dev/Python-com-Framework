# -------- Lista em Python --------- #
lista = ["SENAI", True, 22, 3.5]
print(lista)
print(type(lista[2]))
print(lista[2])
print(len(lista))
lista.insert(1, "Campeão")
lista.append("Feriado")
del lista[3]
lista.append("Senai")
for i in range(len(lista)):
    print(lista[i])

# ----- Tupla ----- #
# Indices 0  1  2  3
tupla = ("Senai", True, 56, 74.6)
print(tupla)
print(type(tupla))
print(type(tupla[1]))
print(type(tupla[3]))

# ------ Dicionário ------ #
#chave: Valor
dicionario = {"nome": "Senai", "logica": False, "num1": 2, "num2": 1.5}
print(dicionario)
print(type(dicionario))
print(dicionario["logica"])
for chave in dicionario.keys:
    print(chave, "->", dicionario)
dicionario.update({"novo": "Senai"})
dicionario.update({"nome": "Terca"})
del dicionario["logica"]

# ----- Conjunto ------ #
conjunto = {"Senai", False, 10, 2.69}
print(conjunto)
print(type(conjunto))
print(conjunto[2])
conjunto.add(23)
conjunto.discard("Senai")
conjunto.clear()
