#Escreva uma função que receba uma lista de números e retorne a média aritmética

def media_arit(lista):
    if len(lista)==0:
      return 0
    
    return sum(lista) / len(lista)
    
#Testando a função
numeros=[30,40,12,5,8,19]
resultado= media_arit(numeros)
print(f"A média aritmética '{resultado}'")