import time
import os
class ej3_Reloj_Digital:
    def __init__(self):
        self.maxMinSeg = 59
        self.maxHora = 1
        self.minVal = 0
        self.valActSeg = 0
        self.valActMin = 0
        self.valActHora = 0

    def setLimite(self):
        pass

    def getValorActual(self):
        return self.valActual

    def incrementar(self):
        while self.valActHora < self.maxHora:
            self.valActSeg = self.valActSeg + 1        
            self.reiniciaCont()
            reloj1.mostrarContador()

    def reiniciaCont (self):
        if self.valActSeg > self.maxMinSeg:
            self.valActSeg = self.minVal
            self.valActMin = self.valActMin + 1
        if self.valActMin > self.maxMinSeg:
            self.valActMin = self.minVal
            self.valActHora = self.valActHora + 1
        if self.valActHora > self.maxHora:
            self.valActHora = self.minVal
            self.valActSeg = self.minVal

    def mostrarContador(self):
        clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.valActHora}:{self.valActMin}:{self.valActSeg}")
        time.sleep(1)
        clear()


reloj1 = ej3_Reloj_Digital()
reloj1.incrementar()