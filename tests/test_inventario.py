#el rchivo contiene el conjunto de pruebas unitarias escritas usando pytest
# que "estresan" el codigo anterior en diferentes condiciones logicas para garantizar que todo funcione bien

"""Pruebas del calculo de inventario"""

import pytest #  Importamos las funciones limpiamente desde src/inventario
from src.inventario import dias_de_inventario, necesita_reposicion

# 1 escenario todo con normalidad
def test_dias_normales():  # 100 unidades de stock vendiendo 10 por dia deben dar exactamente 10 dias.
    assert dias_de_inventario(100, 10) == 10  # Usamos assert (afirmar) para verificar la igualdad exacta.

# dia de sin ventas evitar division porm cero
def test_sin_ventas_dura_infinito():
    assert dias_de_inventario(50, 0) == -1.0  # 50 unidades vendiendo 0 al dia debe dar la señal de infinito: -1.0

# Comprobacion de  repocision de stock
def test_necesita_reposicion_true(): # 20 unidades de stock vendiendo 10 al dia nos da 2 dias restantes.
    assert necesita_reposicion(20, 10) is True  # Como 2 dias es menor que el umbral de 7 dias, debe arrojar "True". es decir que necesitamos inventario

# Comprobacion de casos sin alerta
def test_no_necesita_reposicion(): # 100 unidades vendiendo 10 al dia nos da 10 dias restantes.
    assert necesita_reposicion(100, 10) is False  # Como 10 dias es mayor que el umbral de 7 dias, la tienda esta abastecida (False).

# Validacion de datos corruptos 
def test_stock_negativo_lanza_error():
    with pytest.raises(ValueError): # Verificamos que si se ingresa un stock negativo (-5), el sistema de verdad
        dias_de_inventario(-5, 10)   # lance de forma ruidosa un "ValueError" y detenga la ejecucion.

        
        