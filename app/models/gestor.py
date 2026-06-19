from app.models.vehiculo import Vehiculo

class GestorBitacora:
    """Clase de alto nivel encargada de administrar toda la colección de vehículos."""

    def __init__(self):
        self.vehiculos = []

    def registrar_vehiculo(self, vehiculo: Vehiculo):
        # Evitamos la duplicidad de información
        for v in self.vehiculos:
            if v.placa == vehiculo.placa:
                raise ValueError(f"El vehículo con la placa {vehiculo.placa} ya está registrado.")
        self.vehiculos.append(vehiculo)

    def buscar_vehiculo(self, placa: str) -> Vehiculo:
        placa_buscar = placa.upper().strip()
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa_buscar:
                return vehiculo
        raise KeyError(f"No se encontró ningún vehículo con la placa {placa_buscar}.")

    def obtener_reporte_gastos_totales(self, placa: str) -> float:
        # Reutilización de código: llamamos a un método propio
        vehiculo = self.buscar_vehiculo(placa)
        return vehiculo.obtener_total_gastado()