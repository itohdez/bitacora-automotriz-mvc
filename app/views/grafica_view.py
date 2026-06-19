import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class GraficaView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bitácora Automotriz MVC")
        self.root.geometry("400x350")
        
        tk.Label(self.root, text="Bitácora Automotriz", font=("Arial", 16, "bold")).pack(pady=15)
        
        self.btn_registrar = tk.Button(self.root, text="Registrar Vehículo", width=25)
        self.btn_registrar.pack(pady=5)
        
        self.btn_servicio = tk.Button(self.root, text="Registrar Mantenimiento", width=25)
        self.btn_servicio.pack(pady=5)
        
        self.btn_consultar = tk.Button(self.root, text="Consultar Historial", width=25)
        self.btn_consultar.pack(pady=5)
        
    def iniciar(self):
        self.root.mainloop()

    def abrir_formulario_registro(self, callback):
        # Aseguramos que "Tipo" esté en la lista
        self._crear_ventana_input("Nuevo Vehículo", ["Tipo", "Placa", "Marca", "Kilometraje"], callback)

    def abrir_formulario_servicio(self, callback):
        self._crear_ventana_input("Nuevo Servicio", ["Placa", "Fecha", "Descripción", "Costo", "Kilometraje"], callback)

    def abrir_formulario_consulta(self, callback):
        self._crear_ventana_input("Consultar Historial", ["Placa"], callback)

    def _crear_ventana_input(self, titulo, campos, callback):
        top = tk.Toplevel(self.root)
        top.title(titulo)
        entries = {}
        
        for campo in campos:
            tk.Label(top, text=campo).pack()
            
            # Lógica inteligente para seleccionar el widget adecuado
            if campo == "Fecha":
                e = DateEntry(top, date_pattern='dd/mm/yyyy')
            elif campo == "Tipo":
                e = tk.StringVar(value="Auto")
                tk.OptionMenu(top, e, "Auto", "Moto").pack()
            else:
                e = tk.Entry(top)
            
            # Solo hacemos .pack() si no es el OptionMenu (que ya se empaqueta arriba)
            if not isinstance(e, tk.StringVar):
                e.pack()
                
            entries[campo.lower()] = e
        
        def enviar():
            # Extraemos el valor correctamente, sea Entry o StringVar
            datos = {k: v.get() if isinstance(v, (tk.Entry, tk.StringVar)) else v.get() for k, v in entries.items()}
            callback(datos)
            top.destroy()
            
        tk.Button(top, text="Confirmar", command=enviar).pack(pady=10)

    def mostrar_mensaje(self, mensaje: str, exito: bool = True):
        messagebox.showinfo("Info" if exito else "Error", mensaje)