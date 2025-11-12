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
tupla = ("Senai", True, 56, 74.6)
print(tupla)
print(type(tupla))

