from .controlador import ruta_archivo,leer_archivo, incrementar_id
import json

def leer_alumno(nombre):
    return leer_archivo(nombre)

def guardar_alumno(persona,archivo):
    ruta = ruta_archivo(archivo)
    info = leer_alumno(archivo)
    persona['id_alumno'] =  incrementar_id('ids', 'alumno')
    info.append(persona)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def editar_alumno(persona,archivo,id):
    ruta = ruta_archivo(archivo)
    info = leer_alumno(archivo)

    for p in info:
        if p ['id_alumno'] == id:
            p["nombre"] = persona['nombre']
            p["apellido"] = persona['apellido']
            p["documento"] = persona['documento']
            p["direccion"] = persona['direccion']
            p["telefono"] = persona['telefono']
            p["mail"] = persona['mail']

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def eliminar_alumno(archivo,id):
    ruta = ruta_archivo(archivo)
    info = leer_alumno(archivo)
    borrar = None
    for i, dato in enumerate(info):
        if dato['id_alumno'] == id:
            borrar = i
            break

    del info[borrar]
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def buscar_alumno(archivo, mail):
    info = leer_alumno(archivo)

    persona = None
    for i in info:
        if i['mail'] == mail:
            persona = i
            break

    return persona

