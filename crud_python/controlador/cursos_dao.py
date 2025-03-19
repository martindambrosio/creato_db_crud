from .controlador import ruta_archivo, leer_archivo, incrementar_id
import json

def leer_curso(nombre):
    return leer_archivo(nombre)

def guardar_curso(curs, archivo):
    ruta = ruta_archivo(archivo)
    info = leer_curso(archivo)
    curs['id_curso'] = incrementar_id('ids', 'curso')
    info.append(curs)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def editar_curso(curs, archivo, id):
    ruta = ruta_archivo(archivo)
    info = leer_curso(archivo)

    for p in info:
        if p ['id_curso'] == id:
            p["nombre"] = curs['nombre']
            p["id_profesor"] = curs['id_profesor']
            p["nivel"] = curs['nivel']
            p["turno"] = curs['turno']
            p["dia"] = curs['dia']
            p["horario"] = curs['horario']
            p["costo"] = curs['costo']
            p["estado"] = curs['estado']
    
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def eliminar_curso(archivo, id):
    ruta = ruta_archivo(archivo)
    info = leer_curso(archivo)
    borrar = None
    for i, dato in enumerate(info):
        if dato['id_curso'] == id:
            borrar = i
            break

    del info[borrar]
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)
        
def buscar_curso(archivo, id):
    info = leer_curso(archivo)

    curs = None
    for i in info:
        if i['id_curso'] == str(id):
            curs = i
            break

    return curs