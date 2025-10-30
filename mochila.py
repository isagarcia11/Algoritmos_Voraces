def mochila_fraccionaria(valores, pesos, capacidad, heuristica):
    n = len(valores)
    items = []

    # Construcción de la lista de objetos con su criterio
    for i in range(n):
        if heuristica == 1:
            criterio = valores[i]  # mayor valor primero
        elif heuristica == 2:
            criterio = 1 / pesos[i]  # menor peso primero
        else:
            criterio = valores[i] / pesos[i]  # mayor valor/peso
        items.append((i + 1, valores[i], pesos[i], criterio))

    # Ordenar los objetos según el criterio
    items.sort(key=lambda x: x[3], reverse=True)

    print("\n===================================================")
    if heuristica == 1:
        print("Heurística 1: Mayor valor primero")
    elif heuristica == 2:
        print("Heurística 2: Menor peso primero")
    else:
        print("Heurística 3: Mayor valor/peso (eficiencia)")
    print("===================================================")

    print("ID\tValor\tPeso\tCriterio")
    for i in items:
        print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]:.2f}")

    valor_total = 0
    peso_actual = 0
    seleccion = []

    print("\n--- Proceso de llenado de la mochila ---")
    for (id, valor, peso, crit) in items:
        if peso_actual + peso <= capacidad:
            valor_total += valor
            peso_actual += peso
            seleccion.append((id, valor, peso, 1))
            print(f"Se toma TODO el objeto {id} (peso={peso}, valor={valor})")
        else:
            fraccion = (capacidad - peso_actual) / peso
            valor_total += valor * fraccion
            peso_actual = capacidad
            seleccion.append((id, valor, peso, fraccion))
            print(f"Se toma {fraccion*100:.2f}% del objeto {id} (peso={peso}, valor={valor})")
            break

    print("\nResultado final")
    print(f"Valor total obtenido: {valor_total:.2f}")
    print(f"Peso total usado: {peso_actual:.2f}/{capacidad}")
    print("\nDetalle de selección:")
    for s in seleccion:
        print(f"Objeto {s[0]} → Valor={s[1]}, Peso={s[2]}, Fracción={s[3]:.2f}")

    return valor_total


# ----------- PROGRAMA PRINCIPAL -----------

print("PROBLEMA DE LA MOCHILA FRACCIONARIA (Algoritmo Voraz)")

# Ingreso de datos
n = int(input("Ingrese la cantidad de objetos: "))

valores = []
pesos = []

for i in range(n):
    print(f"\nObjeto {i+1}:")
    v = float(input("  Valor: "))
    p = float(input("  Peso: "))
    valores.append(v)
    pesos.append(p)

capacidad = float(input("\nIngrese la capacidad máxima de la mochila: "))

# Ejecutar las tres heurísticas
resultados = []
for h in [1, 2, 3]:
    valor_total = mochila_fraccionaria(valores, pesos, capacidad, h)
    resultados.append((h, valor_total))

# Mostrar comparación final
print("\n===============================================")
print("COMPARATIVA FINAL DE LAS TRES HEURÍSTICAS")

for (h, valor) in resultados:
    if h == 1:
        nombre = "Mayor valor"
    elif h == 2:
        nombre = "Menor peso"
    else:
        nombre = "Mayor valor/peso"
    print(f"{nombre:25s} → Valor total: {valor:.2f}")
