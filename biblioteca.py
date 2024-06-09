from parseador import *
import re
from datetime import datetime

def mostrar_menu():
    print("1-Ingresar Proyecto")
    print("2-Modificar Proyecto")
    print("3-Cancelar Proyecto")
    print("4-Comprobar proyectos")
    print("5-Mostrar Todos")
    print("6-Calcular presupuesto promedio")
    print("7-Salir")

def devolver_id_disponible(nombre_archivo):
    csv_parseado = leer_csv(nombre_archivo)  
    if not csv_parseado:
        print("El archivo CSV está vacío o no se encontró.")
        return 1 
    lista_lenght = len(csv_parseado) 
    if lista_lenght == 0:
        print("No hay proyectos en el archivo CSV.")
        return 1
    ultima_id = int(csv_parseado[lista_lenght - 1]["id"])
    return ultima_id + 1

def ValidarNombre(nombre: str) -> bool:
    return bool(re.match(r"^[A-Za-z\s]{1,30}$", nombre))

def ValidarDescripcion(descripcion: str) -> bool:
    return len(descripcion) <= 200

def ValidarPresupuesto(presupuesto: str) -> bool:
    return presupuesto.isdigit() and int(presupuesto) >= 500000

def ValidarFecha(fecha: str) -> bool:
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def ValidarEstado(estado: str) -> bool:
    return estado in ['Activo', 'Cancelado', 'Finalizado']

def ValidarFechasInicioFin(fecha_inicio: str, fecha_fin: str) -> bool:
    try:
        inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
        fin = datetime.strptime(fecha_fin, "%d-%m-%Y")
        return fin >= inicio
    except ValueError:
        return False
    
def validacion_alta_csv(nombre_archivo):
    id_proyecto = devolver_id_disponible(nombre_archivo)
    nombre_del_proyecto = input("Ingresa el nombre del proyecto: ")
    descripcion = input("Ingresa la descripcion: ")
    presupuesto = input("Ingresa presupuesto: ")
    fecha_de_inicio = input("Ingresa la fecha de inicio: ")
    fecha_de_final = input("Ingresa la fecha final: ")
    estado = input("Ingresa estado del proyecto: ")

    if ValidarNombre(nombre_del_proyecto) and ValidarDescripcion(nombre_del_proyecto) and ValidarPresupuesto(presupuesto) and ValidarFecha(fecha_de_inicio) and ValidarFecha(fecha_de_final) and ValidarFechasInicioFin(fecha_de_inicio,fecha_de_final):
        nuevo_proyecto = {
        "id": id_proyecto,
        "Nombre del Proyecto": nombre_del_proyecto,
        "Descripción": descripcion,
        "Fecha de inicio": fecha_de_inicio,
        "Fecha de Fin": fecha_de_final,
        "Presupuesto": presupuesto,
        "Estado": estado
        }
        csv_parseado = leer_csv(nombre_archivo)  
        csv_parseado.append(nuevo_proyecto)
        return csv_parseado
    else:
        return False

def cancelar_proyecto(nombre_archivo, id_proyecto):
    csv_parseado = leer_csv(nombre_archivo)     
    for proyectos in csv_parseado:
        if proyectos["id"] == id_proyecto:
             proyectos["Estado"] = "Cancelado";
             print(id_proyecto)
             return csv_parseado
    return False

def modificar_proyecto(nombre_archivo, id_proyecto):

    csv_parseado = leer_csv(nombre_archivo) 
    validacion = False
    for proyectos in csv_parseado:
        if proyectos["id"] == id_proyecto:   
            opcion = sub_menu_datos_modificar()
            if opcion != False:
                match opcion:
                    case 1:
                        nombre_del_proyecto = input("Ingresa el nombre del proyecto: ")
                        validacion = ValidarNombre(nombre_del_proyecto)
                        if validacion:
                            proyectos["Nombre del Proyecto"] = nombre_del_proyecto
                    case 2:
                        descripcion = input("Ingresa la descripcion: ")
                        validacion = ValidarDescripcion(descripcion)
                        if validacion:
                            proyectos["Descripción"] = descripcion
                    case 3:
                        presupuesto = input("Ingresa presupuesto: ")
                        validacion = ValidarPresupuesto(presupuesto)
                        if validacion:
                            proyectos["Presupuesto"] = presupuesto
                    case 4:
                        fecha_de_inicio = input("Ingresa la fecha de inicio: ")
                        validacion = ValidarFecha(fecha_de_inicio)
                        if validacion:
                            validacion = ValidarFechasInicioFin(fecha_de_inicio, proyectos["Fecha de Fin"])
                            if validacion:
                                proyectos["Fecha de inicio"] = fecha_de_inicio
                    case 5:
                        fecha_de_final = input("Ingresa la fecha final: ")
                        validacion = ValidarFecha(fecha_de_final)
                        if validacion:
                            validacion = ValidarFechasInicioFin(proyectos["Fecha de inicio"], fecha_de_final)
                            if validacion:
                                proyectos["Fecha de Fin"] = fecha_de_final
                    case 6:
                        estado = input("Ingresa estado del proyecto: ")
                        validacion = ValidarEstado(estado)
                        if validacion:
                            proyectos["Estado"] = estado
                if validacion != False:
                    return csv_parseado     
            else : 
                print("Opcion invalida")
    return False

def sub_menu_datos_modificar():
        print("\nSubmenú de Modificación de Datos:")
        print("1. Nombre del Proyecto")
        print("2. Descripción")
        print("3. Presupuesto")
        print("4. Fecha de inicio")
        print("5. Fecha de finalización")
        print("6. Estado")
        print("7. Terminar Modificación")

        opcion = int(input("Selecciona una opción: "))
        if opcion <= 7 and opcion >= 1:
            return opcion
        return False

def comprobar_proyecto(nombre_archivo):
    csv_parseado = leer_csv(nombre_archivo)

    for proyectos in csv_parseado:
        if proyectos["Estado"] == "Activo" and comparar_fechas(proyectos["Fecha de inicio"],proyectos["Fecha de Fin"]):
            print(f"proyecto {proyectos["Nombre del Proyecto"]} pasa a estado finalizado")
            proyectos["Estado"] = "Finalizado"
    return csv_parseado
    



def comparar_fechas(fecha_inicial_str, fecha_final_str):
    try:
        # Parsear las fechas a objetos datetime
        fecha_inicial = datetime.strptime(fecha_inicial_str, "%d-%m-%Y")
        fecha_final = datetime.strptime(fecha_final_str, "%d-%m-%Y")
        
        # Comparar las fechas
        return fecha_inicial > fecha_final
    except ValueError:
        print("Error: Las fechas no tienen el formato correcto (dd-mm-yyyy).")
        return False







    

