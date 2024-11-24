class Asignatura:

    def __init__(self, nombre, salon="remoto"): # En main se utiliza una vez sin salon.
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        return f"{self._nombre} {self._salon}"
