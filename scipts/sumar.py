import sys

if len(sys.argv) == 3:    
    num1= int(sys.argv[1])   # Guardar en lista 1
    num2= int(sys.argv[2])    # Guardar en lista 2
    resultado = num1 + num2
    print (f"La suma de {num1}+{num2} es: {resultado}")
else:
    print("Error - Introduce los argumentos correctamente")
    print("Ejemplo: sumar.py 5 3")

                 