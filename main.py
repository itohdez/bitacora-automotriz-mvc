from app.controllers.bitacora_controller import BitacoraController
from app.views.grafica_view import GraficaView

if __name__ == "__main__":
    # 1. Instanciamos la vista primero
    vista = GraficaView()
    
    # 2. Pasamos la vista al controlador para que él la gestione
    aplicacion = BitacoraController(vista)
    
    # 3. Iniciamos el ciclo de vida de la aplicación
    vista.iniciar()