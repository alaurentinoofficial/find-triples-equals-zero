import time

class Cronometro:
    def __init__(self):
        self.__inicio = None
        self.__tempo_passado = 0
    
    def Iniciar(self):
        self.__inicio = time.clock()
    
    def Parar(self):
        if self.__inicio is not None:
            self.__tempo_passado = time.clock() - self.__inicio
    
    def Exibir(self):
        if self.__tempo_passado is None:
            return time.clock() - self.__inicio
        
        return self.__tempo_passado
    
    def Zerar(self):
        self.__inicio = None
        self.__tempo_passado = None
    
    def __str__(self):
        return str(self.Exibir())
    
    def __repr__(self):
        return "Cronometro.Cronometro()"