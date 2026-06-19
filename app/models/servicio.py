class Servicio:
    """Clase que representa un mantenimiento realizado a un vehículo."""

    def __init__(self, fecha: str, descripcion: str, costo: float, kilometraje_servicio: int):
        # Protegemos el estado del objeto bloqueando valores matemáticamente imposibles
        if costo < 0:
            raise ValueError("El costo del servicio no puede ser negativo.")
        if kilometraje_servicio < 0:
            raise ValueError("El kilometraje no puede ser negativo.")

        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        self.kilometraje_servicio = kilometraje_servicio

    def __str__(self):
        return f"{self.fecha} - {self.descripcion} | Costo: ${self.costo} | Km: {self.kilometraje_servicio}"