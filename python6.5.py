"""""
Realiza un programa que lea dos números por teclado y permita elegir entre 4
opciones en un menú
1 - Mostrar la suma de los dos números
2 - Mostrar la resta de los dos números (el primero menos el segundo)
3 - Mostrar la multiplicación de los dos números
4 - Salir del programa
En caso de introducir una opción inválida, el programa volverá a solicitar otra
opción hasta que el usuario elija salir.
"""""

n1 = int(input ("Dime un número"))
n2 = int (input ("Dime otro número"))

print("Mostrar la suma de los dos números")
print("Mostrar la resta de los dos números el primero menos el segundo")
print("Mostrar la multiplicación de los dos números")
print("Salir del programa")

a=int(input("Elige una de estas cuatro opciones (1,2,3,4):"))

while a != 1 and a != 2 and a != 3 and a != 4 :    
    a = int(input("Dime uno de los cuatro números."))
print("Perfecto")


if a== 1:
    print("La suma de los dos números es:",n1+n2)
elif a == 2:
    print ("La resta de los dos números es",n1-n2)
elif a == 3:
    print("La multiplicación de los dos números es",n1*n2)
elif a == 4:
    print("Has abandonado el programa")