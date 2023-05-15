class Nodo:
    # Constructor
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None


class List:
    def __init__(self):
        self.inicio = None
        self.size = 0

    def add(self, valor):
        nuevo_nodo = Nodo(valor)
        if (self.inicio == None):
            self.inicio = nuevo_nodo
        else:
            nodo_iterador = self.inicio
            while nodo_iterador.siguiente != None:
                nodo_iterador = nodo_iterador.siguiente
            nodo_iterador.siguiente = nuevo_nodo
        self.size += 1
    
    def delete(self, value):
        nodo_actual = self.inicio
        nodo_anterior = None
        key = False
        while nodo_actual != None:
            if nodo_actual.valor == value:
                key = True
                if nodo_anterior == None:
                    self.inicio = nodo_actual.siguiente
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    nodo_actual = nodo_actual.siguiente
            else:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
        if key == False:
            return 'The element is not in the list'
        else: 
            self.size -=1   
 
    
    def find_value(self, value):
        nodo_iterador = self.inicio
        indice = 0
        key = False
        for x in range(0, self.size):
            if nodo_iterador.valor == value:
                key = True
                return indice
            else:
                nodo_iterador = nodo_iterador.siguiente
            indice +=1
        if(key != True):
            return 'sorry, element is not in the list'
        
    def find_by_index(self,index):
        nodo_iterador = self.inicio
        if index >= self.size :
            return 'index out of bounds'
        else:
            for x in range(0, index):
                nodo_iterador = nodo_iterador.siguiente  
            return nodo_iterador.valor
    
    def add_first(self, value):
        nuevo_nodo = Nodo(value)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo
    
    def __str__(self):
        if self.inicio == None:
            return '[]'
        else:
            elementos = []
            nodo_iterador = self.inicio
            while nodo_iterador != None:
                elementos.append(str(nodo_iterador.valor))# El str es necesario para poder usar el metodo join mas adelante
                nodo_iterador = nodo_iterador.siguiente
            return '[' + ', '.join(elementos) + ']'
            
       
        
