# interpretacion de las imagenes

dentro de las imaagines lo que hice fue resaltar punto por punto las cosas mas importantes, asi creando un bosquejo de como mas o menos tengo que hacer el pseudo codigo. resaltando que tipo de comandos debo hacer para que cada funcion sea posible y bajo que variables o constantes deben funcionar 

# PSEUDO CODIGO

Inicio

    Función principal:

        # Información del usuario
        pedir al usuario que ingrese su título (Sr. o Sra.)
        pedir al usuario que ingrese su nombre
        pedir al usuario que ingrese su apellido
        
        juntar el título, nombre, y apellido para formar el nombre completo
        imprimir mensaje de bienvenida con el nombre completo

        # Selección de vuelo
        Mostrar las ciudades disponibles:
            1. Medellín
            2. Armenia
            3. Santa Marta
            
        pedir al usuario que seleccione el número de la ciudad de origen (1/2/3)
        pedir al usuario que seleccione el número de la ciudad de destino (1/2/3)
        
        # Diccionario de distancias entre las ciudades
        Definir distancias entre ciudades:
            (Medellín a Armenia) = 240 km
            (Medellín a Santa Marta) = 461 km
            (Armenia a Santa Marta) = 657 km
            
        # Identificamos el origen y destino
        Si el origen es 1, ciudad_origen = "Medellín"
        Si el origen es 2, ciudad_origen = "Armenia"
        Si el origen es 3, ciudad_origen = "Santa Marta"
        
        Si el destino es 1, ciudad_destino = "Medellín"
        Si el destino es 2, ciudad_destino = "Armenia"
        Si el destino es 3, ciudad_destino = "Santa Marta"
        
        # Preguntar día y fecha del vuelo
        pedir al usuario que ingrese el día de la semana en que desea viajar
        Convertir el día de la semana a minúsculas
        pedir al usuario que ingrese el día del mes en que desea viajar (1-30)
        
        # Calcular la distancia
        Si origen < destino:
            Obtener la distancia desde el diccionario utilizando la clave (origen, destino)
        De lo contrario:
            Obtener la distancia desde el diccionario utilizando la clave (destino, origen)
        
        # Calcular precio según distancia y día
        Si la distancia es menor a 400 km:
            Si el día de la semana es lunes, martes, miércoles o jueves:
                precio = 79900
            De lo contrario:
                precio = 119900
        De lo contrario:
            Si el día de la semana es lunes, martes, miércoles o jueves:
                precio = 156900
            De lo contrario:
                precio = 213000
                
        # Asignación de asiento
        pedir al usuario que ingrese su preferencia de asiento (pasillo, ventana, o no tiene preferencia)
        Convertir la preferencia de asiento a minúsculas
        
        Si la preferencia de asiento es "pasillo", asiento = "C"
        Si la preferencia de asiento es "ventana", asiento = "A"
        De lo contrario, asiento = "B"
        
        Generar un número de asiento aleatorio entre 1 y 29
        Concatenar el número de asiento y la letra para formar el asiento asignado
        
        # Salida
        Mostrar resumen de la reserva:
            Mostrar nombre completo
            Mostrar ciudad de origen
            Mostrar ciudad de destino
            Mostrar fecha de vuelo
            Mostrar precio del boleto
            Mostrar asiento asignado

    Si este archivo es el archivo principal:
        Llamar a la función principal

Fin
