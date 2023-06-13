class Mision():
    def __init__(self, planeta, captura, recompensa):
        self.planeta = planeta
        self.captura = captura
        self.recompensa = recompensa
    
    def __str__(self):
        return f"{self.planeta} - {self.captura} - {self.recompensa}"