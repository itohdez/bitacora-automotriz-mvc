from app.models.gestor import GestorBitacora
from app.models.vehiculo import Vehiculo
from app.models.servicio import Servicio
from app.views.grafica_view import GraficaView

class BitacoraController:
    def __init__(self):
        self.gestor = GestorBitacora()
        self.vista = GraficaView()
        
        self.vista.btn_registrar.config(command=lambda: self.vista.abrir_formulario_registro(self.registrar_vehiculo))
        self.vista.btn_servicio.config(command=lambda: self.vista.abrir_formulario_servicio(self.registrar_servicio))
        self.vista.btn_consultar.config(command=lambda: self.vista.abrir_formulario_consulta(self.consultar_historial))
        
        self.vista.configurar_callback_eliminar(self.abrir_selector_eliminacion)

    def abrir_selector_eliminacion(self):
        placas = list(self.gestor.vehiculos.keys())
        if not placas:
            self.vista.mostrar_mensaje("No hay vehículos registrados para eliminar.", False)
        else:
            self.vista.solicitar_eliminacion_con_lista(placas, self.eliminar_vehiculo)

    def eliminar_vehiculo(self, datos):
        try:
            if self.gestor.eliminar_vehiculo(datos["placa"]):
                self.vista.mostrar_mensaje(f"Vehículo {datos['placa']} eliminado.")
            else:
                self.vista.mostrar_mensaje("Error al eliminar.", False)
        except Exception as e:
            self.vista.mostrar_mensaje(str(e), False)

    def registrar_vehiculo(self, datos):
        try:
            v = Vehiculo(datos["placa"], datos["marca"], int(datos["kilometraje"]), datos["tipo"])
            self.gestor.registrar_vehiculo(v)
            self.vista.mostrar_mensaje("Vehículo registrado.")
        except Exception as e: self.vista.mostrar_mensaje(str(e), False)

    def registrar_servicio(self, datos):
        try:
            v = self.gestor.buscar_vehiculo(datos["placa"])
            s = Servicio(datos["fecha"], datos["descripción"], float(datos["costo"]), int(datos["kilometraje"]))
            v.agregar_servicio(s)
            self.gestor.guardar_datos()
            self.vista.mostrar_mensaje("Servicio agregado.")
        except Exception as e: self.vista.mostrar_mensaje(str(e), False)

    def consultar_historial(self, datos):
        try:
            v = self.gestor.buscar_vehiculo(datos["placa"])
            res = "\n".join([f"{s.fecha} - {s.descripcion} (${s.costo})" for s in v.historial_servicios])
            self.vista.mostrar_mensaje(res if res else "Sin servicios.")
        except Exception as e: self.vista.mostrar_mensaje(str(e), False)