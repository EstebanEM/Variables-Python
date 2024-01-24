#Programa para calcular la distancia recorrida en un movimiento rectilíneo. Recuerde $x=v*t$ donde $v$ es velocidad y $t$ es tiempo. Solicitar al usuario velocidad en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km).
#descripcion de un movimiento en line arecta
#km=1000
print("Binvenido, aquí calcularemos la distancia de un mivimiento ectilineo")
v=int(input("Para eso, necesito que ingreses la velocidad: "))#ingresa la velocidad del objeto

t= int(input("Ahora ingresa los minutos recorridos: "))#ingresa el timepo del objeto
d = (v * (t/60))
print("la disatancia recorrida en un mivimineto rectilinineo es: ", d, "km/h")
