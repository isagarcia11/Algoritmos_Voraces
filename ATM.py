def entregar_dinero_cajero(monto_solicitado: int) -> dict:
    # ... (El código de la función principal es el mismo y no necesita cambios) ...
    # Se omite para brevedad, pero usa la función original que ya tienes
    
    # 1. Verificar la condición de divisibilidad por 10000
    if monto_solicitado % 10000 != 0:
        return {
            "estado": "ERROR",
            "mensaje": f"El monto solicitado (${monto_solicitado:,.0f} COP) debe ser divisible por 10000.",
            "entregado": 0
        }

    denominaciones_disponibles = [
        (100000, 50), (50000, 100), (20000, 200), (10000, 300)
    ]

    monto_restante = monto_solicitado
    total_entregado = 0
    billetes_entregados = {}

    # 2. Aplicar el Algoritmo Voraz
    for valor, disponible in denominaciones_disponibles:
        if monto_restante == 0:
            break

        max_necesarios = monto_restante // valor
        cantidad_a_entregar = min(max_necesarios, disponible)

        if cantidad_a_entregar > 0:
            valor_entregado = cantidad_a_entregar * valor
            
            monto_restante -= valor_entregado
            total_entregado += valor_entregado
            
            billetes_entregados[valor] = cantidad_a_entregar
    
    # 3. Verificación final y salida
    if monto_restante == 0:
        return {
            "estado": "EXITO",
            "mensaje": f"Entrega exitosa. Total entregado: ${total_entregado:,.0f} COP.",
            "billetes_entregados": billetes_entregados
        }
    else:
        return {
            "estado": "ALERTA",
            "mensaje": f"No hay suficientes billetes para completar la solicitud. Solo se pudieron entregar ${total_entregado:,.0f} COP.",
            "billetes_entregados": billetes_entregados,
            "monto_faltante": monto_restante
        }

# ----------------------------------------------------------------------
# Parte para interacción con el usuario usando INPUT
# ----------------------------------------------------------------------

def main():
    print("--- Simulador de Cajero Automático (Algoritmo Voraz) ---")
    
    try:
        # Usamos input() para solicitar el dato
        monto_str = input("Ingrese el monto de dinero a retirar (en pesos colombianos, debe ser divisible por 10000): ")
        
        # Convertimos la entrada a un número entero
        monto = int(monto_str)
        
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")
        return

    # Llamamos a la función principal con el monto ingresado
    resultado = entregar_dinero_cajero(monto)

    print("\n--- Resultado de la Transacción ---")
    print(f"Estado: {resultado['estado']}")
    print(resultado['mensaje'])

    # Si hubo entrega (éxito o alerta parcial), mostramos el detalle
    if resultado["estado"] in ["EXITO", "ALERTA"]:
        print("\nDetalle de Billetes Entregados:")
        # Ordenamos los billetes entregados por valor (de mayor a menor)
        billetes_ordenados = sorted(resultado["billetes_entregados"].items(), key=lambda item: item[0], reverse=True)
        
        for valor, cantidad in billetes_ordenados:
            print(f"  - ${valor:,.0f}: {cantidad} unidad(es)")
        
        if resultado.get("monto_faltante", 0) > 0:
             print(f"\nMonto faltante por entregar: ${resultado['monto_faltante']:,.0f} COP.")

if __name__ == "__main__":
    main()