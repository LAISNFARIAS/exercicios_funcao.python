# Faça uma função que converta uma temperatura em Celsius para Fahrenheit


def fahrenheit(celsius):
    fahrenheit= (celsius * 9/5)+32
    return fahrenheit

temperatura_celsius = 24
temperatura_fahrenheit =fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F")