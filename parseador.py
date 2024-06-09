import os
import csv

def escribir_csv(csv_parseado, nombre_archivo: str):
  
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv: 
        writer = csv.DictWriter(archivo_csv, fieldnames=csv_parseado[0].keys())
        writer.writeheader()
        for proyecto in csv_parseado:
            presupuesto = proyecto["Presupuesto"].replace('"', '')  
            proyecto["Presupuesto"] = presupuesto
            writer.writerow(proyecto)

def leer_csv(nombre_archivo: str):
    lista_elementos = [] 

    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding='utf-8') as archivo:  
                reader = csv.DictReader(archivo)
                for fila in reader:
                    lista_elementos.append(fila)
            return lista_elementos
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return []
    else:
        print("Archivo no encontrado")
        return []
