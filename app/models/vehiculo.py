import re
from app.models.servicio import Servicio

class Vehiculo:
    def __init__(self, placa, marca, kilometraje_actual, tipo):
        self.tipo = tipo.strip().capitalize()
        self.placa = self._validar_placa(placa, self.tipo)
        self.marca = marca
        self.kilometraje_actual = int(kilometraje_actual)
        self.historial_servicios = []

    def _validar_placa(self, placa, tipo):
        p = placa.upper().strip()
        patron = r"^[A-Z]{3}\d{3}$" if tipo == "Auto" else r"^[A-Z]{3}\d{2}[A-Z]$"
        if not re.match(patron, p):
            raise ValueError(f"Formato de placa inválido para {tipo}.")
        return p

    def agregar_servicio(self, servicio):
        self.historial_servicios.append(servicio)
        if servicio.kilometraje_servicio > self.kilometraje_actual:
            self.kilometraje_actual = servicio.kilometraje_servicio

    def to_dict(self):
        return {
            "placa": self.placa, "marca": self.marca, "tipo": self.tipo,
            "kilometraje_actual": self.kilometraje_actual,
            "historial_servicios": [{"fecha": s.fecha, "descripcion": s.descripcion, "costo": s.costo, "kilometraje_servicio": s.kilometraje_servicio} for s in self.historial_servicios]
        }