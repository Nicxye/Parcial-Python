class Superheroe():
    def __init__(self, nombre_s, nombre_p, anio, grupo):
        self.nombre_s = nombre_s
        self.nombre_p = nombre_p
        self.anio = anio
        self.grupo = grupo
    
    def __str__(self):
        return f"{self.nombre_s} - {self.nombre_p} - {self.anio} - {self.grupo}"