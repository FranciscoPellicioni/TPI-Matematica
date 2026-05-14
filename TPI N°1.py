vec1 = [101, 102, 103, 104, 105, 106]
vec2 = [104, 105, 106, 107, 108]
vec3 = [102,105,109]
interseccion = [ ]
union = [ ]
unionC = []
diferencia = []
cont=0
cont2=0
cont3=0
for i in range (len(vec1)): #Interseccion
    if vec1[i] in vec2:
        interseccion.append(vec1[i])

for i in range (len(vec1)): #Union
    if vec1[i] not in union:
            union.append(vec1[i])

for j in range (len(vec2)): #Union
    if vec2[j] not in union:
        union.append(vec2[j])

for k in range (len(union)): #Union - C
     if union[k] not in vec3:
          unionC.append(union[k])
          
for i in range (len(vec1)): #Diferencia
    if vec1[i] not in vec2:
            diferencia.append(vec1[i])

for j in range (len(vec2)): #Diferencia
    if vec2[j] not in vec1:
        diferencia.append(vec2[j])






print("la cantida de usuarios que utilizan ambas plataformas es:",len(interseccion))
print("La cantidad de usuarios que utilizan al menos una plataforma es:",len(union))
print("la cantidad de usuarios que utilizan la api :",len(vec1),"y la cantida de usuarios que utilizan la web:",len(vec2))   
print("Usuarios que utilizan plataforma pero no presentan errores:",unionC)
print("Cantidad:",len(unionC))
print("Usuarios que utilizan exclusivamente una sola plataforma:",diferencia)
print("Cantidad:",len(diferencia))