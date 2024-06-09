from biblioteca import *
from parseador import *

continuar = True
nombre_del_archivo = "archivos/Proyectos.csv"

while continuar:
    mostrar_menu()

    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    match opcion:
        case 1:
            proyecto = validacion_alta_csv(nombre_del_archivo)
            if proyecto != False:
                print("\n\t\tProyecto agregado\n")
                escribir_csv(proyecto, nombre_del_archivo)
            else:
                print("\n\t\tIngreso mal los datos\n")
        case 2:
            id_proyecto = input("Ingrese el id del proyecto que quiere modificar: ")
            proyecto_modificado = modificar_proyecto(nombre_del_archivo, id_proyecto)
            if proyecto_modificado != False:
                print("Proyecto Modificado")
                escribir_csv(proyecto_modificado, nombre_del_archivo)  
            else :
                  print("No se pudo modificar el proyecto")  
        case 3:
            id_proyecto = input("Ingrese el id del proyecto que quiere cancelar: ")
            proyecto_cancelado = cancelar_proyecto(nombre_del_archivo, id_proyecto)
            if proyecto_cancelado != False:
                print("Proyecto Cancelado")
                escribir_csv(proyecto_cancelado, nombre_del_archivo)    
            else:
                print("No se pudo cancelar el proyecto")  
        case 4:
            proyecto_comprabado = comprobar_proyecto(nombre_del_archivo)
            escribir_csv(proyecto_comprabado, nombre_del_archivo)  
            print("Se comprobaron todos los archivos")
        case 5:
            leer_csv(nombre_del_archivo)
        case 6:
            print("Calcular presupuesto promedio")
            # calcular_presupuesto_promedio()
        case 7:
            print("Saliendo del programa...")
            continuar = False
        case _:
            print("Opción no válida, por favor intente de nuevo.")


        
       

