#Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.
a=10/100
b=15/100
print("Detarminar tu salario  a pagar")
dias=int(input("Ingresa tus días tabajados: "))
salario=int(input("Ahora ingresa tu salario diario: "))
s=(dias*salario/a/b)
print("Tu salario se determino en: ", s)

