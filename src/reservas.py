
import os
import random

def main():
    # Información del usuario
    titulo = input("Ingrese su título (Sr. o Sra.): ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    
    nombre_completo = f"{titulo} {nombre} {apellido}"
    print(f"{nombre_completo}, ¡Bienvenido a Arrows Airlines!")

    # Selección de vuelo
    print("Seleccione un origen y destino entre las siguientes ciudades:")
    print("1. Medellín")
    print("2. Armenia")
    print("3. Santa Marta")
    
    origen = int(input("Seleccione el número de la ciudad de origen (1/2/3): "))
    destino = int(input("Seleccione el número de la ciudad de destino (1/2/3): "))
    
    # Diccionario de distancias entre las ciudades
    distancias = {
        (1, 2): 240,  # Medellín a Armenia
        (1, 3): 461,  # Medellín a Santa Marta
        (2, 3): 657   # Armenia a Santa Marta
    }
    
    # Identificamos el origen y destino
    if origen == 1:
        ciudad_origen = "Medellín"
    elif origen == 2:
        ciudad_origen = "Armenia"
    else:
        ciudad_origen = "Santa Marta"
    
    if destino == 1:
        ciudad_destino = "Medellín"
    elif destino == 2:
        ciudad_destino = "Armenia"
    else:
        ciudad_destino = "Santa Marta"
    
    # Preguntamos el día y fecha del vuelo
    dia_semana = input("Ingrese el día de la semana en el que desea viajar: ").lower()
    dia_mes = int(input("Ingrese el día del mes en que desea viajar (1-30): "))
    
    # Calcular la distancia
    distancia = distancias.get((origen, destino)) if origen < destino else distancias.get((destino, origen))
    
    # Calcular precio según distancia y día
    if distancia < 400:
        if dia_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
            precio = 79900
        else:
            precio = 119900
    else:
        if dia_semana in ['lunes', 'martes', 'miércoles', 'jueves']:
            precio = 156900
        else:
            precio = 213000
            
    # Asignación de asiento
    preferencia_asiento = input("¿Prefiere un asiento en el pasillo, ventana, o no tiene preferencia? ").lower()
    
    if preferencia_asiento == "pasillo":
        asiento = "C"
    elif preferencia_asiento == "ventana":
        asiento = "A"
    else:
        asiento = "B"
        
    numero_asiento = random.randint(1, 29)
    asiento_asignado = f"{numero_asiento}{asiento}"
    import os
    # Salida
    print(f"\n--- Resumen de la Reserva ---")
    print(f"Nombre: {nombre_completo}")
    print(f"Origen: {ciudad_origen}")
    print(f"Destino: {ciudad_destino}")
    print(f"Fecha de vuelo: {dia_semana} {dia_mes}")
    print(f"Precio del boleto: ${precio}")
    print(f"Asiento asignado: {asiento_asignado}")

if __name__ == "__main__":
    main()


