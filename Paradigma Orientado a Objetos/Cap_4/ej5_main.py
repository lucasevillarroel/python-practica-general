from ej5_Fracciones import Fracciones

fraccion1 = Fracciones(1,2)
fraccion2 = Fracciones(1,4)
fraccion3 = fraccion1.suma(fraccion2)

print(f"Fracciones sumadas: {fraccion3.getNumerador()}/{fraccion3.getDenominador()}")
