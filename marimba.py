import random
import matplotlib.pyplot as plt

COSTO_OBJETIVO = [500000, 200000, 150000]
COSTO_TOTAL = [600000, 300000, 280000]  #!DATOS SACADOS DE MERCADO LIBRE
TIPOS_MADERA = ['PINO', 'HORMIGUILLO']
INCRUSTACION = ["A", "B", "C"]
TAMANIOS = ["PROFESIONAL", "GRANDE", "MEDIANA"]
BARNIZADO = ["NORMAL", "TINTA"]
TAMANO_POBLACION = 50
PROBABILIDAD_MUTACION = 0.1
GENERACIONES = 20

peores_individuos = []
promedios_individuoss = []
mejores_individuos = []
peores_grafico = []
promedios_grafico = []
mejores_grafico = []

tamañoPoblacion = 0
maximoPoblacion = 0
minimo = 0
maximo = 0
generaciones = 0
allFitness = []

listaSeleccion = []
listaCruza = []
listaMutacion = []
listaFitness = []

contador_gens = 0
contadorControl = 0
mejores_gen = []
peores_gen = []
mejoresFit = []
promedio_gen = []


def GenerarPrecio():
    valor = COSTO_TOTAL[0] // 9
    return random.uniform(100, valor)  # Rango de precios para la madera


def CrearMarimba(tamaño_poblacion):
    global contadorControl
    global listaSeleccion
    global listaCruza
    global listaMutacion
    global listaFitness
    for i in range(tamaño_poblacion):
        tablaSeleccion = {
            'Indice': i + 1,
            'Faldones': random.choice(TIPOS_MADERA),
            'FaldonesPrecio': 0,
            'Bastidores': random.choice(TIPOS_MADERA),
            'BastidoresPrecio': 0,
            'Cajones': random.choice(TIPOS_MADERA),
            'CajonesPrecio': 0,
            'Patas': random.choice(TIPOS_MADERA),
            'PatasPrecios': 0,
            'Tirantes': random.choice(TIPOS_MADERA),
            'TirantesPrecios': 0,
            'Teclas': random.choice(TIPOS_MADERA),
            'TeclasPrecios': 0,
            'Incrustaciones': random.choice(INCRUSTACION),
            'IncrustacionesPrecios': 0,
            'Tamanio': TAMANIOS[0],
            'TamanioPrecios': COSTO_TOTAL[0],
            'Barnizado': random.choice(BARNIZADO),
            'BarnizadoPrecio': 0,
            'Fitness': 0
        },
        tablaCruza = {
            'Indice': '',
            'Faldones': '',
            'FaldonesPrecio': 0,
            'Bastidores': '',
            'BastidoresPrecio': 0,
            'Cajones': '',
            'CajonesPrecio': 0,
            'Patas': '',
            'PatasPrecios': 0,
            'Tirantes': '',
            'TirantesPrecios': 0,
            'Teclas': '',
            'TeclasPrecios': 0,
            'Incrustaciones': '',
            'IncrustacionesPrecios': 0,
            'Tamanio': '',
            'TamanioPrecios': '',
            'Barnizado': '',
            'BarnizadoPrecio': 0,
            'Fitness': 0
        },
        tablaMutacion = {
            'Faldones': '',
            'FaldonesPrecio': '',
            'Bastidores': '',
            'BastidoresPrecio': '',
            'Cajones': '',
            'CajonesPrecio': '',
            'Patas': '',
            'PatasPrecios': '',
            'Tirantes': '',
            'TirantesPrecios': '',
            'Teclas': '',
            'TeclasPrecios': '',
            'Incrustaciones': '',
            'IncrustacionesPrecios': '',
            'Tamanio': '',
            'TamanioPrecios': '',
            'Barnizado': '',
            'BarnizadoPrecio': '',
            'Fitness': 0
        },
        tablaFitness = {
            'Padre': 0,
            'Fitness padre': 0,
            'Hijo': 0,
            'Fitness hijo': 0,
            'Mejor fitness': 0,
            'Cadena de bits': 0
        },
        listaSeleccion.extend(tablaSeleccion)
        listaCruza.extend(tablaCruza)
        listaMutacion.extend(tablaMutacion)
        listaFitness.extend(tablaFitness)
        contadorControl += 1


