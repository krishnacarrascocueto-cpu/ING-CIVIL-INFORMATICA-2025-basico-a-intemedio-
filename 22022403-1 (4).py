# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: L-36
# PROFESOR DE TEORÍA: Carlos Vera Escobar
# PROFESOR DE LABORATORIO: Natalia Sanhueza
#
# AUTOR
# NOMBRE: Krishna Carrasco Cueto
# RUN: 22.022.403-1
# CARRERA: Fundamentos de Programación 

#defino una funcion para poder sacar los datos
def sacar_datos(archivo):
    # necesito crear el nombre del archivo y el de la carpeta cartones

    ruta_carp = "cartones/cartón_" + str(archivo) + ".txt" 
    carton_datos = []

    # abro el archivo usando el bloque with open para que despues se cierre solo
    with open(ruta_carp, "r") as archi:
        for archiv_linea in archi: 

            # .split para poder separar los números por los espacios
            espacios = archiv_linea.split()
            fila_cart = []
            i = 0

            # ciclo while para poder trasformar el texto en número entero
            while i < len(espacios):
                # agrego el numero a la fila que estamos armando
                fila_cart.append(int(espacios[i]))
                i = i + 1
            # guardo la fila completa en el carton
            carton_datos.append(fila_cart)
    return carton_datos

# defino una funcion para ver si el carton ya tiene una fila lista
def chequear_linea(el_carton, numeros_que_salieron): #apuntes de funciones

    f = 0 #f signica variable de fila para ver si completa la linea o no
    while f < len(el_carton):
        fila_ahora = el_carton[f]
        cuantos_tengo = 0
        c = 0 #c significa que recorre la columna donde se encarga de mover izquierda a derecha por los 9 espacios que tiene una sola fila del carton
        while c < len(fila_ahora):
            numero_celda = fila_ahora[c]
            # si el numero no es cero, debo buscarlo en la lista de los que me salieron
            if numero_celda != 0:
                k = 0 #la variable k significa es para ver si el numero salio o no 
            
                while k < len(numeros_que_salieron):
                    if numero_celda == numeros_que_salieron[k]:
                        cuantos_tengo = cuantos_tengo + 1
                    k = k + 1
            c = c + 1
        # segun la regla, si tengo 5 en una fila gane linea
        if cuantos_tengo == 5:
            return True
        f = f + 1
    return False

# defino una funcion para ver si el carton ya se completo entero
def chequear_lleno(el_carton, numeros_que_salieron): #apuntes de funciones 
    puntos_totales = 0
    f = 0
    while f < len(el_carton):
        fila_ahora = el_carton[f]
        c = 0 
        while c < len(fila_ahora):
            numero_celda = fila_ahora[c]
            # los ceros no valen, solo los numeros de verdad
            if numero_celda != 0:
                k = 0
                while k < len(numeros_que_salieron):
                    if numero_celda == numeros_que_salieron[k]:
                        puntos_totales = puntos_totales + 1
                    k = k + 1
            c = c + 1
        f = f + 1
    # el carton tiene 15 numeros en total segun el enunciado
    if puntos_totales == 15:
        return True
    return False

# entrada 

# pido en la entrada  la tómbola de numero segun el enunciado
text_usuario = input("Ingrese la secuencia: ")
peda_texto = text_usuario.split(",")

# proceso
numeros_juego = []
n = 0 #esta variable es para preparar los numeros que ingreso el usuario
# paso todo a una lista de numero de verdad
while n < len(peda_texto):
    numeros_juego.append(int(peda_texto[n]))
    n = n + 1

# voy a cargar los 100 cartones de una para tenerlo a mano
todos_mis_cartones = []
num_archivo = 1
while num_archivo <= 100:
    todos_mis_cartones.append(sacar_datos(num_archivo))
    num_archivo = num_archivo + 1

# creo  listas para guardar quienes ganan
lista_ganan_linea = []
lista_ganan_todo = []

# uso estas marcas para saber cuando parar de buscar
ya_hubo_linea = False #apuntes de strings boleanos 
ya_hubo_carton = False 

salieron_ahora = []
turno = 0 #esta variable significa para ir sacando los numeroos de la tombola uno por uno 

# empiezo a dar los numeros en el programa uno por uno
while turno < len(numeros_juego): #apuntes ciclos while y strings
    # entro a revisar si todavia nos falta algun ganador
    if ya_hubo_linea == False or ya_hubo_carton == False: #apuntes de condiciones 
        salieron_ahora.append(numeros_juego[turno])
        
        # reviso linea (solo hasta encontrar a los primeros)
        if ya_hubo_linea == False:
            pos = 0 #esta variable por cada numero que sale se usa esta variable pos para revisar cada uno de los 100 cartones y ver si alguno comppleto linea o carton 
            while pos < 100:
                if chequear_linea(todos_mis_cartones[pos], salieron_ahora):
                    lista_ganan_linea.append("cartón_" + str(pos + 1) + ".txt")
                pos = pos + 1
            # si encuentro a alguien, activo el pare para linea
            if len(lista_ganan_linea) > 0:
                ya_hubo_linea = True
        
        # reviso si alguien lleno el carton
        if ya_hubo_carton == False:
            pos = 0
            while pos < 100:
                if chequear_lleno(todos_mis_cartones[pos], salieron_ahora):
                    lista_ganan_todo.append("cartón_" + str(pos + 1) + ".txt")
                pos = pos + 1
            if len(lista_ganan_todo) > 0:
                ya_hubo_carton = True
                
    turno = turno + 1

# salida
# muestro los resultados finales por pantalla 
print("Cartones ganadores de línea:", lista_ganan_linea)
print("Cartones ganadores:", lista_ganan_todo)