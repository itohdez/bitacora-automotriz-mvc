from app.models.gestor import GestorBitacora
from app.models.vehiculo import Vehiculo
from app.models.servicio import Servicio

class BitacoraController:
    def __init__(self, vista):
        self.gestor = GestorBitacora()
        self.vista = vista
        self.vista.btn_registrar.configure(command=lambda: self.vista.abrir_formulario_registro(self.registrar_vehiculo))
        self.vista.btn_servicio.configure(command=lambda: self.vista.abrir_formulario_servicio(self.registrar_servicio))
        self.vista.btn_consultar.configure(command=lambda: self.vista.abrir_formulario_consulta(self.consultar_historial))
        self.vista.btn_exportar.configure(command=lambda: [self.gestor.exportar_a_csv(), self.vista.mostrar_mensaje("CSV Generado")])
        self.vista.configurar_callback_eliminar(self.abrir_selector_eliminacion)

    def registrar_vehiculo(self, d):
        try:
            self.gestor.registrar_vehiculo(Vehiculo(d["placa"], d["marca"], d["kilometraje"], d["tipo"]))
            self.vista.mostrar_mensaje("Vehículo registrado.")
        except Exception as e: self.vista.mostrar_mensaje(str(e), False)

    def registrar_servicio(self, d):
        try:
            v = self.gestor.buscar_vehiculo(d["placa"])
            if not v: raise ValueError("Vehículo no encontrado.")
            v.agregar_servicio(Servicio(d["fecha"], d["descripción"], d["costo"], d["kilometraje"]))
            self.gestor.guardar_datos()
            self.vista.mostrar_mensaje("Servicio agregado.")
        except Exception as e: self.vista.mostrar_mensaje(str(e), False)

    def consultar_historial(self, d):
        v = self.gestor.buscar_vehiculo(d["placa"])
        if not v: self.vista.mostrar_mensaje("No encontrado.", False)
        else: self.vista.mostrar_mensaje("\n".join([str(s) for s in v.historial_servicios]) or "Sin servicios.")

    def abrir_selector_eliminacion(self): self.vista.solicitar_eliminacion_con_lista(list(self.gestor.vehiculos.keys()), self.eliminar_vehiculo)
    def eliminar_vehiculo(self, d):
        if self.gestor.eliminar_vehiculo(d["placa"]): self.vista.mostrar_mensaje("Eliminado.")