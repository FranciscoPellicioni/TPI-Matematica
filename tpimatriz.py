def inicializar():
    matriz = []
    funciones = int(input("Ingrese la cantidad de funciones: "))
    servidores = int(input("Ingrese la cantidad de servidores: "))
    for i in range(funciones):
        matriz.append([0] * servidores)
    print("Matriz inicial:")
    mostramat(matriz)
    cargamat(matriz, servidores, funciones,)
    recorrermat(matriz, funciones, servidores)
def cargamat(matriz, servidores, funciones):
    for i in range(funciones):
        for j in range(servidores):
            matriz[i][j] = int(input("Ingrese el elemento %d,%d: " % (i, j)))
            print("Matriz actualizada:")
            mostramat(matriz)    
def recorrermat(matriz, funciones, servidores):
    print("Matriz final:")
    mostramat(matriz)
    mostratranspuesta(matriz)
    for i in range(funciones):
        acu = 0
        for j in range(servidores):
            acu = acu + matriz[i][j]
        promefun = acu / servidores
        print("Fila", i, "el tiempo promedio es:", promefun)
    for i in range(servidores):
        acu2 = 0
        for j in range(funciones):
            acu2 = acu2 + matriz[j][i]
        promeser = acu2 / funciones
        print("Columna", i, "el tiempo promedio es:", promeser)
def mostramat(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print()
def mostratranspuesta(matriz):
    transpuesta = []
    for j in range(len(matriz)):
        fila = []
        for i in range(len(matriz)):
            fila.append(matriz[i][j])
        transpuesta.append(fila)
    print("Matriz transpuesta:")
    mostramat(transpuesta)
inicializar()