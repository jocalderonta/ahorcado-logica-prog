#Importar el modulo random para poder seleccionar una palabra aleatoria.
import random

#Usamos tupla porque no cambia la lista de palabras durante el juego
palabras = ("python", "programacion", "teclado", "universidad", "monitor", "linux")

palabra_secreta = random.choice(palabras)

intentos_restantes = 6
letras_adivinadas = []
progreso = []

#Una posición oculta ("_") por cada letra de la palabra
for letra in palabra_secreta:
    progreso.append("_")

print("=" * 40)
print("¡BIENVENIDO AL JUEGO DEL AHORCADO!")
print("=" * 40)
print(f"Reglas:\n1. Debes adivinar la palabra secreta letra por letra.\n2. Tienes {intentos_restantes} intentos antes de perder.\n3. Si la letra ya fue usada, no se descuenta intento.\n4. ¡Buena suerte!")

#El juego continúa mientras tengamos los suficientes intentos y no hayamos completado la palabra
while intentos_restantes > 0 and "_" in progreso:
    print(f"\nPalabra: {' '.join(progreso)}")
    print(f"Letras usadas: {letras_adivinadas}")
    letra = input("Ingresa una letra: ").lower()

    #Solo se acepta una letra del alfabeto
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada no válida. Debes ingresar una sola letra (a-z).")
        continue

    if letra in letras_adivinadas:
        print("Ya intentaste esa letra. Prueba con otra.")

    else:
        letras_adivinadas.append(letra)
        
#Verificación de si la letra ingresada está dentro de la palabra secreta.
        if letra in palabra_secreta:
            #Revela la letra en cada posición donde aparece
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    progreso[i] = letra
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Intentos restantes: {intentos_restantes}")

if "_" not in progreso:
    print("\n¡Felicidades! Ganaste:")
    print(f"La palabra secreta era: {palabra_secreta}")
else:
    print("\n¡Perdiste! Se acabaron los intentos :)")
    print(f"La palabra secreta era: {palabra_secreta}")



    

