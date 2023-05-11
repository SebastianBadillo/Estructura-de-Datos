class Nodo:
    # Constructor
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    # Método Ver el valor
    def devolver_valor(self):
        print(self.valor)

    # Método asignar siguiente
    def asignar_siguiente(self, nodo):
        self.siguiente = nodo # Aqui se genera el 
    
    #Me todo cambiar valor al nodo
    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor
    
Nodo1 = Nodo('A')
Nodo2 = Nodo('C')
#print(Nodo1.siguiente)  

# Primera forma
Nodo1.devolver_valor()

# Segunda forma, apartir del metodo indicando el objeto
Nodo.devolver_valor(Nodo1)

Nodo1.cambiar_valor('B')

Nodo1.devolver_valor()

Nodo1.asignar_siguiente(Nodo2)
print(Nodo1)
print(Nodo1.siguiente)
print(Nodo2)


    
