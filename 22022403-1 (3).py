# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: 10145-0-C-1 / 10145-0-L-36
# PROFESOR DE TEORÍA: CARLOS VERA ESCOBAR 
# PROFESOR DE LABORATORIO: NATALIA SANHUEZA
#
# AUTOR
# NOMBRE: KRISHNA CARRASCO CUETO
# RUN: 22.022.403-1
# CARRERA: Bachillerato con mención Ingeniería Civil Informática
# Entrada
# escribo las 5 entradas que me pide el enunciado para tomar los datos 
torre_1 = input("Ingrese las torres del primer jugador: ")
torre_2 = input("Ingrese las torres del segundo jugador: ")
torre_3 = input("Ingrese las torres del tercer jugador: ")
torre_4 = input("Ingrese las torres del cuarto jugador: ")
ataques = input("Ingrese los ataques: ")
# Proceso
# creo una funciona para ver las entradas, y hago listas para poder almacenar los datos
def como_esta_la_torre(torre1, torre2, torre3, torre4, numero_de_ataques):
    # "cree unas listas para poder almacenar los datos que necesito para la entrada"
    nomb_torre = [] # "nombre de las torres"
    posic_torr = []
    est_viva = [] # "para ver si la torre esta viva o destruida"
    jug_torres = [torre1, torre2, torre3, torre4]
    # ocuparemos un ciclo for para las entradas, el ciclo for hace que recorre las listas de las torres una por una
    for torres_entrada in jug_torres: # apunter de iterativos y teoria
        sepa_torre = torres_entrada.split(",") # separamos por coma para tener cada torre solita (apunte listas)
        for torr in sepa_torre:
            torr = torr.strip() # ocupo .strip para elimiar espacios en blanco
            # evitar errores de comparacion en el string (apuntes listas)
            datos_torr = torr.split(":") # ocupo .split para separar los nombres con (apuntes listas)
            nomb_torre.append(datos_torr[0].strip()) # ocupe .append para poder contar los elementos de la lista (apunte listas)
            posic_torr.append(datos_torr[1].strip())
            est_viva.append(True) # Solo si al principio están vivas osea que sean verdaderas
    # ahora necesito separar la cadena de ataques por la coma segun el enunciado (teoria)
    list_de_ataque = numero_de_ataques.split(",") # separo con la coma con .split (apuntes listas)
    # creo un índice para saber en qué posición de la lista esta    
    posicion_ataque = 0
    # el ciclo se repite mientras la posición sea menor al largo de la lista
    while posicion_ataque < len(list_de_ataque):
        ataque_atk_crudo = list_de_ataque[posicion_ataque]
        #limpio espacios con .strip y separamos por la flecha "->" con .split (apuntes listas) 
        ataque_atk = ataque_atk_crudo.strip()
        deta_espacio = ataque_atk.split("->") 
        # identifico quién ataca y a qué posición apunta 
        qn_ataca = deta_espacio[0].strip()  # qn = quien ataca
        dnd_ataca = deta_espacio[1].strip() # dnd = donde ataca
        indice_ataque = -1  # para verificar si la busqueda fue correcta o no 
        i_busqueda = 0
        while i_busqueda < len(nomb_torre): # buscamos el índice de la torre que ataca
            if nomb_torre[i_busqueda] == qn_ataca:
                indice_ataque = i_busqueda 
            i_busqueda += 1 # variable de indice de busqueda
        # aplica si la torre que ataca ya estaba destruida
        if est_viva[indice_ataque] == False:
            print("Ataque: " + ataque_atk + ", " + qn_ataca + " torre no puede atacar.")
        else:
            # en el caso que la torre este viva, se busca a alguien si le pega
            obj_encontrado = False 
            nom_destruido = ""
            ind = 0
            while ind < len(posic_torr): # solo destruye si la posicion coincide y si no ha encontrado otro obj antes
                if posic_torr[ind] == dnd_ataca and est_viva[ind] == True and obj_encontrado == False:
                    est_viva[ind] = False 
                    nom_destruido = nomb_torre[ind]
                    obj_encontrado = True
                ind += 1
            # en el caso de que el ataque destruyo la torre 
            if obj_encontrado == True:
                print("Ataque: " + ataque_atk + ", destruye " + nom_destruido + ".")
            # en este caso ocupamos el else en caso de que este ataque falle 
            else:
                print("Ataque: " + ataque_atk + ", falla.") 
        # sumo 1 al índice para pasar al siguiente ataque
        posicion_ataque = posicion_ataque + 1
    # variables para conteo final
    letras_de_resultados = ["A", "B", "C", "D"]
    conteo_de_resultados = [0, 0, 0, 0]
    # actualizar el estado de la guerra para ver cuantas torres quedan
    i = 0
    while i < len(nomb_torre):
        if est_viva[i] == True:
            qn = nomb_torre[i][0] # letra del jugador
            let = 0
            while let < 4:
                if letras_de_resultados[let] == qn:
                    conteo_de_resultados[let] += 1
                let += 1
        i += 1
    #ordenar de mayor a menor con desempate alfabetico 
    list_pasada = 0
    while list_pasada < 4:
        i = 0
        while i < 3:
            camb = False 
            # ordenar de mayor a menor por puntaje
            if conteo_de_resultados[i] < conteo_de_resultados[i+1]:
                camb = True
            # si hay empate, ordenar alfabéticamente
            elif conteo_de_resultados[i] == conteo_de_resultados[i+1]:
                if letras_de_resultados[i] > letras_de_resultados[i+1]:
                    camb = True
            # si se debe hacer el cambio, intercambio los valores en ambas listas
            if camb == True: 
                aux_conteo = conteo_de_resultados[i]
                conteo_de_resultados[i] = conteo_de_resultados[i+1]
                conteo_de_resultados[i+1] = aux_conteo
                aux_letra = letras_de_resultados[i]
                letras_de_resultados[i] = letras_de_resultados[i+1]
                letras_de_resultados[i+1] = aux_letra
            i = i + 1
        list_pasada = list_pasada + 1
    # Salida
    lista_para_retornar = [] #cree una lista vacia para poder hacer la salida de la funcion con el retorno y el .append para poder contar y el str para poder concatenar (apuntes listas)
    for i in range (4):
        salida_result =letras_de_resultados[i] + ": " + str(conteo_de_resultados[i]) 
        lista_para_retornar.append(salida_result)
    return(lista_para_retornar)
resultados = como_esta_la_torre(torre_1, torre_2, torre_3, torre_4, ataques) 
#se imprime los resultados finales de una manera ordenada y clara, donde la lista que devolvio la funcion con su print
print("Resultados:")
for salida_retu in resultados:
    print(salida_retu)