def inter(vec1,vec2,interseccion):
    for i in range (len(vec1)): #Interseccion
        if vec1[i] in vec2:
            interseccion.append(vec1[i])
    print("la cantida de usuarios que utilizan ambas plataformas es:",len(interseccion))


def uni(vec1,vec2,union,vec3,unionC,cUnion):
    for i in range (len(vec1)): #Union
        if vec1[i] not in union:
            union.append(vec1[i])

    for j in range (len(vec2)): #Union
        if vec2[j] not in union:
            union.append(vec2[j])
    print("La cantidad de usuarios que utilizan al menos una plataforma es:",len(union))

    for k in range (len(union)): #Union - C
        if union[k] not in vec3:
            unionC.append(union[k])
    print("Usuarios que utilizan plataforma pero no presentan errores:",unionC)
    print("Cantidad:",len(unionC))

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

def union_vec1_vec2_vec3(vec1,vec2,vec3,usuarios):
    
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

def es_critico(p,q,r):
    return(p or q) and r

def critico(usuarios,vec1,vec2,vec3,criticos,no_criticos,usuario):

    for i in range(len(usuarios)):
        usuario = usuarios[i]

        p = usuario in vec1
        q = usuario in vec2
        r = usuario in vec3

        if es_critico(p, q, r):
            criticos.append(usuario)
        else:
            no_criticos.append(usuario)

    print("Usuarios críticos:", criticos)
    print("Cantidad:", len(criticos))

    print("Usuarios no críticos:", no_criticos)
    print("Cantidad:", len(no_criticos))


def definicion():

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
    inter(vec1,vec2,interseccion)
    uni(vec1,vec2,union,vec3,unionC,cUnion)
    dif(vec1,vec2,diferencia)
    union_vec1_vec2_vec3(vec1,vec2,vec3,usuarios)
    critico(usuarios,vec1,vec2,vec3,criticos,no_criticos,usuario)
   

definicion()




