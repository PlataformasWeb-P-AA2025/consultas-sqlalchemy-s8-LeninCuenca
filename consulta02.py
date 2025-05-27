#Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 . 
# En función de los departamentos, presentar el nombre del departamento y el 
# número de cursos que tiene cada departamento
# #
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from clases import Base, Departamento, Curso, Tarea, Entrega
from config import cadena_base_datos

#se arma el camino de la base de datos
engine = create_engine(cadena_base_datos)

# Crear una sesión
session = Session(engine)

# Consulta todos los departamentos que tengan al menos una entrega con calificación <= 0.3
departamentos = (session.query(Departamento)
    .join(Curso)
    .join(Tarea)
    .join(Entrega)
    .filter(Entrega.calificacion <= 0.3)
    .all()
)
# Recorre los departamentos filtrados
for departamento in departamentos:
    num_cursos = len(departamento.cursos)
    print(f"Departamento: {departamento.nombre}, Número de Cursos: {num_cursos}")