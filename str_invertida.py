#Crie uma função que receba uma string e retorne a mesma string invertida

def str_invertida(palavra):
    return palavra[::-1]


palavra = "Amora"
palavra_invertida=str_invertida(palavra)
print(f"A palavra '{palavra}' invertida é'{palavra_invertida}'.")