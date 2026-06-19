from app.models.gestor import GestorBitacora
from app.models.vehiculo import Vehiculo
from app.models.servicio import Servicio
from app.views.grafica_view import GraficaView

class BitacoraController:
    def __init__(self):
        self.gestor = GestorBitacora()
        self.vista = GraficaView()
        
        # Conexión de botones
        self.vista.btn_registrar.config(command=lambda: self.vista.abrir_formulario_registro(self.registrar_vehiculo))
        self.vista.btn_servicio.config(command=lambda: self.vista.abrir_formulario_servicio(self.registrar_servicio))
        self.vista.btn_consultar.config(command=lambda: self.vista.abrir_formulario_consulta(self.consultar_historial))
        self.vista.configurar_callback_eliminar(self.eliminar_vehiculo)

    def registrar_vehiculo(self, datos):
        try:
            v = Vehiculo(datos["placa"], datos["marca"], int(datos["kilometraje"]), datos["tipo"])
            self.gestor.registrar_vehiculo(v)
            self.vista.mostrar_mensaje("Vehículo registrado correctamente.")
        except Exception as e: 
            self.vista.mostrar_mensaje(str(e), False)

    def registrar_servicio(self, datos):
        try:
            v = self.gestor.buscar_vehiculo(datos["placa"])
            s = Servicio(datos["fecha"], datos["descripción"], float(datos["costo"]), int(datos["kilometraje"]))
            v.agregar_servicio(s)
            self.gestor.guardar_datos() # Guardamos tras agregar el servicio
            self.vista.mostrar_mensaje("Servicio agregado con éxito.")
        except Exception as e: 
            self.vista.mostrar_mensaje(str(e), False)

    def consultar_historial(self, datos):
        try:
            v = self.gestor.buscar_vehiculo(datos["placa"])
            res = "Historial de servicios:\n"
            if not v.historial_servicios:
                res = "No hay servicios registrados."
            else:
                for s in v.historial_servicios:
                    res += f"📅 {s.fecha} | 🔧 {s.descripcion} | 💰 ${float(s.costo):,.0f} | 🛣️ {s.kilometraje_servicio}km\n"
            self.vista.mostrar_mensaje(res)
        except Exception as e: 
            self.vista.mostrar_mensaje(str(e), False)

    def eliminar_vehiculo(self, datos):
        try:
            if self.gestor.eliminar_vehiculo(datos["placa"]):
                self.vista.mostrar_mensaje(f"Vehículo {datos['placa']} eliminado con éxito.")
            else:
                self.vista.mostrar_mensaje("Placa no encontrada.", False)
        except Exception as e:
            self.vista.mostrar_mensaje(str(e), False)