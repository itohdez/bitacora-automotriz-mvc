import json
import os
from app.models.vehiculo import Vehiculo

class GestorBitacora:
    def __init__(self, archivo="bitacora.json"):
        self.archivo = archivo
        self.vehiculos = {}
        self.cargar_datos()

    def registrar_vehiculo(self, vehiculo):
        self.vehiculos[vehiculo.placa] = vehiculo
        self.guardar_datos()

    def eliminar_vehiculo(self, placa):
        if placa in self.vehiculos:
            del self.vehiculos[placa]
            self.guardar_datos()
            return True
        return False

    def buscar_vehiculo(self, placa):
        if placa not in self.vehiculos:
            raise KeyError(f"No se encontró ningún vehículo con la placa {placa}.")
        return self.vehiculos[placa]

    def guardar_datos(self):
        datos = {p: v.to_dict() for p, v in self.vehiculos.items()}
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                for placa, v_dict in datos.items():
                    v = Vehiculo(v_dict["placa"], v_dict["marca"], v_dict["kilometraje_actual"], v_dict["tipo"])
                    # Aquí deberías cargar también los servicios si los guardaste
                    self.vehiculos[placa] = v