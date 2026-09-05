# Este archivo contiene las funciones matematicas que deciden canto
# inventario le queda a una sucursal y si necesita y si necesita abastecerse 
import sys
"""Calculo de reposicion de inventario para una cadena de tiendas."""

# 1. Calcular los dias de inventario
def dias_de_inventario(stock_actual: int, ventas_diarias: float) -> float: #Cuántos días durará el stock al ritmo de ventas actual.Si no hay ventas, el stock dura 'infinito' (devolvemos -1 como señal)
    if stock_actual < 0:   # Bloqueamos inmediatamente valores inadecuados
        raise ValueError("stock_actual no puede ser negativo")
        
    if ventas_diarias < 0:
        raise ValueError("ventas_diarias no puede ser negativo")
        
    if ventas_diarias == 0: # evitamos que divida por cero es decir si tiene productos pero si vende 0 entonces el inventario duraria infinito algo que debemos evitar
        return -1.0    # capturamos esto y devolvemos un -1.0 como señal de advertencia qye esta haciendolo mal
    
    return stock_actual / ventas_diarias  # Logica si tengo 100 panes y vendo 10 al dia entonces me duraran 10 dias


# 2. Decidir si requiere pedir inventario
def necesita_reposicion(stock_actual: int, ventas_diarias: float, umbral_dias: int = 7) -> bool:  # esto es para definir si el stock se acaba en un numero de dias
    dias = dias_de_inventario(stock_actual, ventas_diarias) # ahora calculamos cuantos dias de inventario le quedan de acuerdo a la primera funcion de stock vs ventas 
    if dias == -1.0: # Si recibimos la señal de infinito (-1.0), significa que no hay ventas
        return False  # por lo tanto no hay consumo y NO se necesita inventario devolvemos false

    return dias < umbral_dias

    # umbral_dias = 7
    # Compara los dias calculados contra el "umbral_dias" (por defecto es una semana: 7 dias).
    # Si los dias de stok restantes son menores a 7 dias significa que necesitamos inventario