import timeit
import matplotlib.pyplot as plt

resultadosEsperados = {
    "5.txt": "1413",
    "10.txt": "2118",
    "10_bis.txt": "1237",
    "20.txt": "11603",
    "50.txt": "3994",
    "100.txt": "7492",
    "200.txt": "4230",
    "500.txt": "15842",
    "1000.txt": "4508",
    "2000.txt": "3999", # Custom
    "3000.txt": "3000", # Custom
    "4000.txt": "4000", # Custom
    "5000.txt": "504220",
    "6000.txt": "6000", # Custom
}

def calcular_poder(listaSoldados,listaPoderes):
    subproblemas = [(0,"")]
    resultadoOptimo=0
    cadenaOperaciones = ""
    for i in range(len(listaSoldados)):
        for j in range(i+1):
            optimoAnterior = subproblemas[i-j][0]
            minimoActual = [listaSoldados[i], listaPoderes[j]]
            calculoMinimo = int(min(minimoActual))+optimoAnterior
            if(resultadoOptimo < calculoMinimo):
                resultadoOptimo = calculoMinimo
                cadenaOperaciones = str(subproblemas[i-j][1])+"C"*j+"A"
        subproblemas.append((resultadoOptimo,cadenaOperaciones))
    #print(subproblemas)
    return subproblemas[-1]

def carga_datos(ruta):
    archivo = open(ruta,'r')
    listaSoldados = []
    listaPoderes = []
    obtenerCantidad = True
    cantidadSoldados = 0
    lineas = archivo.readlines()
    for linea in lineas:
        linea = linea.replace('\n','')
        linea=linea.split()
        if(linea[0] == "#"):
            continue
        if(obtenerCantidad):
            obtenerCantidad = False
            cantidadSoldados = int(linea[0])
            print(cantidadSoldados)
        else:
            if(cantidadSoldados > 0):
                listaSoldados.append(int(linea[0]))
                cantidadSoldados = cantidadSoldados - 1
            else:
                listaPoderes.append(int(linea[0]))
    archivo.close()
    return listaSoldados,listaPoderes

def calcular_tiempos(archivos):
    tiempos = []
    for elemento in archivos:
        listaSoldados, listaPoderes = carga_datos(elemento + ".txt")
        tiempo = timeit.timeit(lambda: calcular_poder(listaSoldados, listaPoderes), number=1)
        tiempos.append((elemento,tiempo))
    return tiempos


    
def graficar(tiempos):
    elemento_x = []
    elemento_y = []
    fig, ax = plt.subplots()
    # Dibujar puntos
    for elemento in tiempos:
        elemento_x.append(elemento[0])
        elemento_y.append(elemento[1])    
    ax.scatter(x = elemento_x, y = elemento_y)
    plt.ylabel('Tiempo de ejecución')
    plt.xlabel('Input de datos(oleadas de soldados)')
    plt.title('Gráfico oleadas de soldados vs tiempo')
    # Guardar el gráfico en formato png
    plt.savefig('diagrama-dispersion.png')
    # Mostrar el gráfico
    plt.show()

def main(archivo):
    lista1,lista2 = carga_datos(archivo + ".txt")
    print("Lista de soldados:")
    print(lista1)
    print("Lista de ataques:")
    print(lista2)
    poder = calcular_poder(lista1,lista2)
    if archivo in resultadosEsperados:
        if resultadosEsperados[archivo] == str(poder[0]):
            print("El resultado es el óptimo")
        else:
            print("El resultado no es óptimo")
    else:
        print("No se encontró el archivo en la lista otorgada por la cátedra.")
        print("El resultado del algoritmo para este conjunto de batallas es : ")
        print(poder)


if __name__ == "__main__":
    keys_without_extension = [key.replace('.txt', '') for key in resultadosEsperados.keys()]
    import sys
    if len(sys.argv) < 2:
        print("Batallas disponibles por la cátedra:") 
        print("5, 10, 10_bis, 20, 50, 100, 200, 500, 1000, 5000")
        print("Ejemplo: python tp.py graficar")
        sys.exit(1)
    elif(sys.argv[1] == "graficar"):
        archivos = keys_without_extension
        tiempos = calcular_tiempos(archivos)
        graficar(tiempos)
    elif (sys.argv[1] in keys_without_extension):
        main(sys.argv[1])
    else:
        print("Batallas disponibles por la cátedra:") 
        print("5, 10, 10_bis, 20, 50, 100, 200, 500, 1000, 5000")
        print("Ejemplo: python tp.py 100")
        print("Ejemplo: python tp.py graficar")
        sys.exit(1)