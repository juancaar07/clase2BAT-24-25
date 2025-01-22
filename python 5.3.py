n = int(input("dime un año"))

if (n % 100) == 0 and (n % 400) !=0 or (n % 4) !=0:
    print(n, "El año no es bisiesto")
else:
    print("Es un año bisiesto")
