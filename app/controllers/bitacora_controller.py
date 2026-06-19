from app.models.gestor import GestorBitacora
from app.models.vehiculo import Vehiculo
from app.models.servicio import Servicio
from app.views.grafica_view import GraficaView

class BitacoraController:
    def __init__(self, modo="grafico"):
        self.gestor = GestorBitacora()
        self.vista = GraficaView()
        
        # Conexión de botones
        self.vista.btn_registrar.config(command=lambda: self.vista.abrir_formulario_registro(self.registrar_vehiculo))
        self.vista.btn_servicio.config(command=lambda: self.vista.abrir_formulario_servicio(self.registrar_servicio))
        self.vista.btn_consultar.config(command=lambda: self.vista.abrir_formulario_consulta(self.consultar_historial))

    def registrar_vehiculo(self, datos):
        try:
            v = Vehiculo(datos["placa"], datos["marca"], int(datos["kilometraje"]), "Auto")
            self.gestor.registrar_vehiculo(v)
            self.vista.mostrar_mensaje("Vehículo registrado correctamente.")
        except Exception as e: 
            self.vista.mostrar_mensaje(str(e), False)

    def registrar_servicio(self, datos):
        try:
            v = self.gestor.buscar_vehiculo(datos["placa"])
            if v:
                s = Servicio(datos["fecha"], datos["descripción"], float(datos["costo"]), int(datos["kilometraje"]))
                v.agregar_servicio(s)
                self.vista.mostrar_mensaje("Servicio agregado con éxito.")
            else: 
                self.vista.mostrar_mensaje("Vehículo no encontrado.", False)
        except Exception as e: 
            self.vista.mostrar_mensaje(str(e), False)

    def consultar_historial(self, datos):
        v = self.gestor.buscar_vehiculo(datos["placa"])
        if v:
            res = "Historial de servicios:\n"
            for s in v.historial_servicios:
                res += f"📅 {s.fecha} | 🔧 {s.descripcion} | 💰 ${s.costo:,.0f} | 🛣️ {s.kilometraje_servicio}km\n"
            self.vista.mostrar_mensaje(res if v.historial_servicios else "No hay servicios registrados.")
        else: 
            self.vista.mostrar_mensaje("Vehículo no encontrado.", False)