import pytest
from app.models.servicio import Servicio
from app.models.vehiculo import Vehiculo
from app.models.gestor import GestorBitacora

def test_vehiculo_calcula_total_gastado():
    mi_auto = Vehiculo("ABC-123", "Toyota", 50000, "Auto")
    servicio_1 = Servicio("2023-10-01", "Cambio de aceite", 150.0, 50100)
    servicio_2 = Servicio("2023-11-15", "Cambio de frenos", 300.0, 52000)
    
    mi_auto.agregar_servicio(servicio_1)
    mi_auto.agregar_servicio(servicio_2)
    total = mi_auto.obtener_total_gastado()
    
    assert total == 450.0
    assert mi_auto.kilometraje_actual == 52000

def test_gestor_busca_vehiculo_correctamente():
    gestor = GestorBitacora()
    moto = Vehiculo("XYZ-987", "Yamaha", 10000, "Moto")
    gestor.registrar_vehiculo(moto)
    
    vehiculo_encontrado = gestor.buscar_vehiculo("xyz-987") 
    
    assert vehiculo_encontrado.marca == "Yamaha"
    assert vehiculo_encontrado.placa == "XYZ-987"
    assert vehiculo_encontrado.tipo == "Moto"

def test_crear_servicio_costo_negativo_lanza_error():
    with pytest.raises(ValueError) as informacion_error:
        servicio_invalido = Servicio("2023-10-01", "Lavado", -50.0, 100)
    
    assert "El costo del servicio no puede ser negativo" in str(informacion_error.value)