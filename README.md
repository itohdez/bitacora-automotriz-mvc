# 🚗 Sistema de Bitácora Automotriz 🏍️

Este proyecto es una aplicación de escritorio desarrollada en Python que permite a los usuarios (particulares o talleres mecánicos) llevar un registro detallado y organizado de los mantenimientos, gastos y el historial de servicios de sus vehículos (Autos y Motos).

> Tecnologías: Python 3.x, CustomTkinter, JSON (persistencia), CSV (reportes).

## 🏗️ Arquitectura y Patrones de Diseño

El sistema fue construido aplicando principios de **Programación Orientada a Objetos (POO)** y el patrón arquitectónico **MVC (Modelo-Vista-Controlador)** para garantizar un código limpio, escalable y mantenible.

### Aplicación de POO
* **Encapsulamiento:** Las clases `Vehiculo` y `Servicio` protegen sus datos. Por ejemplo, el cálculo del total gastado se realiza dentro de la propia clase `Vehiculo`, evitando que factores externos manipulen las matemáticas.
* **Validación de Estado:** Los constructores aplican reglas de negocio estrictas (ej. no se permiten kilometrajes negativos ni tipos de vehículos no válidos), lanzando excepciones (`ValueError`) para proteger la integridad de los datos.
* **Composición:** Un `Vehiculo` contiene una lista de objetos `Servicio`, reflejando una relación del mundo real.

### Aplicación de MVC
* **Modelo (`app/models/`):** Contiene la lógica pura (`Vehiculo`, `Servicio`, `GestorBitacora`). No tiene interacción con el usuario (sin `prints` ni `inputs`).
* **Vista (`app/views/`):** Construida con CustomTkinter (basada en tkinter), lo que permite una interfaz de usuario moderna con soporte nativo para temas oscuros y componentes estilizados.
* **Controlador (`app/controllers/`):** Orquesta la aplicación. Recibe los datos capturados por la Vista, los envía al Modelo para su validación/almacenamiento, y captura los errores del Modelo para pedirle a la Vista que muestre las alertas correspondientes.

## 📋 Prerrequisitos

Para ejecutar, es necesario tener instalado el lenguaje de programación Python en tu equipo.

1. **Descarga de Python:**
   * Ve al sitio web oficial: [python.org/downloads](https://www.python.org/downloads/)
   * Descarga la última versión estable para tu sistema operativo (Windows, macOS o Linux).

2. **Instalación (Importante):**
   * **En Windows:** Durante la instalación, **asegúrate de marcar la casilla que dice "Add Python to PATH"**. Este paso es crítico, ya que permite que la terminal reconozca el comando `python`.

3. **Verificación:**
   Para confirmar que Python se instaló correctamente, abre una terminal y escribe:
   ```bash
   python --version

## ⚙️ Instalación y Ejecución

Para garantizar la portabilidad y el correcto funcionamiento del software en cualquier entorno, se han seguido estándares de desarrollo modular:

* **Compatibilidad:** El sistema es compatible con Windows, macOS y Linux (requiere Python 3.x).
* **Gestión de Dependencias:** El proyecto utiliza pip. Se incluye un archivo requirements.txt con las librerías necesarias.
* **Recomendación de Entorno (Best Practice):** Se recomienda ejecutar el proyecto dentro de un Entorno Virtual (venv) para aislar las dependencias.

### Pasos para ejecutar el proyecto en tu entorno local:

1. Clona este repositorio:
    git clone <https://github.com/itohdez/bitacora-automotriz-mvc.git>

2. Entra en la carpeta del proyecto:
    cd bitacora-automotriz-mvc

3. Instala las dependencias necesarias:
    python -m pip install -r requirements.txt

4. Ejecuta la aplicación:
    python main.py

## 🧪 Pruebas Automatizadas
* El proyecto utiliza pytest para garantizar la estabilidad del Modelo mediante el enfoque TDD (Test-Driven Development).
* Se incluyen pruebas válidas (creación y sumas) y pruebas inválidas (manejo de errores ante datos corruptos).

* Para correr los tests, ejecuta en la terminal:
pytest

## 📊 Diagrama de Clases

```mermaid
classDiagram
    class Servicio {
        +str fecha
        +str descripcion
        +float costo
        +int kilometraje_servicio
        +__str__() str
    }
    
    class Vehiculo {
        +str placa
        +str marca
        +int kilometraje_actual
        +str tipo
        +list historial_servicios
        +agregar_servicio(Servicio) void
        +obtener_resumen() str
        +to_dict() dict
    }
    
    class GestorBitacora {
        -dict vehiculos
        +registrar_vehiculo(Vehiculo) void
        +buscar_vehiculo(str placa) Vehiculo
        +eliminar_vehiculo(str placa) bool
        +guardar_datos() void
        +cargar_datos() void
        +exportar_a_csv(str nombre) void
    }
    
    GestorBitacora "1" --> "*" Vehiculo : Gestiona
    Vehiculo "1" --> "*" Servicio : Contiene