def seleccion():
    global listaSeleccion, listaCruza
    sumaFitness = 0
    promedioFitness = 0
    peorFitness = 0
    probAcumulada = 0
    for i in range(len(listaSeleccion)):
        precio = GenerarPrecio()
        listaSeleccion[i].update({'FaldonesPrecio': precio})
        sumaFitness += precio
        precio = GenerarPrecio()
        listaSeleccion[i].update({'BastidoresPrecio': precio})
        sumaFitness += precio
        precio = GenerarPrecio()
        listaSeleccion[i].update({'CajonesPrecio': precio})
        sumaFitness += precio
        precio = GenerarPrecio()
        listaSeleccion[i].update({'PatasPrecios': precio})
        sumaFitness += precio
        precio = GenerarPrecio()
        listaSeleccion[i].update({'TirantesPrecios': precio})
        sumaFitness += precio
        precio = GenerarPrecio()
        listaSeleccion[i].update({'TeclasPrecios': precio})
        sumaFitness += precio
        precio = GenerarPrecio()
        listaSeleccion[i].update({'IncrustacionesPrecios': precio})
        sumaFitness += precio
        precio = GenerarPrecio()
        listaSeleccion[i].update({'BarnizadoPrecio': precio})
        sumaFitness += precio

    for i in range(len(listaSeleccion)):
        precio_total = (listaSeleccion[i]['FaldonesPrecio'] +
                        listaSeleccion[i]['BastidoresPrecio'] +
                        listaSeleccion[i]['CajonesPrecio'] +
                        listaSeleccion[i]['PatasPrecios'] +
                        listaSeleccion[i]['TirantesPrecios'] +
                        listaSeleccion[i]['TeclasPrecios'] +
                        listaSeleccion[i]['IncrustacionesPrecios'] +
                        listaSeleccion[i]['BarnizadoPrecio'])
        listaSeleccion[i]['Fitness'] = precio_total
        sumaFitness += precio_total
    promedioFitness = sumaFitness / len(listaSeleccion)
    for i in range(len(listaSeleccion)):
        if (i == 0):
            peor_fitness = listaSeleccion[0].get("Fitness")
            minimo_fitness = listaSeleccion[0].get('Fitness')
        else:
            if (listaSeleccion[i].get('Fitness') > peor_fitness):
                peor_fitness = listaSeleccion[i].get('Fitness')
                minimo_fitness = listaSeleccion[i].get('Fitness')
            if (minimo_fitness > listaSeleccion[i].get('Fitness')):
                minimo_fitness = listaSeleccion[i].get('Fitness')
        prob = listaSeleccion[i].get('Fitness') / sumaFitness
        expCount = listaSeleccion[i].get('Fitness') / promedioFitness
    mejores = {
        'Generacion': contador_gens,
        'Mejor': peor_fitness,
        'Peor': minimo_fitness,
        'Promedio': promedioFitness
    },
    mejoresFit.extend(mejores)
    equis = 0
    for i in range(len(listaSeleccion)):
        listaFitness[equis].update(
            {'Fitness padre': listaSeleccion[i].get('Fitness')})
        equis += 1


def Cruza():
    for y in range(0, len(listaCruza), 2):
        padre1 = listaCruza[y]
        padre2 = listaCruza[y + 1]
        listaCruza[y].update({"Faldones": padre2.get("Faldones")})
        listaCruza[y + 1].update({"Faldones": padre1.get("Faldones")})
        listaCruza[y].update({"Bastidores": padre2.get("Bastidores")})
        listaCruza[y + 1].update({"Bastidores": padre1.get("Bastidores")})
        listaCruza[y].update({"Cajones": padre2.get("Cajones")})
        listaCruza[y + 1].update({"Cajones": padre1.get("Cajones")})
        listaCruza[y].update({"Patas": padre2.get("Patas")})
        listaCruza[y + 1].update({"Patas": padre1.get("Patas")})
        listaCruza[y].update({"Tirantes": padre2.get("Tirantes")})
        listaCruza[y + 1].update({"Tirantes": padre1.get("Tirantes")})
        listaCruza[y].update({"Teclas": padre2.get("Teclas")})
        listaCruza[y + 1].update({"Teclas": padre1.get("Teclas")})
        listaCruza[y].update({"Incrustaciones": padre2.get("Incrustaciones")})
        listaCruza[y + 1].update(
            {"Incrustaciones": padre1.get("Incrustaciones")})
        listaCruza[y].update({"Barnizado": padre2.get("Barnizado")})
        listaCruza[y + 1].update({"Barnizado": padre1.get("Barnizado")})
    for i in range(len(listaCruza)):
        precio = GenerarPrecio()
        listaCruza[i].update({'FaldonesPrecio': precio})
        precio = GenerarPrecio()
        listaCruza[i].update({'BastidoresPrecio': precio})
        precio = GenerarPrecio()
        listaCruza[i].update({'CajonesPrecio': precio})
        precio = GenerarPrecio()
        listaCruza[i].update({'PatasPrecios': precio})
        precio = GenerarPrecio()
        listaCruza[i].update({'TirantesPrecios': precio})
        precio = GenerarPrecio()
        listaCruza[i].update({'TeclasPrecios': precio})
        precio = GenerarPrecio()
        listaCruza[i].update({'IncrustacionesPrecios': precio})
        precio = GenerarPrecio()
        listaCruza[i].update({'BarnizadoPrecio': precio})


