def calcular_interes_simple(prestamo: float, tasa: float, tiempo_meses: int) -> float:
    """
    Calcula el interés basado en la lógica migrada del sistema legacy.
    """
    if prestamo <= 0 or tasa <= 0:
        raise ValueError("Los valores deben ser positivos")
        
    return (prestamo * tasa * tiempo_meses) / 100

# Ejemplo de uso
if __name__ == "__main__":
    resultado = calcular_interes_simple(5000.00, 5.50, 12)
    print(f"Resultado Modernizado: ${resultado:,.2f}")