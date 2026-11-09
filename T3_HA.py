import random
import math

def monte_carlo_interseccion():
    print("--- CÁLCULO DE ÁREA POR MÉTODO DE MONTECARLO (ELIPSE E HIPÉRBOLA) ---")
    

    a = float(input("Ingrese el valor de a (semieje en x de la elipse): "))
    b = float(input("Ingrese el valor de b (semieje en y de la elipse): "))
    c = float(input("Ingrese el valor de c para la hipérbola: "))
    d = float(input("Ingrese el valor de d para la hipérbola: "))
    cantidad = int(input("Ingrese la cantidad de puntos aleatorios a generar: "))
    
    puntos_en_elipse = 0
    puntos_en_interseccion = 0
    
    area_elipse_teorica = math.pi * a * b
    
    for _ in range(cantidad):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        
        es_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1
        
        if es_elipse:
            puntos_en_elipse += 1
            
            es_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1
            
            if es_hiperbola:
                puntos_en_interseccion += 1

    if puntos_en_elipse > 0:
        proporcion = puntos_en_interseccion / puntos_en_elipse
        area_aproximada_interseccion = proporcion * area_elipse_teorica
    else:
        area_aproximada_interseccion = 0.0

    print("\n--- RESULTADOS ---")
    print(f"1. Puntos aleatorios que cayeron dentro de la elipse: {puntos_en_elipse}")
    print(f"2. Puntos aleatorios que cayeron en la intersección (elipse e hipérbola): {puntos_en_interseccion}")
    print(f"3. Área aproximada de la zona de la elipse que se interseca con la hipérbola: {area_aproximada_interseccion:.4f}")

if __name__ == "__main__":
    monte_carlo_interseccion()