def Mutacion(generacion):
    auxMutados = []
    for x in range(0, len(listaMutacion), 2):
        mut = bool(random.getrandbits(1))
        if mut:
            listaMutacion[x].update({
                'Faldones': random.choice(TIPOS_MADERA),
            })

            listaMutacion[x].update({
                'Bastidores': random.choice(TIPOS_MADERA),
            })
            listaMutacion[x].update({
                'Cajones': random.choice(TIPOS_MADERA),
            })

            listaMutacion[x].update({
                'Tirantes': random.choice(TIPOS_MADERA),
            })
            listaMutacion[x].update({
                'Teclas': random.choice(TIPOS_MADERA),
            })
            listaMutacion[x].update({
                'Incrustaciones':
                random.choice(INCRUSTACION),
            })
            listaMutacion[x].update({
                'Barnizado': random.choice(BARNIZADO),
            })
    for i in range(len(listaMutacion)):
        precio = GenerarPrecio()
        listaMutacion[i].update({'FaldonesPrecio': precio})
        precio = GenerarPrecio()
        listaMutacion[i].update({'BastidoresPrecio': precio})
        precio = GenerarPrecio()
        listaMutacion[i].update({'CajonesPrecio': precio})
        precio = GenerarPrecio()
        listaMutacion[i].update({'PatasPrecios': precio})
        precio = GenerarPrecio()
        listaMutacion[i].update({'TirantesPrecios': precio})
        precio = GenerarPrecio()
        listaMutacion[i].update({'TeclasPrecios': precio})
        precio = GenerarPrecio()
        listaMutacion[i].update({'IncrustacionesPrecios': precio})
        precio = GenerarPrecio()
        listaMutacion[i].update({'BarnizadoPrecio': precio})
    auxMutados = listaMutacion
    auxMutados = sorted(auxMutados, key=lambda x: x['Fitness'], reverse=True)
    ActualizarDatos(auxMutados, generacion)


