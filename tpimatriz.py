def inicializar():
    matriz = []
    acu = 0
    funciones = int(input("ingrese la cantidad de funciones"))
    servidores = int(input("ingrese la cantidad de servidores"))
    for i in range(funciones):
        matriz.append([0]*servidores)
    cargamat(matriz,servidores,funciones)
    recorrermat(matriz,funciones,servidores,acu)
def cargamat(matriz,servidores,funciones):
    for i in range(funciones):
        for j in range(servidores):
            matriz[i][j] = int(input("ingrese el elemento %d,%d :"%(i,j)))
def recorrermat(matriz,funciones,servidores,acu): 
    valor = 0
    for i in range(funciones):
        acu = 0 
        for j in range(servidores):
            if matriz[i][j] >=0:
                acu = matriz[i][j] + acu
    valor
    print(acu)
inicializar()