import random
import matplotlib.pyplot as plt

COSTO_OBJETIVO = [500000, 200000, 150000]
COSTO_TOTAL = [600000, 300000, 280000]  #!DATOS SACADOS DE MERCADO LIBRE
TIPOS_MADERA = ['PINO', 'HORMIGUILLO']
INCRUSTACION = ["A", "B", "C"]
TAMANIOS = ["PROFESIONAL", "GRANDE", "MEDIANA"]
BARRIZADO = ["NORMAL", "TINTA"]
TAMANO_POBLACION = 50
PROBABILIDAD_MUTACION = 0.1
GENERACIONES = 20

peores_individuos = []
promedios_individuoss = []
mejores_individuos = []
peores_grafico = []
promedios_grafico = []
mejores_grafico = []


def CrearMarimba():
    return {
        'faldones': random.choice(TIPOS_MADERA),
        'bastidores': random.choice(TIPOS_MADERA),
        'cajones': random.choice(TIPOS_MADERA),
        'patas': random.choice(TIPOS_MADERA),
        'tirantes': random.choice(TIPOS_MADERA),
        'teclas': random.choice(TIPOS_MADERA),
        'incrustaciones': random.choice(INCRUSTACION),
        'tamanio': TAMANIOS[0],
        'barnizado': random.choice(BARRIZADO)
    }


def Costos(marimba):
    costo = 0
    for componente, madera in marimba.items():
        if componente == "faldones":
            costo += 5000 if madera == "PINO" else 7000
        elif componente == "bastidores":
            costo += 2000 if madera == "PINO" else 3000
        elif componente == "cajones":
            costo += 10000 if madera == "PINO" else 20000
        elif componente == "patas":
            costo += 1000 if madera == "PINO" else 1500
        elif componente == "tirantes":
            costo += 15000 if madera == "PINO" else 20000
        elif componente == "teclas":
            costo += 15000 if madera == "PINO" else 200000
        elif componente == "incrustaciones":
            costo += 1500 if madera == "PINO" else 1000
        elif componente == "barnizado":
            costo += 10000 if madera == "PINO" else 15000
    return costo


def CalcularCosto(marimbas):
    poblacion_con_costo = []
    for marimba in marimbas:
        marimba_con_costo = marimba.copy()
        marimba_con_costo['costo'] = Costos(marimba)
        poblacion_con_costo.append(marimba_con_costo)
    return poblacion_con_costo


def CalcularFitness(marimbas):
    global promedios_individuoss
    poblacion_fitness = []
    for marimba in marimbas:
        costo_marimba = CalcularCosto([marimba])[0]['costo']
        if costo_marimba is not None:  # Verificar si el costo se calculó correctamente
            fitness = 1 / (1 + abs(costo_marimba - COSTO_TOTAL[0]))
            promedio = fitness / TAMANO_POBLACION
            promedios_individuoss.append(promedio)
            marimba_con_fitness = marimba.copy()
            marimba_con_fitness['fitness'] = fitness
            poblacion_fitness.append(marimba_con_fitness)
    return poblacion_fitness


def Cruzar(padre1, padre2):
    hijo = {}
    for componente in padre1:
        # 50% de probabilidad de heredar del padre 1 y 50% del padre 2
        hijo[componente] = padre1[componente] if random.random(
        ) < 0.5 else padre2[componente]
    return hijo


def Mutacion(individuo):
    componente_a_mutar = random.choice(list(individuo.keys()))
    if componente_a_mutar in [
            'faldones', 'bastidores', 'cajones', 'patas', 'tirantes', 'teclas'
    ]:
        individuo[componente_a_mutar] = random.choice(TIPOS_MADERA)
    elif componente_a_mutar == 'incrustaciones':
        individuo[componente_a_mutar] = random.choice(INCRUSTACION)
    elif componente_a_mutar == 'barnizado':
        individuo[componente_a_mutar] = random.choice(BARRIZADO)
    individuo_con_costo = CalcularCosto([individuo])[0]
    individuo_con_fitness = CalcularFitness([individuo_con_costo])[0]
    return individuo_con_fitness


