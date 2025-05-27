#Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, 
# calificación, nombre de instructor y nombre del departamento

from sqlalchemy import create_engine, select, join
from sqlalchemy.orm import Session
from clases import Base, Departamento, Instructor, Curso, Estudiante, Tarea, Entrega
from config import cadena_base_datos
#se arma el camino de la base de datos

engine = create_engine(cadena_base_datos)

# Crear una sesión
session = Session(engine)

# Realizar la consulta solicitada
resultado = (
    session.query( Entrega,Tarea.titulo.label("nombre_tarea"), Estudiante.nombre.label("nombre_estudiante"),Entrega.calificacion,Instructor.nombre.label("nombre_instructor"),Departamento.nombre.label("nombre_departamento"))
    .join(Entrega.tarea)
    .join(Tarea.curso)
    .join(Curso.departamento)
    .join(Curso.instructor)
    .join(Entrega.estudiante)
    .filter(Departamento.nombre == "Arte")
    .all()
)

for entrega, nombre_tarea, nombre_estudiante, calificacion, nombre_instructor, nombre_departamento in resultado:
    print(f"Tarea: {nombre_tarea}, Estudiante: {nombre_estudiante}, Calificación: {calificacion}, Instructor: {nombre_instructor}, Departamento: {nombre_departamento}")