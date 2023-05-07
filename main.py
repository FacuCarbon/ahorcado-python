import random

def main(): 
    # pido la cantidad de jugadores y sus nombres
    def pedir_cantidad_jugadores():
        cantidad_jugadores = input("¿Cuantos jugadores son? ")
        if cantidad_jugadores == "1":
            jugador = input("Por favor, ingrese su nombre: ")
            return [jugador]
        elif cantidad_jugadores == "2":
            jugador1 = input("Por favor, ingrese el nombre de el jugador 1: ")
            jugador2 = input("Ahora por favor ingrese el nombre de el jugador 2: ")
            return [jugador1, jugador2]

    # le muestro los niveles disponibles y le pido el nivel
    def pedir_nivel():
        while True:
            print("\nMuy bien, ahora eleccione el nivel de dificultad: ")
            print("1 - Facil")
            print("2 - Intermedio")
            print("3 - Dificil")
            nivel_elegido = input("¿Ya se decidió?, ingrese el nivel elegido: ")
            if nivel_elegido in ["1", "2", "3"]:
                return nivel_elegido
            else:
                print("\nTu selección no coincide con los niveles disponibles, te los vuelvo a repetir nuevamente: ")

    # dependiendo de el nivel elegido, cargamos las palabras asignadas al nivel con sus intentos
    def cargar_palabras(nivel_elegido):
        if nivel_elegido == "1":
            with open("palabras/palabrasFaciles.txt", "r") as archivo:
                palabras = [linea.strip() for linea in archivo]
            intentos = 3
        elif nivel_elegido == "2":
            with open("palabras/palabrasIntermedias.txt", "r") as archivo:
                palabras = [linea.strip() for linea in archivo]
            intentos = 5
        else:
            with open("palabras/palabrasDificiles.txt", "r") as archivo:
                palabras = [linea.strip() for linea in archivo]
            intentos = 7
        return palabras, intentos

    jugadores = pedir_cantidad_jugadores()
    nivel_elegido = pedir_nivel()
    palabras, intentos = cargar_palabras(nivel_elegido)

    jugador_actual = jugadores[0]
    while True:
        palabra_a_adivinar = random.choice(palabras)
        print(f"\n{jugador_actual}, es tu turno de adivinar la palabra.")
        adivinar_palabra(jugador_actual, palabra_a_adivinar, intentos)
        if len(jugadores) > 1:
            jugador_actual = jugadores[1] if jugador_actual == jugadores[0] else jugadores[0]
            continuar = input("Presione Enter para continuar o 'q' para salir del juego: ")
            if continuar.lower() == "q":
                break
        else:
            continuar = input("Presione Enter para continuar o 'q' para salir del juego: ")
            if continuar.lower() == "q":
                break
def adivinar_palabra(jugador_actual, palabra_a_adivinar, intentos):
    letras_adivinadas = []
    turno = 1
    letra_revelada = random.randint(0, len(palabra_a_adivinar) - 1)
    palabra_oculta = ["_" if i != letra_revelada else palabra_a_adivinar[i] for i in range(len(palabra_a_adivinar))]
    print("\nLa palabra a adivinar es: ", " ".join(palabra_oculta), "\n")
    while intentos > 0:
        print("Turno " + str(turno))
        letra = input(f"{jugador_actual}, es su turno, ingrese una letra: ")
        if letra in letras_adivinadas:
            print(f"La letra {letra} ya fue adivinada, intente con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_a_adivinar:
            print(f"Felicidades, la letra {letra} forma parte de la palabra.")
            palabra_oculta = [letra if letra == palabra_a_adivinar[i] else palabra_oculta[i] for i in range(len(palabra_a_adivinar))]
            print(" ".join(palabra_oculta))
            if "_" not in palabra_oculta:
                print(f"{jugador_actual} ha ganado el juego!")
                return
        else:
            print(f"Lo siento, la letra {letra} no es parte de la palabra.")
            intentos -= 1
        turno += 1
    print(f"El juego ha terminado. La palabra correcta era: {palabra_a_adivinar}")





if __name__ == "__main__":
    main()