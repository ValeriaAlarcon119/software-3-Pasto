from ed.secuenciales.nodo import NodoLSE

#Author : VALERIA ALARCON ANDRADE

class Cola:

    def __init__(self):
        """ constructor de la clase.
        """
        self.frente = NodoLSE(None)

    def es_vacia(self):
        """método que permite averiguar si la cola es o no vacia.

        Returns:
            bool: retorna true en caso de que la lista no tenga elementos, de lo contrario retorna false.
        """
        return self.frente.dato is None

    def encolar(self, nuevo_dato):
        """método que permite agregar un nuevo dato al final de la cola en caso de que sea del mismo tipo.

        Args:
            nuevo_dato (Object): dato que se agregará.

        Returns:
            bool: retorna true si el dato se logró agregar, de lo contrario retorna false.
        """
        nuevo_nodo = NodoLSE(nuevo_dato)
        nodo_actual = self.frente
        ban = False

        if self.es_vacia():
            self.frente = nuevo_nodo
            ban = True
        elif type(nuevo_dato) is type(self.frente.dato):
            while nodo_actual.sig:
                nodo_actual = nodo_actual.sig
            nodo_actual.sig = nuevo_nodo
            ban = True
        return ban

    def desencolar(self):
        """método que permite remover un dato de la cola.

        Returns:
            Object: dato que se removera de la cola.
        """
        frente_ant = self.frente
        frente_nuevo = self.frente.sig

        if self.es_vacia():
            return None
        elif frente_nuevo:
            self.frente = frente_nuevo
            self.frente.sig = frente_nuevo.sig
            return frente_ant
        else:
            self.frente = NodoLSE(None)
            return frente_ant

    def __frente__(self):
        """método que permite conocer el elemento que se encuentra en el frente de la cola.

        Returns:
            Object: objeto que esta en el frente de la cola.
        """
        return self.frente

    def __len__(self):
        """método que calcula el número de elementos en la cola.

        Returns:
            int: número de datos de la cola.
        """
        nodo_actual = self.frente
        cont = 0

        while nodo_actual:
            cont +=1
            nodo_actual = nodo_actual.sig
        return cont