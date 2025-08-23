# Declaracion de una clase
class Persona:
    """
        Clase que representa a una persona con nombre y edad.
    """
    def __init__(self,nombre,edad):
        """
        Inicializa una instancia de la clase Persona.
        :param nombre: Nombre de la persona.
        :param edad: Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        """
        Imprime un saludo personalizado.
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    def __str__(self):
        """
        Devuelve una representación en cadena de la persona.
        :return: Cadena con el nombre y la edad de la persona.
        """
        return f"{self.nombre}, {self.edad} años"
    def __repr__(self):
        """
        Devuelve una representación en cadena de la persona para depuración.
        :return: Cadena con el nombre y la edad de la persona.
        """
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
### HERENCIA ###
class Estudiante(Persona):
    """
        Clase que representa a un estudiante, hereda de Persona.
    """
    def __init__(self,nombre,edad,carrera):
        """
        Inicializa una instancia de la clase Estudiante.
        :param nombre: Nombre del estudiante.
        :param edad: Edad del estudiante.
        :param carrera: Carrera del estudiante.
        """
        super().__init__(nombre,edad)
        self.carrera = carrera
    def estudiar(self):
        """
        Imprime un mensaje indicando que el estudiante está estudiando.
        """
        print(f"{self.nombre} está estudiando la carrera {self.carrera}.")
    def __str__(self):
        """
        Devuelve una representación en cadena del estudiante.
        :return: Cadena con el nombre, la edad y la carrera del estudiante.
        """
        return f"Estudiante(nombre={self.nombre},edad= {self.edad},carrera={self.carrera})"
p1 = Persona("Juan",30)
e1 = Estudiante("Ana",22,"Ingeniería de software")

# LLamada a los métodos
p1.saludar()
e1.saludar()
e1.estudiar()

print(p1)
print(e1)
print(f"Representación de p1: {repr(p1)}")
print(f"Representación de e1: {repr(e1)}")