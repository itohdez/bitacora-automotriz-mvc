# 🚗 Sistema de Bitácora Automotriz 🏍️

Este proyecto es una aplicación de consola interactiva desarrollada en Python que permite a los usuarios (particulares o talleres mecánicos) llevar un registro detallado y organizado de los mantenimientos, gastos y el historial de servicios de sus vehículos (Autos y Motos).

## 🏗️ Arquitectura y Patrones de Diseño

El sistema fue construido aplicando principios de **Programación Orientada a Objetos (POO)** y el patrón arquitectónico **MVC (Modelo-Vista-Controlador)** para garantizar un código limpio, escalable y mantenible.

### Aplicación de POO
* **Encapsulamiento:** Las clases `Vehiculo` y `Servicio` protegen sus datos. Por ejemplo, el cálculo del total gastado se realiza dentro de la propia clase `Vehiculo`, evitando que factores externos manipulen las matemáticas.
* **Validación de Estado:** Los constructores aplican reglas de negocio estrictas (ej. no se permiten kilometrajes negativos ni tipos de vehículos no válidos), lanzando excepciones (`ValueError`) para proteger la integridad de los datos.
* **Composición:** Un `Vehiculo` contiene una lista de objetos `Servicio`, reflejando una relación del mundo real.

### Aplicación de MVC
* **Modelo (`app/models/`):** Contiene la lógica pura (`Vehiculo`, `Servicio`, `GestorBitacora`). No tiene interacción con el usuario (sin `prints` ni `inputs`).
* **Vista (`app/views/`):** Construida con la librería externa `rich`, se encarga exclusivamente de mostrar menús coloridos y capturar la información del teclado. Es "ciega" a las reglas de negocio.
* **Controlador (`app/controllers/`):** Orquesta la aplicación. Recibe los datos capturados por la Vista, los envía al Modelo para su validación/almacenamiento, y captura los errores del Modelo para pedirle a la Vista que muestre las alertas correspondientes.

## 📊 Diagrama de Clases

```mermaid
classDiagram
    class Servicio {
        -str fecha
        -str descripcion
        -float costo
        -int kilometraje_servicio
    }
    
    class Vehiculo {
        -str placa
        -str marca
        -int kilometraje_actual
        -str tipo
        -list historial_servicios
        +agregar_servicio(servicio) void
        +obtener_total_gastado() float
    }
    
    class GestorBitacora {
        -list vehiculos
        +registrar_vehiculo(vehiculo) void
        +buscar_vehiculo(placa) Vehiculo
        +obtener_reporte_gastos_totales(placa) float
    }
    
    GestorBitacora "1" --> "*" Vehiculo : Administra
    Vehiculo "1" --> "*" Servicio : Contiene