#Escreva uma função que verifique se o número é par ou ímpar

def par_impar(x):
    if x % 2==0:
     return "Par."
    else:
     return "Ímpar."

x=6
resultado = par_impar(x)
print(f"O número {x} é {resultado}.")