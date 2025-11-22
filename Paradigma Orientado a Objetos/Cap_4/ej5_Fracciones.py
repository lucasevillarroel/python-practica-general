class Fracciones():

# Constructor
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

# Getters y Setters
    def getNumerador(self):
        return self.numerador

    def setNumerador(self):
        pass

    def getDenominador(self):
        return self.denominador

    def setDenominador(self):
        pass

# Metodos
    def suma(self, fraccion):
        nuevoNumerador = ((self.numerador * fraccion.getDenominador())+(fraccion.getNumerador()*self.denominador))
        nuevoDenominador = self.denominador * fraccion.getDenominador()
        return Fracciones(nuevoNumerador, nuevoDenominador)

    def resta(self):
        pass
    def multiplicacion(self):
        pass
    def division(self):
        pass