# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA 
# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN 
# 
# AUTOR 
# NOMBRE: Krishna Carrasco Cueto
# RUN: 22022403-1

# defino una funcion para poder transformar el tiempo (apuntes de funciones)
def trans_tiempo(total_seg): 
    horas_tiem = total_seg // 3600 # para poder obtener las horas mediante division entera por 3600 ( 1 hora = 3600s) 
    resto = total_seg % 3600 # necesito tener el sobro de las horas para poder calcular los minutos
    minutos_tiem = resto // 60 # paso los minutos que me sobran en segundo
    segundos_tiem = resto % 60 # para saber el resultado final de los segundos restantes 

    # necesito concatenar con str para poder pasar los numeros en formato texto (apuntes de introduccion de python) 
    resultado_final_del_tiempo = str(horas_tiem) + "h" + str(minutos_tiem) + "m" + str(segundos_tiem) + "s" 
    return resultado_final_del_tiempo # retorno para sea formateado los datos en el archivo (apuntes funciones y archivos)


# defino una segunda funcion para leer lo que tiene el archivo general
def leer_arch(entrada_archivo):
    with open(entrada_archivo, "r") as archivo_de_entr:
        lineas_leer = archivo_de_entr.readlines() # leeo con .readlines las lineas del archivo (apuntes archivos)
    return lineas_leer

# ahora puedo hacer mi bloque de entrada solicitando lo que me pide el enunciado 
# Entrada

archi_nomb_abrir = input("Ingrese el nombre del archivo: ") 
lineas_datos = leer_arch(archi_nomb_abrir) # llamo a la funcion para obtener la lista de lineas (apunte de funciones y los ejemplos de archivo)

# Procesamiento y Salida
# creo el archivo Log-procesado.csv del que me dice el enunciado
with open("Log-procesado.csv", "w") as archivo_salida: #ocupo el bloque  with open para hacer la apertura del archivo y haci poder realizar la lectura respectiva
    # la primera linea debe tener  (job, time)
    prime_linea = lineas_datos[0].strip()
    archivo_salida.write(prime_linea)
    
    # recorro los datos desde la segunda linea
    indice = 1
    while indice < len(lineas_datos): #por eso ocupo el ciclo while y el len para poder contar la cantidad de caracteres (apuntes de iterativos y strings)
        linea_actual = lineas_datos[indice].strip()
        
        if linea_actual != "":
            # separo el nombre del trabajo y el tiempo por la coma 
            partes = linea_actual.split(",") #lo ocupo para  poder buscar todas las comas en el texto y lo corto en pedazos justo en ese punto (apuntes listas)
            nombre_job = partes[0].strip() # lo  necesito para poder eliminar esos espacios en blanco
            # convierto a entero para poder procesarlo en la funcion
            segundos_valor = int(partes[1].strip())
            
            # obtengo el formato que me pide y le hago el llamado con la variable de trans_tiempo donde defini la funcion
            tiempo_legible = trans_tiempo(segundos_valor)
            
            # uso  "\n" al inicio para que la ultima linea no tenga salto al final 
            nueva_linea = "\n" + nombre_job + "," + tiempo_legible
            archivo_salida.write(nueva_linea)
            
        indice = indice + 1
#el archivo se debe cerrar automaticamente al terminar con el bloque with
