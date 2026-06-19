from app.models.servicio import Servicio

class Vehiculo:
    """Clase que representa un vehículo (Auto o Moto) y gestiona su historial."""

    def __init__(self, placa: str, marca: str, kilometraje_actual: int, tipo: str):
        if int(kilometraje_actual) < 0:
            raise ValueError("El kilometraje actual no puede ser negativo.")
        
        # Clasificamos el tipo de vehículo al nacer el objeto
        tipo_formateado = tipo.strip().capitalize()
        if tipo_formateado not in ["Auto", "Moto"]:
            raise ValueError("El tipo de vehículo debe ser 'Auto' o 'Moto'.")
            
        self.placa = placa.upper()
        self.marca = marca
        self.kilometraje_actual = int(kilometraje_actual)
        self.tipo = tipo_formateado
        self.historial_servicios = []  

    def agregar_servicio(self, servicio: Servicio):
        """Añade un nuevo servicio al historial y actualiza el kilometraje."""
        self.historial_servicios.append(servicio)
        if servicio.kilometraje_servicio > self.kilometraje_actual:
            self.kilometraje_actual = servicio.kilometraje_servicio

    def obtener_total_gastado(self) -> float:
        """Encapsulamiento: El vehículo sabe cómo sumar sus propios gastos."""
        return sum(servicio.costo for servicio in self.historial_servicios)

    def to_dict(self):
        """Convierte el objeto a un diccionario para poder guardarlo en JSON."""
        return {
            "placa": self.placa,
            "marca": self.marca,
            "kilometraje_actual": self.kilometraje_actual,
            "tipo": self.tipo,
            "historial_servicios": [
                {
                    "fecha": s.fecha,
                    "descripcion": s.descripcion,
                    "costo": s.costo,
                    "kilometraje_servicio": s.kilometraje_servicio
                } for s in self.historial_servicios
            ]
        }