def SeleccionarMejores(poblacion, n):
    global peores_individuos
    # print(poblacion," esto mando")
    poblacion_ordenada = sorted(
        poblacion,
        key=lambda x: x.get('fitness', float('-inf')
                            ),  # Usar float('-inf') como valor predeterminado
    )

    # print(poblacion_ordenada, "Asd")
    mejores = poblacion_ordenada[:n]
    peores = poblacion_ordenada[-n:]
    # print(peores)
    peores_individuos.extend(poblacion_ordenada[-n:])
    return mejores


def ComprobarCosto(individuo):
    if 'costo' in individuo:
        print("El individuo tiene costo.")
    else:
        print("El individuo no tiene costo.")


# def AlgoritmoGenetico():
#     global mejores_individuos, GENERACIONES
#     poblacion = [CrearMarimba() for _ in range(TAMANO_POBLACION)]
#     poblacion = CalcularFitness(poblacion)

#     nueva_generacion = []
#     for _ in range(GENERACIONES):
#         padre1, padre2 = random.sample(poblacion, 2)
#         hijo = Cruzar(padre1, padre2)
#         if random.random() < PROBABILIDAD_MUTACION:
#             hijo = Mutacion(hijo)
#         nueva_generacion.append(hijo)  #267500
#     poblacion_seleccionada = SeleccionarMejores(nueva_generacion,
#                                                 TAMANO_POBLACION)
#     mejores_individuos.extend(poblacion_seleccionada)
#     Clasificar()


def AlgoritmoGenetico():
    global mejores_individuos, peores_individuos, promedios_individuoss
    poblacion = [CrearMarimba() for _ in range(TAMANO_POBLACION)]
    poblacion = CalcularFitness(poblacion)

    nueva_generacion = []
    for _ in range(GENERACIONES):
        padre1, padre2 = random.sample(poblacion, 2)
        hijo = Cruzar(padre1, padre2)
        if random.random() < PROBABILIDAD_MUTACION:
            hijo = Mutacion(hijo)
        nueva_generacion.append(hijo)
    poblacion_seleccionada = SeleccionarMejores(nueva_generacion,
                                                TAMANO_POBLACION)
    mejores_individuos.extend(poblacion_seleccionada)
    Clasificar()

def Graficar(x, y, z):
    print(x, " eso es mejor")
    plt.plot(x, label="Mejor Caso")  # Dibuja el gráfico
    plt.xlabel("Generaciones")  # Inserta el título del eje X
    plt.ylabel("Evolucion del Fitness")  # Inserta el título del eje Y
    plt.ioff()  # Desactiva modo interactivo de dibujo
    plt.ion()  # Activa modo interactivo de dibujo
    plt.plot(
        y,
        label="Peor Caso")  # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()  # Desactiva modo interactivo
    plt.ion()  # Activa modo interactivo de dibujo
    plt.plot(z, label="Caso promedio"
             )  # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()  # Desactiva modo interactivo
    # plt.plot(lista3)   # No dibuja datos de lista3
    plt.legend()
    plt.show()  # Fuerza dibujo de datos de l


def Clasificar():
    global GENERACIONES, mejores_individuos, peores_individuos, promedios_individuoss
    global peores_grafico, promedios_grafico, mejores_grafico
    ComprobarCosto(mejores_individuos)
    for marimba in mejores_individuos:
        mejores_grafico.append(marimba['fitness'])
    for marimba in peores_individuos:
        peores_grafico.append(marimba['fitness'])
    for promedio in promedios_individuoss:
        promedios_grafico.append(promedio)
    Graficar(mejores_grafico, peores_grafico, promedios_grafico)


AlgoritmoGenetico()
