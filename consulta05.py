#5. 
#5.1 En una consulta, obtener todos los cursos.
#5.2 Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso (con otra consulta), 
#y presentar el promedio de calificaciones de las entregas

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from clases import Base, Curso, Entrega, Tarea
from config import cadena_base_datos

#se arma el camino de la base de datos
engine = create_engine(cadena_base_datos)

# Crear una sesión
session = Session(engine)

#5.1 Obtener todos los cursos
cursos = session.query(Curso).all()
#5.2 Iterar sobre cada curso y obtener las entregas, calculando el promedio de calificaciones
for curso in cursos:
    entregas = (
        session.query(Entrega)
        .join(Entrega.tarea)
        .filter(Tarea.curso_id == curso.id)
        .all()
    )

    if entregas:
        promedio = sum(e.calificacion for e in entregas) / len(entregas)
        print(f"Curso: {curso.titulo}, Promedio de Calificaciones: {promedio}")