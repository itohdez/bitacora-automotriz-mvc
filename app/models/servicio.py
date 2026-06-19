class Servicio:
    def __init__(self, fecha, descripcion, costo, kilometraje_servicio):
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = float(costo)
        self.kilometraje_servicio = int(kilometraje_servicio)
        if self.costo < 0 or self.kilometraje_servicio < 0:
            raise ValueError("El costo y kilometraje deben ser positivos.")

    def __str__(self):
        return f"{self.fecha} - {self.descripcion} | Costo: ${self.costo} | Km: {self.kilometraje_servicio}"