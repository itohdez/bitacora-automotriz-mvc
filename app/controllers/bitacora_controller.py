from app.models.gestor import GestorBitacora
from app.models.vehiculo import Vehiculo
from app.models.servicio import Servicio
from app.views.consola_view import ConsolaView

class BitacoraController:
    """Controlador que orquesta la comunicación entre la Vista y el Modelo."""

    def __init__(self):
        self.gestor = GestorBitacora()
        self.vista = ConsolaView()

    def iniciar(self):
        self.vista.mostrar_bienvenida()
        while True:
            opcion = self.vista.mostrar_menu_principal()
            if opcion == "1":
                self.registrar_nuevo_vehiculo()
            elif opcion == "2":
                self.registrar_servicio()
            elif opcion == "3":
                self.consultar_vehiculo()
            elif opcion == "4":
                self.vista.mostrar_mensaje("¡Gracias por usar el Sistema de Bitácora Automotriz!")
                break

    def registrar_nuevo_vehiculo(self):
        datos = self.vista.pedir_datos_vehiculo()
        try:
            kilometraje_int = int(datos["kilometraje"])
            nuevo_vehiculo = Vehiculo(datos["placa"], datos["marca"], kilometraje_int, datos["tipo"])
            
            self.gestor.registrar_vehiculo(nuevo_vehiculo)
            self.vista.mostrar_mensaje(f"{nuevo_vehiculo.tipo} '{datos['placa']}' registrado correctamente.")
            
        except ValueError as error_modelo:
            # Si se captura un ValueError (ej. placa repetida), se lo pasamos a la vista
            self.vista.mostrar_mensaje(str(error_modelo), exito=False)

    def consultar_vehiculo(self):
        placa = self.vista.pedir_placa()
        try:
            vehiculo = self.gestor.buscar_vehiculo(placa)
            gastos = vehiculo.obtener_total_gastado()
            self.vista.mostrar_mensaje(
                f"{vehiculo.tipo} {vehiculo.marca} ({vehiculo.placa}) encontrado. Gastos totales: ${gastos}"
            )
        except KeyError as error_modelo:
            self.vista.mostrar_mensaje(str(error_modelo), exito=False)

    def registrar_servicio(self):
        """Busca un vehículo, pide los datos del servicio y se los asigna."""
        placa = self.vista.pedir_placa()
        
        try:
            # 1. Buscamos si el vehículo existe antes de pedir más datos
            vehiculo = self.gestor.buscar_vehiculo(placa)
            
            # 2. Si llegamos aquí es porque no hubo error. Pedimos los datos a la Vista
            datos = self.vista.pedir_datos_servicio()
            
            # 3. Transformamos textos a números (Puede generar ValueError si escriben letras)
            costo_float = float(datos["costo"])
            km_int = int(datos["kilometraje"])
            
            # 4. Creamos el objeto (Puede generar ValueError si envían números negativos)
            nuevo_servicio = Servicio(datos["fecha"], datos["descripcion"], costo_float, km_int)
            
            # 5. Delegamos al vehículo la tarea de guardar su propio servicio
            vehiculo.agregar_servicio(nuevo_servicio)
            
            self.vista.mostrar_mensaje(f"Mantenimiento agregado exitosamente al {vehiculo.tipo} {vehiculo.placa}.")
            
        except KeyError as error_busqueda:
            # Atrapa el error si la placa no existe en el sistema
            self.vista.mostrar_mensaje(str(error_busqueda), exito=False)
        except ValueError as error_datos:
            # Atrapa los errores matemáticos (costo negativo o intentar convertir letras a números)
            self.vista.mostrar_mensaje(f"Error en los datos ingresados: {error_datos}", exito=False)