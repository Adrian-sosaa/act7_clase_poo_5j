print("PROGRAMACION POO")
# Definicio de clases
class Perro:
    # funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def dato_perro(self,nombre,edad):
        print(f" Nombre: {nombre} edad: {edad}")

    
# Zona de creacion de objetos
pitbull=Perro()

# zona de uso de objetos
pitbull.dato_perro("Boby", 4)
pitbull.morder()