import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
    __builder = None
   
    def setBuilder(self, builder):
        self.__builder = builder
	   
    def getPlane(self):
        plane = Plane()

        # Primero el chasis
        body = self.__builder.getBody()
        plane.setBody(body)

        # Luego las turbinas (2)
        i = 0
        while i < 2:
            turbinas = self.__builder.getTurbinas()
            plane.addTurbinas(turbinas)
            i += 1

        # Luego las alas (2)
        j = 0
        while j < 2:
            alas = self.__builder.getAlas()
            plane.addAlas(alas)
            j += 1
        # el tren de aterrizaje
        tren_aterrizaje = self.__builder.getTren_aterrizaje()
        plane.setTren_aterrizaje(tren_aterrizaje)

      # Retorna el vehiculo completo
        return plane

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Plane:
    def __init__(self):
        self.__alas = list()
        self.__turbinas = list()
        self.__body = None
        self.__tren_aterrizaje = None

    def setBody(self, body):
        self.__body = body

    def addAlas(self, alas):
        self.__alas.append(alas)

    def addTurbinas(self, turbinas):
        self.__turbinas.append(turbinas)

    def setTren_aterrizaje(self, tren_aterrizaje):
        self.__tren_aterrizaje = tren_aterrizaje


    def specification(self):
        print ("chasis: %s" % (self.__body.shape))
        print (f"tenemos {len(self.__turbinas)} turbinas ")
        print (f"tenemos {len(self.__alas)} alas")
        print ("tenemos un tren de aterrizaje ")

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
    def getTurbinas(self): pass
    def getAlas(self): pass
    def getTren_aterrizaje(self): pass
    def getBody(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Jeep
#* Establece instancias para tomar ruedas, motor y chasis
#* estableciendo las partes específicas que (en un Jeep) 
#* deben tener esas partes
#*-------------------------------------------------------
class AirbusBuilder(Builder):
   
    def getTurbinas(self):
        turbinas = Turbinas()
        turbinas.horsepower = 4000
        return turbinas

    def getAlas(self):
        alas = Alas()
        alas.dimenciones = 40
        return alas

    def getTren_aterrizaje(self):
        tren_aterrizaje = Tren_aterrizaje()
        tren_aterrizaje.shape = ""
        return tren_aterrizaje
    
    def getBody(self):
        body = Body()
        body.shape = "Chasis de triciclo"
        return body

#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Turbinas:
    horsepower = None
class Alas:
    dimenciones = None

class Tren_aterrizaje:
   shape = None

class Body:
   shape = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   airbusBuilder = AirbusBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Jeep
#*----------------------------------------------------------------   
   director.setBuilder(airbusBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Jeep según
#* la hoja de ruta
#*----------------------------------------------------------------
   airbus = director.getPlane()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   airbus.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
#    os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion\n")

   main()
