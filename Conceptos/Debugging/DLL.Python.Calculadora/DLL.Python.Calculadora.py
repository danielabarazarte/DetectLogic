print("Calculadora #DetectaLaL�gica")

num1 = float(input("Ingrese el primer n�mero: "))
num2 = float(input("Ingrese el segundo n�mero: "))

print("Operaciones:")
print("1. Suma")
print("2. Resta")  
print("3. Multiplicaci�n")
print("4. Divisi�n")

operacion = input("Seleccione la operaci�n (1/2/3/4): ")

if operacion == '1':
    print(num1, "+", num2, "=", num1 + num2)

elif operacion == '2':
    print(num1, "-", num2, "=", num1 - num2)

elif operacion == '3':
    print(num1, "*", num2, "=", num1 * num2)

elif operacion == '4':
    print(num1, "/", num2, "=", num1 / num2)

else:
    print("Operaci�n inv�lida")