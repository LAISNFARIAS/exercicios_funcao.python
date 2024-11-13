#Faça uma função que verifique se uma palavra é palíndromo

def palindromo(palavra):
    palavra = palavra.lower()
    return palavra ==palavra[::-1]

#Testando a função

palavra = "ROMA"
if palindromo(palavra):
  print(f"A palavra '{palavra}' é um palíndromo.")
else:
     print(f"A palavra '{palavra}' não é um palíndromo.")