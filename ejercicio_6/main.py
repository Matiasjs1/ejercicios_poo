from agenciaMarketing import AgenciaMarketing
from campaniaRedesSociales import CampaniaRedesSociales
from campaniaSEO import CampaniaSEO
import os
def main():
    # Crear una agencia de marketing
    agencia = AgenciaMarketing()
    
    # Crear una campaña de redes sociales
    campania_redes = CampaniaRedesSociales(
        cliente="Empresa A",
        presupuesto=5000,
        duracion=30,
        interacciones_sociales=["me gusta", "comentarios", "compartidos"]
    )
    
    # Registrar resultados para la campaña de redes sociales
    campania_redes.registrar_resultados(1, 100, 10, 200)
    campania_redes.registrar_resultados(2, 150, 15, 250)
    campania_redes.registrar_resultados(3, 200, 20, 300)
    
    # Crear una campaña SEO
    campania_seo = CampaniaSEO(
        cliente="Empresa B",
        presupuesto=3000,
        duracion=60,
        palabras_clave_efectivas=["marketing digital", "publicidad online", "SEO"]
    )
    
    # Registrar resultados para la campaña SEO
    campania_seo.registrar_resultados(1, 50, 5, 100)
    campania_seo.registrar_resultados(2, 75, 8, 150)
    campania_seo.registrar_resultados(3, 100, 12, 200)
    
    # Agregar campañas a la agencia
    agencia.agregar_nuevas_campanias(campania_redes)
    agencia.agregar_nuevas_campanias(campania_seo)
    
    # Mostrar información de todas las campañas
    print("\n=== Informe de todas las campañas ===")
    agencia.mostrar_informe()
    
    # Mostrar campañas de un tipo específico
    print("\n=== Campañas de Redes Sociales ===")
    for campania in agencia.listar_campania("redes_sociales"):
        campania.mostrar_info()
    
    # Mostrar ranking de eficiencia
    print("\n=== Ranking de Eficiencia ===")
    ranking = agencia.calcular_ranking_eficientes()
    for eficiencia, campania in ranking:
        print(f"Eficiencia: {eficiencia:.2f}")
        campania.mostrar_info()
    
    # Mostrar cliente con mejor ROI
    print("\n=== Cliente con Mejor ROI ===")
    print(f"Cliente: {agencia.calcular_cliente_mejor_ROI()}")
    
    # Mostrar campaña con mayor eficiencia
    print("\n=== Campaña con Mayor Eficiencia ===")
    eficiencia, campania = agencia.campania_mayor_eficiencia()
    print(f"Eficiencia: {eficiencia:.2f}")
    campania.mostrar_info()
    os.system("pause")

if __name__ == "__main__":
    main()
