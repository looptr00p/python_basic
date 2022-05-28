arr_palabra = []

def calcular_puntaje(n_intentos, n_maximo_intentos, palabra):
    puntaje = (1 - (n_intentos/n_maximo_intentos)) * len(palabra)
    return puntaje

def adivinar_palabra(n_intentos, palabra):
    global arr_palabra
    intentos = 0
    cant_letras_adivinadas = 0
    while intentos < n_intentos and cant_letras_adivinadas < len(palabra):
        letra = ''
        while len(letra) > 1 or letra.isalpha() == False:
            letra = input("Ingrese letra: ")
        if letra in palabra:
            for x in range(len(palabra)):
                if letra == palabra[x]:
                    arr_palabra[x]  = letra
                    cant_letras_adivinadas += 1
            print(*arr_palabra)
        else:
            intentos += 1
    if intentos >= n_intentos:
        print(f"Usted ya intentó", n_intentos, "veces, la palabra era", palabra)
    puntaje_obtenido = calcular_puntaje(intentos, n_intentos, palabra)
    return puntaje_obtenido


def proponer_palabra(nombre_adivinador):
    global arr_palabra
    arr_palabra = []
    intento = 0
    while intento < 3:
        palabra = input("Palabra a adivinar: ").lower()
        if(len(palabra) >= 20 or palabra.isalpha() == False):
            print("Ingrese palabra sin simbolos ni numeros y maximos 20 caracteres")
            intento += 1
            print(f"Intentos ",intento,"/3")
        else:
            for x in palabra:
                arr_palabra.append('_')
            return palabra
    print("3 palabras mal ingresadas, el ganador es el Adivinador", nombre_adivinador)
    exit()

def control_de_rol(jugador_proponedor, jugador_adivinador, cantidad_intentos):
    proponedor = jugador_proponedor
    adivinador = jugador_adivinador
    print(f'Ahora juega Proponedor:', proponedor)
    palabra = proponer_palabra(adivinador)
    print(f"Ahora juega Adivinador: ", adivinador)
    puntaje_de_adivinar = adivinar_palabra(cantidad_intentos, palabra)
    return puntaje_de_adivinar

def informar_ganador(ganador, perdedor, puntaje_maximo, puntaje_minimo):
    print(f'El Ganador es el jugador', ganador)
    print(f'Puntaje jugador', ganador, ':', puntaje_maximo)
    print(f'Puntaje jugador', perdedor, ':', puntaje_minimo)
    
def control_de_turnos():
    print('Hola bienvenido al juego adivina palabra ')
    jugador_uno = input("Nombre primer jugador: ")
    jugador_dos = input("Nombre segundo jugador: ")
    cantidad_palabras = int(input("Cantidad de palabras: "))
    cantidad_intentos = int(input("Cantidad de Intentos: "))
    ronda = 1
    puntaje_jugador_uno = []
    puntaje_jugador_dos = []
    while ronda <= cantidad_palabras:
        print(f'Ronda:', ronda)
        puntaje = control_de_rol(jugador_uno, jugador_dos, cantidad_intentos)
        puntaje_jugador_dos.append(puntaje)
        puntaje = control_de_rol(jugador_dos, jugador_uno, cantidad_intentos)
        puntaje_jugador_uno.append(puntaje)
        ronda+=1
    sum_jugador_uno = sum(puntaje_jugador_uno)
    sum_jugador_dos = sum(puntaje_jugador_dos)
    if(sum_jugador_dos == sum_jugador_uno):
        print("WOW! Han empatado, vuelvan a jugar ")
        print(f'Puntaje jugador', jugador_uno, ':', sum_jugador_uno)
        print(f'Puntaje jugador', jugador_dos, ':', sum_jugador_dos)
    elif(sum_jugador_dos > sum_jugador_uno):
        informar_ganador(jugador_dos, jugador_uno, sum_jugador_dos, sum_jugador_uno)
    else:
        informar_ganador(jugador_uno, jugador_dos, sum_jugador_uno, sum_jugador_dos)

control_de_turnos()