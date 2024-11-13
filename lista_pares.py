#Faça uma função que receba uma lista e retorne uma nova lista com os elementos pares
#da lista original


def elementos_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    return pares

#Testando código:

lista=[20,21,22,23,24,25,26,27,28,29,30]
pares = elementos_pares(lista)
print(pares)