from .controlador import ruta_archivo,leer_archivo, incrementar_id
import json

def leer_notas(nombre):
    return leer_archivo(nombre)

def guardar_notas(nota,archivo):
    ruta = ruta_archivo(archivo)
    info = leer_notas(archivo)
    nota['id_nota'] =  incrementar_id('ids', 'nota')
    info.append(nota)

    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)

def editar_notas(nota,archivo,id):
    ruta = ruta_archivo(archivo)
    info = leer_notas(archivo)

    for p in info:
        if  p['id_nota'] == id:
            p["id_curso"] = nota['id_curso']
            p["id_alumno"] = nota['id_alumno']
            p["tipo_examen"] = nota['tipo_examen']
            p["fecha"] = nota['fecha']
            p["nota"] = nota['nota']
            p["observaciones"] = nota['observaciones']
           
    with open(ruta, 'w') as f:
        json.dump(info, f, indent=4)


def buscar_nota(archivo, mail):
    info = leer_notas(archivo)

    nota = None
    for i in info:
        if i['mail'] == mail:
            nota = i
            break

    return nota
