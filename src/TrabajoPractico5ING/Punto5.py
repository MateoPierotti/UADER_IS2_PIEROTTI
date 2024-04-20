import os

# Clase Memento para almacenar el estado del archivo
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

# Clase FileWriterUtility para manejar el archivo y sus estados
class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.states = []  # Lista para almacenar los estados pasados

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.states.append(memento)  # Almacena el estado actual
        if len(self.states) > 4:  # Limita la cantidad de estados almacenados a 4
            self.states.pop(0)  # Elimina el estado más antiguo si hay más de 4 estados guardados

    def undo(self, steps=0):
        if steps < len(self.states):
            memento = self.states[-1 - steps]  # Recupera el estado según el número de pasos
            self.file = memento.file
            self.content = memento.content

# Clase FileWriterCaretaker para manejar el guardado y deshacer
class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps=0):
        writer.undo(steps)


if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar el estado anterior")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar el estado anterior a este")
    caretaker.undo(writer, 1)  # Deshace 1 paso hacia atrás
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

