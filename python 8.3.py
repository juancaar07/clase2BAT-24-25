datos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
n=int(input("Dime un número: "))

if n >= 1 or n <=12:
    print(datos[n-1])
else:
    print("Fuera del rango entre 1 y 12")