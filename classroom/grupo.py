from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12" # Se espera este formato en el print.

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]): # Estudiantes debe tener valor por defecto
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 1"): # Se espera que este por defecto sea 1
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
