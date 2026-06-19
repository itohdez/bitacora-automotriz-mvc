import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

# Configuración estética
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class GraficaView:
    """Interfaz gráfica moderna utilizando CustomTkinter con layouts corregidos."""

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Bitácora Automotriz MVC")
        self.root.geometry("400x550")
        
        self.label = ctk.CTkLabel(self.root, text="Bitácora Automotriz", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)
        
        # Botones principales
        self.btn_registrar = ctk.CTkButton(self.root, text="Registrar Vehículo", width=200)
        self.btn_registrar.pack(pady=10)
        self.btn_servicio = ctk.CTkButton(self.root, text="Registrar Mantenimiento", width=200)
        self.btn_servicio.pack(pady=10)
        self.btn_consultar = ctk.CTkButton(self.root, text="Consultar Historial", width=200)
        self.btn_consultar.pack(pady=10)
        self.btn_eliminar = ctk.CTkButton(self.root, text="Eliminar Vehículo", width=200, fg_color="#FF4C4C")
        self.btn_eliminar.pack(pady=10)
        self.btn_exportar = ctk.CTkButton(self.root, text="Exportar a CSV", width=200, fg_color="#2ECC71") 
        self.btn_exportar.pack(pady=10)
        self.btn_salir = ctk.CTkButton(self.root, text="Salir", width=200, command=self.root.destroy, fg_color="#7F8C8D")
        self.btn_salir.pack(pady=20)
        
    def iniciar(self):
        self.root.mainloop()

    def _abrir_calendario(self, entry_widget):
        top = tk.Toplevel(self.root)
        top.title("Seleccionar Fecha")
        cal = DateEntry(top, date_pattern='dd/mm/yyyy')
        cal.pack(pady=20)
        
        def aplicar():
            entry_widget.delete(0, 'end')
            entry_widget.insert(0, cal.get())
            top.destroy()
        tk.Button(top, text="Confirmar", command=aplicar).pack(pady=10)

    def _crear_ventana_input(self, titulo, campos, callback):
        top = ctk.CTkToplevel(self.root)
        top.title(titulo)
        top.geometry("350x450")
        top.attributes("-topmost", True)
        
        entries = {}
        # Título del formulario
        ctk.CTkLabel(top, text=titulo, font=("Arial", 16, "bold")).pack(pady=15)
        
        for campo in campos:
            # FRAME PRINCIPAL PARA CADA CAMPO (Ordena Etiqueta + Input)
            frame = ctk.CTkFrame(top, fg_color="transparent")
            frame.pack(fill="x", padx=20, pady=5)
            
            # Etiqueta fija a la izquierda
            ctk.CTkLabel(frame, text=campo, width=80, anchor="w").pack(side="left")
            
            # Input a la derecha
            if campo == "Fecha":
                e = ctk.CTkEntry(frame, width=120)
                e.pack(side="left", padx=5)
                ctk.CTkButton(frame, text="📅", width=30, command=lambda e=e: self._abrir_calendario(e)).pack(side="left")
            elif campo == "Tipo":
                e = ctk.CTkOptionMenu(frame, values=["Auto", "Moto"], width=150)
                e.pack(side="left", padx=5)
            else:
                e = ctk.CTkEntry(frame, width=150)
                e.pack(side="left", padx=5)
            
            entries[campo.lower()] = e
        
        def enviar():
            callback({k: v.get() for k, v in entries.items()})
            top.destroy()
            
        ctk.CTkButton(top, text="Confirmar", command=enviar).pack(pady=30)

    # Métodos de interfaz
    def abrir_formulario_registro(self, callback): self._crear_ventana_input("Nuevo Vehículo", ["Tipo", "Placa", "Marca", "Kilometraje"], callback)
    def abrir_formulario_servicio(self, callback): self._crear_ventana_input("Nuevo Servicio", ["Placa", "Fecha", "Descripción", "Costo", "Kilometraje"], callback)
    def abrir_formulario_consulta(self, callback): self._crear_ventana_input("Consultar Historial", ["Placa"], callback)
    def configurar_callback_eliminar(self, callback): self.btn_eliminar.configure(command=callback)
    def mostrar_mensaje(self, msg, exito=True): messagebox.showinfo("Info" if exito else "Error", msg)
    def solicitar_eliminacion_con_lista(self, placas, callback):
        top = ctk.CTkToplevel(self.root)
        top.geometry("300x200")
        var = ctk.StringVar(value=placas[0])
        ctk.CTkOptionMenu(top, variable=var, values=placas).pack(pady=20)
        ctk.CTkButton(top, text="Eliminar", fg_color="red", command=lambda: [callback({"placa": var.get()}), top.destroy()]).pack()