num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
oper = input("Operación (+, -, *, /): ")
if oper == '+':
 result = num1 + num2
elif oper == '-':
 result = num1 - num2
elif oper == '*':
 result = num1 * num2
elif oper == '/':
 result = num1 / num2
else:
 result = "Inválida"
print(f"Resultado: {result}")