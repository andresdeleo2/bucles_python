# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
operadores = ["+","-","*","/","**","FIN"]
numero_1 = float(input("Ingrese Primer Numero: "))
operador = str(input("Ingrese Operador +,-,/,* ó ** /// Para Salir escriba FIN: "))
while operador not in operadores:
    operador = str(input(" ERROR! Ingrese un operador valido: "))
    if operador == "FIN":
        break
 

while operador != "FIN":
    numero_2 = float(input("Ingrese Segundo Numero: ")) #Pido acá el segundo numero, porque si se ingresa FIN en primera instancia, ya no se pide el 2do numero.
    if operador == "+":
        resultado = numero_1 + numero_2
    elif operador == "-":
        resultado = numero_1 - numero_2
    elif operador == "*":
        resultado = numero_1 * numero_2
    elif operador == "/":
        resultado = numero_1 / numero_2
    elif operador == "**":
        resultado = numero_1 ** numero_2
    print("El resultado es: ", resultado)
    numero_1 = float(input("Ingrese Primer Numero: "))
    operador = str(input("Ingrese Operador +,-,/,* ó ** /// Para Salir escriba FIN: "))
    while operador not in operadores:
        operador = str(input(" ERROR! Ingrese un operador valido: "))
    






