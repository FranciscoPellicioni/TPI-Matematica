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
        print("6-volver al menu principal")
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
        if choice==6:
            resultado=False
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
def inter(vec1,vec2,interseccion):
    for i in range (len(vec1)): #Interseccion
        if vec1[i] in vec2:
            interseccion.append(vec1[i])
    print("la cantida de usuarios que utilizan ambas plataformas es:",len(interseccion))


def uni(vec1,vec2,union):
    for i in range (len(vec1)): #Union
        if vec1[i] not in union:
            union.append(vec1[i])

    for j in range (len(vec2)): #Union
        if vec2[j] not in union:
            union.append(vec2[j])
    print("La cantidad de usuarios que utilizan al menos una plataforma es:",len(union))
    return union


def union_c(union,vec3,unionC):
    for k in range (len(union)): #Union - C
        if union[k] not in vec3:
            unionC.append(union[k])
    print("Usuarios que utilizan una plataforma pero no presentan errores:",unionC)
    print("Cantidad:",len(unionC))
    

def c_union(vec3,union,cUnion):
    for l in range(len(vec3)): #C - Union
        if vec3[l] not in union:
            cUnion.append(vec3[l])
    print("Usuarios que estan en C pero no en AuB:",cUnion)


def dif(vec1,vec2,diferencia):          
    for i in range (len(vec1)): #Diferencia
        if vec1[i] not in vec2:
            diferencia.append(vec1[i])

    for j in range (len(vec2)): #Diferencia
        if vec2[j] not in vec1:
            diferencia.append(vec2[j])
    print("Usuarios que utilizan exclusivamente una sola plataforma:",diferencia)
    print("Cantidad:",len(diferencia))


def union_vec1_vec2_vec3(vec1,vec2,vec3,usuarios): #Union de todos los usuarios
    
    for i in range(len(vec1)):
        if vec1[i] not in usuarios:
            usuarios.append(vec1[i])

    for j in range(len(vec2)):
        if vec2[j] not in usuarios:
            usuarios.append(vec2[j])

    for k in range(len(vec3)):
        if vec3[k] not in usuarios:
            usuarios.append(vec3[k])
    print("Usuarios totales:",usuarios)
    return usuarios


def es_critico(p,q,r): #Evaluar la expresion (pVq) /\ r
    return(p or q) and r
    
def critico(usuarios,vec1,vec2,vec3,criticos,no_criticos,usuario): #Verificar usuarios criticos

    for i in range(len(usuarios)):
        usuario = usuarios[i]
        #Verifica si el usuario existe en cada vector
        p = usuario in vec1
        q = usuario in vec2
        r = usuario in vec3
        print("TABLA DE VERDAD")
        print(p,q,r)
        if es_critico(p, q, r): #llamar funcion es_critico
            criticos.append(usuario)
        else:
            no_criticos.append(usuario)
        
    print("Usuarios críticos:", criticos)
    print("Cantidad:", len(criticos))

    print("Usuarios no críticos:", no_criticos)
    print("Cantidad:", len(no_criticos))


def menu():
    print("\nMENU")
    print("1. Usuarios que utilizan ambas plataformas")
    print("2. Usuarios que utilizan al menos una plataforma")
    print("3. Usuarios que utilizan la plataforma, pero no presentan errores")
    print("4. Usuarios que aparecen en C pero no en AuB")
    print("5. Usuarios que utilizan exclusivamente una sola plataforma")
    print("6. Mostrar todos los usuarios")
    print("7. Verificar usuarios criticos")
    print("8. volver al menu principal")


def definicion(): #Definir vectores y llamar funciones

    vec1 = [101, 102, 103, 104, 105, 106]
    vec2 = [104, 105, 106, 107, 108]
    vec3 = [102,105,109]
    interseccion = [ ]
    union = [ ]
    unionC = []
    diferencia = []
    cUnion = []
    usuarios = []
    usuario = []
    criticos = []
    no_criticos = []
    opcion = 0
    while opcion != 8:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            inter(vec1,vec2,interseccion)
        elif opcion == 2:
            uni(vec1,vec2,union)
        elif opcion == 3:
            union_c(union,vec3,unionC)
        elif opcion == 4:
            c_union(vec3,union,cUnion)
        elif opcion == 5:
            dif(vec1,vec2,diferencia)
        elif opcion == 6:
            union_vec1_vec2_vec3(vec1,vec2,vec3,usuarios)
        elif opcion == 7:
            critico(usuarios,vec1,vec2,vec3,criticos,no_criticos,usuario)
        elif opcion == 8:
            print("volver al menu principal")
        else:
            print("Opcion invalida")
def menugeneral():
    resultado = True
    while resultado:
        print("------menu principal------")
        print("1- Unidad conjuntos")
        print("2- Unidad matrices")
        print("3-salir del sistema")
        choicee=int(input("ingrese al menu que desea acceder:(1 o 2)"))
        if choicee==1:
            definicion()
        elif choicee==2:
            menumatriz()
        elif choicee==3:
            print("ejecucion terminada con exito")
            resultado=False
if __name__ == "__main__":
    menugeneral()