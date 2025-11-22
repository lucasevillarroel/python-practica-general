class Clase_Metodo:
    def __init__(self, valorInicial):
        self.atributo = valorInicial

    def accion (self, parametro):
        self.atributo = self.atributo + parametro

# Esta clase define un atributo de tipo entero y lo inicializa en valorInicial. Luego el metodo 'accion' le suma el valor que le pasamos como parametro en el llamado del metodo.