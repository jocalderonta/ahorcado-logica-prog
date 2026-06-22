#Es importante importar el modulo random para poder seleccionar una palabra aleatoria de la lista de palabras.
import random

#Posibles palabras para el juego del ahorcado
palabras = ["python", "programacion", "teclado", "universidad","monitor","linux"]

#Elección aleatoria de una palabra de la lista
palabra_secreta = random.choice(palabras)

intentos_restantes = 6
letras_adivinadas = []
progreso = []

#Con el condicional for rrecorremos la palabra secreta letra por letra y agrergamos y gión bajo, lo cual simula la cantidad de letras que tiene la palabra secreta y el progreso del jugador.
for letra in palabra_secreta:
    progreso.append("_")

print ("=" * 40)  
print("¡BIENVENIDO AL JUEGO DEL AHORCADO!") 
print ("=" * 40)  
print(f"Reglas:\n1. Debes adivinar la palabra secreta letra por letra.\n2. Tienes {intentos_restantes} intentos antes de perder.\n3. Si la letra ya fue usada, no se descuenta intento.\n4. ¡Buena suerte!")

#El juego continúa mientras tengamos los suficientes intentos y no hayamos completado la palabra
while intentos_restantes > 0 and "_" in progreso:
    print("\nPalabra: ", " ".join(progreso)) #Se muestra la palabra con sus letras reveladas.Con join convertimos la lista en un solo texto y con espacio entre ellos
    print("Letras usadas:",letras_adivinadas) #Se muestra la lista sde la letras que ya se usó
    letra = input("Ingresa una letra: ").lower() #Se pide al usuario que ingrese una letra y se convierte a minúscula

    #Se verifica que si la letra ingresada ya fue intentada anteriormente.
    if letra in letras_adivinadas:
        print("Ya intentaste esa letra. Prueba con otra.")
        
    else:
        # Si es nueva se agregará a la lista de letras usadas.
        letras_adivinadas.append(letra)

        # Se hace la verificación de si la letra ingresada está dentro de la palabra secreta.
        if letra in palabra_secreta:
            #Se recorre la palabra pa ver las posiciones en donde aparece esa letra.
            for i in range(len(palabra_secreta)):# recorremos cada posición de la palabra (0,1,2,3,4,5)
                if palabra_secreta[i] == letra:# si la letra en esa posición coincide con lo que el jugador escribió
                    progreso[i] = letra # actualizamos esa misma posición en la lista "progreso"
        else:
            #Si la letra no está en la palabra secreta, se resta un intento.
            intentos_restantes -= 1
            print("Letra incorrecta. Intentos restantes:", intentos_restantes)

#Al final se realiza la verificación de si se ha completado la palabra secreta.
if "_" not in progreso:
    print("\n¡Felicidades! Ganaste:")
    print("La palabra secreta era:", palabra_secreta)
else:
    print("\n¡Perdiste! Se acabaron los intentos :)")
    print("La palabra secreta era:", palabra_secreta)



    

