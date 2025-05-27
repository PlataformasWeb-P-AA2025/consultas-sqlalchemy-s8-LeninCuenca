#Obtener todas las tareas asignadas a los siguientes estudiantes 

#Jennifer Bolton 
#Elaine Perez
#Heather Henderson
#Charles Harris

#En función de cada tarea, presentar el número de entregas que tiene

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from clases import Base, Entrega, Tarea, Estudiante
from config import cadena_base_datos

#se arma el camino de la base de datos
engine = create_engine(cadena_base_datos)

# Crear una sesión
session = Session(engine)
# Lista de estudiantes a consultar

estudiantes = [
    "Jennifer Bolton",
    "Elaine Perez",
    "Heather Henderson",
    "Charles Harris"
]
# Realizar la consulta 
resultado = (session.query(Tarea)
    .join(Entrega)
    .join(Estudiante)
    .filter(Estudiante.nombre.in_(estudiantes))
    .all()
)

# Recorre las tareas obtenidas
for tarea in resultado:
    num_entregas = len(tarea.entregas)
    print(f"Tarea: {tarea.titulo}, Número de Entregas: {num_entregas}")