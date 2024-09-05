
def main():
    # Pedir datos de entrada al usuario
    altitud_inicial = float(input("agrega la altitud inicial del satélite (en kilómetros): "))
    coeficiente_arrastre = float(input("agrega el coeficiente de arrastre inicial (por ejemplo, 0.01): "))
    altitud_minima_seguridad = float(input("agrega la altitud mínima de seguridad (en kilómetros): "))

    # Inicializar variables
    altitud_actual = altitud_inicial
    numero_orbitas = 0
    altitud_perdida = 0

    print("\nSimulación de desintegración orbital:")
    print(f"Altitud inicial: {altitud_inicial} km")

    # Bucle para simular la órbita
    while altitud_actual > altitud_minima_seguridad:
        numero_orbitas += 1
        altitud_perdida = coeficiente_arrastre * altitud_actual
        altitud_actual -= altitud_perdida
        coeficiente_arrastre += 0.0001  # Aumentar ligeramente el coeficiente de arrastre

        # Mostrar las primeras dos órbitas
        if numero_orbitas <= 2:
            print(f"Órbita {numero_orbitas}: Altitud = {altitud_actual:.2f} km, Pérdida de altitud = {altitud_perdida:.2f} km")

        # Verificar si la pérdida de altitud es muy pequeña (estabilización)
        if altitud_perdida < 0.01:
            print(f"\nEl satélite se estabiliza en la órbita {numero_orbitas} a una altitud de {altitud_actual:.2f} km.")
            return

    # Mostrar la altitud y órbita final si se reingresa a la atmósfera
    print(f"\nEl satélite ha reingresado en la atmósfera terrestre en la órbita {numero_orbitas} a una altitud de {altitud_actual:.2f} km.")

# Ejecutar la simulación
if __name__ == "__main__":
    
    main()

