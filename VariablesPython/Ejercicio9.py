#Programa que permita a una tienda saber el valor que pagara un cliente por la compra de varios elementos de la misma referencia. Debe tener como entradas el valor unitario, la cantidad de productos comprados y al valor final se debe adicionar el 16% correspondiente al IVA.
print("Valor que pagara un cliente por productos" )
valor=int(input("El producto más comprado en estos días son las chocolatinas, el valor unitario es de $ "))
cantidad=int(input("Generalmente los clintes compran la cantidad de: "))
costo= cantidad*valor/1+16
print(cantidad, "chocolatinas cuestan: ", costo)

