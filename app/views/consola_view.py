from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

class ConsolaView:
    """Clase encargada exclusivamente de la interfaz de usuario."""

    def __init__(self):
        self.console = Console()

    def mostrar_bienvenida(self):
        titulo = "[bold cyan]🚗 Sistema de Bitácora Automotriz🏍️[/bold cyan]\n[italic]Gestión de mantenimientos y gastos[/italic]"
        self.console.print(Panel(titulo, expand=False, border_style="cyan"))

    def mostrar_menu_principal(self) -> str:
        self.console.print("\n[bold yellow]--- Menú Principal ---[/bold yellow]")
        self.console.print("1. Registrar nuevo vehículo")
        self.console.print("2. Registrar servicio de mantenimiento")
        self.console.print("3. Consultar historial de un vehículo")
        self.console.print("4. Salir del sistema")
        
        opcion = Prompt.ask("\nSelecciona una opción", choices=["1", "2", "3", "4"])
        return opcion

    def mostrar_mensaje(self, mensaje: str, exito: bool = True):
        if exito:
            self.console.print(f"[bold green]✔ Éxito:[/bold green] {mensaje}")
        else:
            self.console.print(f"[bold red]✖ Error:[/bold red] {mensaje}")

    def pedir_datos_vehiculo(self) -> dict:
        self.console.print("\n[bold magenta]--- Ingresar Datos del Vehículo ---[/bold magenta]")
        tipo = Prompt.ask("Selecciona el tipo de vehículo", choices=["Auto", "Moto"])
        placa = Prompt.ask("Ingresa la placa")
        marca = Prompt.ask("Ingresa la marca")
        kilometraje = Prompt.ask("Ingresa el kilometraje actual (solo números)")
        
        # Entregamos los datos empaquetados, listos para que el controlador los use
        return {
            "tipo": tipo,
            "placa": placa,
            "marca": marca,
            "kilometraje": kilometraje
        }

    def pedir_placa(self) -> str:
        return Prompt.ask("\nIngresa la placa del vehículo a buscar")
    
    def pedir_datos_servicio(self) -> dict:
        """Solicita los datos de un mantenimiento y los retorna en un diccionario."""
        self.console.print("\n[bold cyan]--- Ingresar Datos del Mantenimiento ---[/bold cyan]")
        fecha = Prompt.ask("Ingresa la fecha (ej. 2023-10-25)")
        descripcion = Prompt.ask("Ingresa la descripción (ej. Cambio de aceite)")
        costo = Prompt.ask("Ingresa el costo (solo números)")
        kilometraje = Prompt.ask("Ingresa el kilometraje al momento del servicio")
        
        return {
            "fecha": fecha,
            "descripcion": descripcion,
            "costo": costo,
            "kilometraje": kilometraje
        }   