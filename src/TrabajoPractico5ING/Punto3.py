class Observer:
    def update(self, event):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)


class ConcreteObserver(Observer):
    def __init__(self, id):
        self.id = id

    def update(self, event):
        if event == self.id:
            print(f"Se ha emitido un evento para el ID {self.id}")


# Crear instancias de clases observadoras con ID específicos
observer1 = ConcreteObserver("ABCD")
observer2 = ConcreteObserver("EFGH")
observer3 = ConcreteObserver("WXYZ")
observer4 = ConcreteObserver("1234")

# Crear instancia de sujeto observable
subject = Subject()

# Suscribir las clases observadoras al sujeto observable
subject.subscribe(observer1)
subject.subscribe(observer2)
subject.subscribe(observer3)
subject.subscribe(observer4)

# Emitir 8 IDs y notificar a los observadores
ids = ["ABCD", "WXYZ", "1234", "5678", "EFGH", "8765", "4321", "IJKL"]
for id in ids:
    subject.notify(id)
