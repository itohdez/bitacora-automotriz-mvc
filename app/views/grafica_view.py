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
        
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Vehículo", width=25)
        self.btn_eliminar.pack(pady=5)
        
    def iniciar(self):
        """Este es el método que faltaba para arrancar el bucle principal de la GUI."""
        self.root.mainloop()

    def abrir_formulario_registro(self, callback):
        self._crear_ventana_input("Nuevo Vehículo", ["Tipo", "Placa", "Marca", "Kilometraje"], callback)

    def abrir_formulario_servicio(self, callback):
        self._crear_ventana_input("Nuevo Servicio", ["Placa", "Fecha", "Descripción", "Costo", "Kilometraje"], callback)

    def abrir_formulario_consulta(self, callback):
        self._crear_ventana_input("Consultar Historial", ["Placa"], callback)

    def configurar_callback_eliminar(self, callback):
        self.callback_eliminar = callback
        self.btn_eliminar.config(command=self.solicitar_eliminacion)

    def solicitar_eliminacion(self):
        self._crear_ventana_input("Eliminar Vehículo", ["Placa"], self.callback_eliminar)

    def _crear_ventana_input(self, titulo, campos, callback):
        top = tk.Toplevel(self.root)
        top.title(titulo)
        top.geometry("300x400")
        entries = {}
        for campo in campos:
            tk.Label(top, text=campo, pady=5).pack()
            if campo == "Fecha": 
                e = DateEntry(top, width=20, date_pattern='dd/mm/yyyy')
            elif campo == "Tipo":
                e = tk.StringVar(value="Auto")
                tk.OptionMenu(top, e, "Auto", "Moto").pack()
            else: 
                e = tk.Entry(top, width=30)
            
            if not isinstance(e, tk.StringVar): 
                e.pack()
            entries[campo.lower()] = e
        
        def enviar():
            datos = {k: v.get() if isinstance(v, (tk.Entry, tk.StringVar)) else v.get() for k, v in entries.items()}
            callback(datos)
            top.destroy()
            
        tk.Button(top, text="Confirmar", command=enviar, width=20).pack(pady=20)

    def mostrar_mensaje(self, mensaje: str, exito: bool = True):
        messagebox.showinfo("Info" if exito else "Error", mensaje)