#Es importante importar el modulo random para poder seleccionar una palabra aleatoria de la lista de palabras.
import random

#Posibles palabras para el juego del ahorcado
palabras = ["python", "programacion", "teclado", "universidad","monitor"]

#Elección aleatoria de una palabra de la lista
palabra_secreta = random.choice(palabras)

intentos_restantes = 6
letras_adivinadas = []
progreso = []

for letra in palabra_secreta:
    progreso.append("_")
    
#El juego continúa mientras tengamos los suficientes intentos y no hayamos completado la palabra
while intentos_restantes > 0 and "_" in progreso:
    print("\nPalabra: ", " ".join(progreso)) #Con join convertimos la lista en un solo texto y con espacio entre ellos
    print("Letras usadas:",letras_adivinadas) #Se muestra la lista sde la letras que ya se usó
    letra = input("Ingresa una letra: ").lower() #Se pide al usuario que ingrese una letra y se convierte a minúscula
    