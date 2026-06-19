import json, os, csv
from app.models.vehiculo import Vehiculo
from app.models.servicio import Servicio

class GestorBitacora:
    def __init__(self, archivo="bitacora.json"):
        self.archivo = archivo
        self.vehiculos = {}
        self.cargar_datos()

    def buscar_vehiculo(self, placa):
        return self.vehiculos.get(placa.upper().strip())

    def registrar_vehiculo(self, v):
        self.vehiculos[v.placa] = v
        self.guardar_datos()

    def eliminar_vehiculo(self, placa):
        p = placa.upper().strip()
        if p in self.vehiculos:
            del self.vehiculos[p]
            self.guardar_datos()
            return True
        return False

    def guardar_datos(self):
        with open(self.archivo, 'w') as f:
            json.dump({p: v.to_dict() for p, v in self.vehiculos.items()}, f, indent=4)

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                try:
                    datos = json.load(f)
                    for p, v_d in datos.items():
                        v = Vehiculo(v_d["placa"], v_d["marca"], v_d["kilometraje_actual"], v_d["tipo"])
                        for s in v_d.get("historial_servicios", []):
                            v.agregar_servicio(Servicio(s["fecha"], s["descripcion"], s["costo"], s["kilometraje_servicio"]))
                        self.vehiculos[p] = v
                except: self.vehiculos = {}

    def exportar_a_csv(self, nombre="reporte_vehiculos.csv"):
        with open(nombre, 'w', newline='', encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerow(["Placa", "Marca", "Tipo", "Km", "Fecha", "Desc", "Costo"])
            for v in self.vehiculos.values():
                for s in v.historial_servicios:
                    w.writerow([v.placa, v.marca, v.tipo, v.kilometraje_actual, s.fecha, s.descripcion, s.costo])