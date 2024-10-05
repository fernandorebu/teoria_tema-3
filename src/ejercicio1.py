from datetime import date 
fecha_prueba = date(2024, 10, 2)

def fecha_en_intervalo(fecha, fecha_inicio, fecha_final):
    lista = []
    if fecha > fecha_inicio and fecha < fecha_final:
        lista.append(fecha)
    return lista




# Caso 1: fecha dentro del intervalo
print(fecha_en_intervalo(fecha_prueba, date(2024, 1, 1), ))  # True

# Caso 2: fecha fuera del intervalo (menor que fecha_min)
fecha_min = None
print(fecha_en_intervalo(fecha_prueba, date(2024, 10, 3), date(2024, 12, 31)))  # False

# Caso 3: fecha fuera del intervalo (mayor que fecha_max)
print(fecha_en_intervalo(fecha_prueba,None, date(2024, 9, 30)))  # False

# Caso 4: sin límite inferior (fecha_min es None)
print(fecha_en_intervalo(fecha_prueba, None, date(2024, 9, 30)))  # False

# Caso 5: sin límite superior (fecha_max es None)
print(fecha_en_intervalo(fecha_prueba, date(2024, 1, 1), None))  # True

# Caso 6: sin límites (fecha_min es None y fecha_max es None)
print(fecha_en_intervalo(fecha_prueba, None, None))  # True