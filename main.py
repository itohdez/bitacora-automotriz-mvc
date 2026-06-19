from app.controllers.bitacora_controller import BitacoraController

if __name__ == "__main__":
    # Cambia a "consola" si quieres volver a la terminal
    aplicacion = BitacoraController(modo="grafico") 
    aplicacion.vista.iniciar()