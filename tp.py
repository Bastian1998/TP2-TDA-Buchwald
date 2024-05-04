def calcular_poder(listaSoldados,listaPoderes):
    subproblemas = [(0,"")]
    resultadoOptimo=[0]
    cadenaOperaciones = ""
    for i in range(len(listaSoldados)):
        for j in range(i+1):
            optimoAnterior = subproblemas[i-j][0]
            minimoActual = [listaSoldados[i], listaPoderes[j]]
            calculoMinimo = int(min(minimoActual))+optimoAnterior
            if(resultadoOptimo[0] < calculoMinimo):
                resultadoOptimo[0] = calculoMinimo
                cadenaOperaciones = str(subproblemas[i-j][1])+"C"*j+"A"
        subproblemas.append((resultadoOptimo[0],cadenaOperaciones))
    print(subproblemas)
    return resultadoOptimo[-1]

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

#lista1 = [271,531,916,656,664]
#lista2 = [21,671,749,833,1543]
lista1,lista2 = carga_datos("10.txt")
print("lista de soldados:")
print(lista1)
print("lista de ataques:")
print(lista2)
print("Los subproblemas y respuesta óptima son:")
print(calcular_poder(lista1,lista2))