def ActualizarDatos(mutados, generacion):
    global contadorControl
    for x in range(2):
        if contadorControl < maximoPoblacion:
            contadorControl += 1
            tablaSeleccion = {
                "Indice": contadorControl - 1,
                'Faldones': mutados[x].get("Faldones"),
                'FaldonesPrecio': 0,
                'Bastidores': mutados[x].get("Bastidores"),
                'BastidoresPrecio': 0,
                'Cajones': mutados[x].get("Cajones"),
                'CajonesPrecio': 0,
                'Patas': mutados[x].get("Patas"),
                'PatasPrecios': 0,
                'Tirantes': mutados[x].get("Tirantes"),
                'TirantesPrecios': 0,
                'Teclas': mutados[x].get("Teclas"),
                'TeclasPrecios': 0,
                'Incrustaciones': mutados[x].get("Incrustaciones"),
                'IncrustacionesPrecios': 0,
                'Tamanio': TAMANIOS[0],
                'TamanioPrecios': COSTO_TOTAL[0],
                'Barnizado': mutados[x].get("Barnizado"),
                'BarnizadoPrecio': 0,
                'Fitness': 0
            },
            tablaCruza = {
                'Faldones': mutados[x].get("Faldones"),
                'FaldonesPrecio': 0,
                'Bastidores': mutados[x].get("Bastidores"),
                'BastidoresPrecio': 0,
                'Cajones': mutados[x].get("Cajones"),
                'CajonesPrecio': 0,
                'Patas': mutados[x].get("Patas"),
                'PatasPrecios': 0,
                'Tirantes': mutados[x].get("FaldTirantesones"),
                'TirantesPrecios': 0,
                'Teclas': mutados[x].get("Teclas"),
                'TeclasPrecios': 0,
                'Incrustaciones': mutados[x].get("Incrustaciones"),
                'IncrustacionesPrecios': 0,
                'Tamanio': TAMANIOS[0],
                'TamanioPrecios': COSTO_TOTAL[0],
                'Barnizado': mutados[x].get("Barnizado"),
                'BarnizadoPrecio': 0,
                'Fitness': 0
            },
            tablaMutacion = {
                'Faldones': '',
                'FaldonesPrecio': '',
                'Bastidores': '',
                'BastidoresPrecio': '',
                'Cajones': '',
                'CajonesPrecio': '',
                'Patas': '',
                'PatasPrecios': '',
                'Tirantes': '',
                'TirantesPrecios': '',
                'Teclas': '',
                'TeclasPrecios': '',
                'Incrustaciones': '',
                'IncrustacionesPrecios': '',
                'Tamanio': '',
                'TamanioPrecios': '',
                'Barnizado': '',
                'BarnizadoPrecio': '',
                'Fitness': 0
            },
            tablaFitness = {
                'Padre': 0,
                'Fitness padre': 0,
                'Hijo': 0,
                'Fitness hijo': 0,
                'Mejor fitness': 0
            }
            listaSeleccion.extend(tablaSeleccion)
            listaCruza.extend(tablaCruza)
            listaMutacion.extend(tablaMutacion)
            listaFitness.append(tablaFitness)
        else:
            ControlPoblacion(contadorControl)


def ControlPoblacion(contadorControl):
    for x in range(contadorControl):
        if (listaFitness[x].get('Fitness hijo')
                > listaFitness[x].get('Fitness padre')):
            listaSeleccion[x].update(
                {'Poblacion Inicial': listaFitness[x].get('Hijo')})
        else:
            listaSeleccion[x].update(
                {'Poblacion Inicial': listaFitness[x].get('Padre')})
        listaSeleccion[x].update({
            'Valor de x': 0,
            'Fitness': 0,
            'Prob i': 0,
            'Prob acumulada': 0,
            'Conteo esperado': 0,
            'Conteo actual': 0
        })


def Empezar(tamañoPoblacion, poblacionMax, generaciones):
    global contador_gens
    global maximoPoblacion
    maximoPoblacion = poblacionMax
    CrearMarimba(tamañoPoblacion)
    for i in range(generaciones):
        seleccion()
        Cruza()
        Mutacion(generaciones)
    Clasificar(generaciones)


def Clasificar(generaciones):
    global mejores_gen, peores_gen, promedio_gen
    for i in range(generaciones):
        mejores_gen.append(mejoresFit[i].get('Mejor'))
        peores_gen.append(mejoresFit[i].get('Peor'))
        promedio_gen.append(mejoresFit[i].get('Promedio'))
    GenerarGrafica(mejores_gen, peores_gen, promedio_gen)


def GenerarGrafica(x, y, z):
    x = sorted(x)
    y = sorted(y,reverse=True)
    z = sorted(z)
    print("MEJOR MARIMBA XD ", peores_gen[len(mejoresFit)-1])
    plt.plot(x, label="Caso promedio")  # Dibuja el gráfico
    plt.xlabel("Generaciones")  # Inserta el título del eje X
    plt.ylabel("Evolucion del Fitness")  # Inserta el título del eje Y
    plt.ioff()  # Desactiva modo interactivo de dibujo
    plt.ion()  # Activa modo interactivo de dibujo
    plt.plot(y, label="Mejor Caso"
             )  # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()  # Desactiva modo interactivo
    plt.ion()  # Activa modo interactivo de dibujo
    plt.plot(z, label="Peor caso"
             )  # Dibuja datos de lista2 sin borrar datos de lista1
    plt.ioff()  # Desactiva modo interactivo
    # plt.plot(lista3)   # No dibuja datos de lista3
    plt.legend()
    plt.show()  # Fuerza dibujo de datos de lista3


Empezar(10, 20, 500)
