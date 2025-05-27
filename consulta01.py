#Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte. 
# En función de la entrega, presentar, nombre del tarea, nombre del estudiante, 
# calificación, nombre de instructor y nombre del departamento

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from clases import Base, Departamento, Curso,Tarea, Entrega
from config import cadena_base_datos
#se arma el camino de la base de datos

engine = create_engine(cadena_base_datos)

# Crear una sesión
session = Session(engine)

# Realizar la consulta
resultado = (session.query(Entrega)
    .join(Entrega.tarea)
    .join(Tarea.curso)
    .join(Curso.departamento)
    .filter(Departamento.nombre == "Arte")
    .all()
)

for entrega in resultado:
    tarea = entrega.tarea
    estudiante = entrega.estudiante
    curso = tarea.curso
    instructor = curso.instructor
    departamento = curso.departamento
    print(f"Tarea: {tarea.titulo}, Estudiante: {estudiante.nombre}, Calificación: {entrega.calificacion}, Instructor: {instructor.nombre}, Departamento: {departamento.nombre}")