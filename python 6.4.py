#6.4 Pide al usuario su nombre y un número. Después de esto, muestra por
#pantalla, su nombre el número de veces que haya elegido. Comprueba y evita
#que se produzcan errores.
#Realiza un programa que lea dos números por teclado y permita elegir entre 4
# opciones en un menú
#1 - Mostrar la suma de los dos números
#2 - Mostrar la resta de los dos números (el primero menos el segundo)
#3 - Mostrar la multiplicación de los dos números
#4 - Salir del programa
#En caso de introducir una opción inválida, el programa volverá a solicitar otra
#opción hasta que el usuario elija salir

nombre = input("Dime un nombre ")
n = int(input("Dime un número "))

while n > 0:
    print(nombre)
    n = (n  - 1)
print("Fin del programa")