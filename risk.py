from itertools import product, permutations
import tkinter as tk
from tkinter import ttk, messagebox


PUNTOS_TOTALES = 20
COSTOS = {
    'Infantería': 1,
    'Caballería': 3,
    'Artillería': 5
}
FUERZA = {
    'Infantería': 1,
    'Caballería': 3,
    'Artillería': 5
}


territorios = {
    'Territorio 1': 10,
    'Territorio 2': 15,
    'Territorio 3': 12
}

# Generar combinaciones válidas 
def generar_combinaciones_validas():
    combinaciones_validas = []
    for inf, cab, art in product(range(PUNTOS_TOTALES + 1), repeat=3):
        if (inf * COSTOS['Infantería'] + cab * COSTOS['Caballería'] + art * COSTOS['Artillería']) <= PUNTOS_TOTALES:
            if inf >= 1 and cab >= 1 and art >= 1:
                combinaciones_validas.append({'Infantería': inf, 'Caballería': cab, 'Artillería': art})
    return combinaciones_validas





def generar_permutaciones_ataque():
    return list(permutations(territorios.keys()))







# éxito de un ataque
def calcular_exito(combinacion, territorio):
    fuerza_total = (combinacion['Infantería'] * FUERZA['Infantería'] +
                    combinacion['Caballería'] * FUERZA['Caballería'] +
                    combinacion['Artillería'] * FUERZA['Artillería'])
    return fuerza_total >= territorios[territorio]







# maximizar conquistas
def optimizar_combinaciones():
    combinaciones = generar_combinaciones_validas()
    mejores_resultados = []
    for combinacion in combinaciones:
        victorias = sum(calcular_exito(combinacion, territorio) for territorio in territorios)
        mejores_resultados.append((combinacion, victorias))
    mejores_resultados.sort(key=lambda x: x[1], reverse=True)
    return mejores_resultados[0]








# territorios más débiles
def ordenar_territorios_por_debilidad():
    return sorted(territorios.items(), key=lambda x: x[1])






# estrategia según tipo de tropas y territorio
def estrategia_tipo_terreno(combinacion):
    estrategia = {
        'Territorio 1': 'Infantería',
        'Territorio 2': 'Caballería',
        'Territorio 3': 'Artillería'
    }
    for territorio, tipo_prioritario in estrategia.items():
        print(f"En {territorio}, prioriza el uso de {tipo_prioritario}.")





# optimizar eficiencia/costo
def optimizar_por_eficiencia():
    combinaciones = generar_combinaciones_validas()
    combinaciones.sort(key=lambda c: sum(c[tipo] * COSTOS[tipo] for tipo in c))
    return combinaciones[0]




# implementacion de interfaz grafica
def iniciar_interfaz():
    root = tk.Tk()
    root.title("Planificador de Ataques - Risk")
    root.geometry("600x600")

    ttk.Label(root, text="Planificador de Ataques", font=("Helvetica", 16)).pack(pady=10)
    
    # Botones 
    def mostrar_combinaciones():
        resultado = generar_combinaciones_validas()
        messagebox.showinfo("Combinaciones Válidas", f"Se generaron {len(resultado)} combinaciones válidas.")
    
    def mostrar_permutaciones():
        resultado = generar_permutaciones_ataque()
        messagebox.showinfo("Permutaciones", f"Se generaron {len(resultado)} permutaciones.")
    
    def mostrar_optimizacion():
        mejor_combinacion, victorias = optimizar_combinaciones()
        messagebox.showinfo("Optimización", f"Mejor combinación: {mejor_combinacion}, Victorias: {victorias}")
    
    def mostrar_territorios_debiles():
        orden = ordenar_territorios_por_debilidad()
        messagebox.showinfo("Orden de Ataque", f"Orden recomendado: {orden}")
    
    
    ttk.Button(root, text="Generar Combinaciones", command=mostrar_combinaciones).pack(pady=5)
    ttk.Button(root, text="Generar Permutaciones", command=mostrar_permutaciones).pack(pady=5)
    ttk.Button(root, text="Optimizar Estrategia", command=mostrar_optimizacion).pack(pady=5)
    ttk.Button(root, text="Ordenar por Debilidad", command=mostrar_territorios_debiles).pack(pady=5)
    
    ttk.Button(root, text="Salir", command=root.quit).pack(pady=20)
    
    root.mainloop()

if __name__ == '__main__':
    iniciar_interfaz()

