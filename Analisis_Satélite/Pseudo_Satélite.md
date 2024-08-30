
# Analisis

El código inicialmente simulara la desintegración orbital de un satélite debido a la resistencia atmosférica. Inicialmente, debo pedirle al usuario que ingrese la altitud inicial del satélite, el coeficiente de arrastre, y la altitud mínima de seguridad. Utilizando un bucle 'while', el programa simulara cada órbita, calculando la pérdida de altitud en función del coeficiente de arrastre y actualizando la altitud del satélite en consecuencia. Después de cada órbita, el coeficiente de arrastre se incrementara de a poco para reflejar el aumento de resistencia. El bucle se detendrá cuando el satélite alcanze la altitud mínima de seguridad o cuando la pérdida de altitud sea despreciable, indicando que el satélite se habrá estabilizado. Finalmente, el programa le mostrará al usuario las primeras dos órbitas y la altitud final, ya sea en una órbita estabilizada o tras reingresar en la atmósfera, proporcionando una simulación efectiva del proceso de desintegración orbital.

# pseudocodigo

Inicio

//Solicitar datos de entrada al usuario:

   Pedir altitud_inicial (en kilómetros)
   Pedir coeficiente_arrastre (por ejemplo, 0.01)
   Pedir altitud_minima_seguridad (en kilómetros)

//Inicializar variables:
   altitud_actual = altitud_inicial
   numero_orbitas = 0
   altitud_perdida = 0

   Imprimir "Simulación de desintegración orbital:"
   Imprimir altitud_inicial

//Mientras altitud_actual > altitud_minima_seguridad:
   Incrementar numero_orbitas en 1

//Calcular altitud_perdida = coeficiente_arrastre * altitud_actual
  Restar altitud_perdida de altitud_actual
  Incrementar coeficiente_arrastre en 0.0001

Si numero_orbitas <= 2:
  Imprimir "Órbita numero_orbitas: Altitud = altitud_actual, Pérdida de altitud = altitud_perdida"

Si altitud_perdida < 0.01:
   Imprimir "El satélite se estabiliza en la órbita numero_orbitas a una altitud de altitud_actual."

Terminar el programa

Fin del bucle

Imprimir "El satélite ha reingresado en la atmósfera terrestre en la órbita numero_orbitas a una altitud de altitud_actual."

Fin
