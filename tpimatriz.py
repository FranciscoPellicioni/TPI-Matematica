def menumatriz():
    matriz=[]
    funciones = 0
    servidores = 0 
    resultado= True
    while resultado:
        print("----menu de matrices-----")
        print("1- registrar cantidad de filas(funciones) y columnas de la matriz(servidores)")
        print("2- llena la matriz elemento por elemento")
        print("3- tiempo promedio de ejecucion por funcion")
        print("4- tiempo promedio de ejecucion por servidor")
        print("5- visualizar la matriz transpuesta")
        choice = int(input("Ingrese la opción (1, 2, 3, 4): "))
        if choice==1:
            servidores,funciones=inicializar(matriz,funciones,servidores)
        if choice==2:
            cargamat(matriz,funciones,servidores)
        if choice==3:
            promedioejecucion(matriz,funciones,servidores)
        if choice==4:
            promedioservidor(matriz,funciones,servidores)
        if choice==5:
            mostratranspuesta(matriz)
def inicializar(matriz,funciones,servidores):
    funciones = int(input("Ingrese la cantidad de funciones: "))
    servidores = int(input("Ingrese la cantidad de servidores: "))
    for i in range(funciones):
        matriz.append([0] * servidores)
    print("Matriz inicial:")
    mostramat(matriz)
    return servidores,funciones
def cargamat(matriz, servidores, funciones):
    for i in range(funciones):
        for j in range(servidores):
            matriz[i][j] = int(input("Ingrese el elemento %d,%d: " % (i, j)))
            print("Matriz actualizada:")
            mostramat(matriz)    
def promedioejecucion(matriz, funciones, servidores):
    print("Matriz final:")
    mostramat(matriz)
    for i in range(funciones):
        acu = 0
        for j in range(servidores):
            acu = acu + matriz[i][j]
        promefun = acu / servidores
        print("Fila", i, "el tiempo promedio es:", promefun)
def promedioservidor(matriz,funciones,servidores):   
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
menumatriz()