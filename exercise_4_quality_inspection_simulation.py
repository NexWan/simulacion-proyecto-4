"""
Ejercicio 4: Simulación de Inspección (CORREGIDO)
==================================================
Objetivo:
Simular un proceso de inspección continua donde:
- Tiempos de inspección ~ Normal(Media=6, Desviación=2).
- Probabilidad de defecto = 15%.
- Se simulan 100 piezas continuas.

Salida:
- CSV y Excel con datos detallados.
- Gráficas de tiempos y defectos.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import warnings
import io
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage

warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURACIÓN Y PARÁMETROS
# ============================================================================

RANDOM_SEED = 42
NUM_PIEZAS = 100

# Parámetros del Proceso (Según enunciado)
MEDIA_TIEMPO = 6.0      # Minutos
STD_TIEMPO = 2.0        # Minutos
PROB_DEFECTO = 0.15     # 15% de rechazo

# Rutas de salida
OUTPUT_DIR = Path("output/problema4")
CSV_PATH = OUTPUT_DIR / "problema4_simulacion.csv"
EXCEL_PATH = OUTPUT_DIR / "problema4_simulacion.xlsx"
IMG_PATH = OUTPUT_DIR / "problema4_graficas.png"

# ============================================================================
# LÓGICA DE SIMULACIÓN
# ============================================================================

def run_simulation():
    """Ejecuta la simulación de inspección pieza por pieza."""
    print(f"Iniciando simulación para {NUM_PIEZAS} piezas...")
    
    rng = np.random.default_rng(RANDOM_SEED)
    resultados = []
    
    for i in range(1, NUM_PIEZAS + 1):
        # 1. Generar Tiempo (Normal)
        # Usamos max(0.1, val) para evitar tiempos negativos en casos extremos
        tiempo = max(0.1, rng.normal(MEDIA_TIEMPO, STD_TIEMPO))
        
        # 2. Determinar si tiene defecto (Bernoulli)
        es_defectuosa = rng.random() < PROB_DEFECTO
        
        resultados.append({
            'Pieza_ID': i,
            'Tiempo_Inspeccion': round(tiempo, 4),
            'Estado': 'RECHAZADA' if es_defectuosa else 'ACEPTADA',
            'Defecto_Flag': 1 if es_defectuosa else 0,
            'Tiempo_Acumulado': 0 # Se calculará después
        })
    
    df = pd.DataFrame(resultados)
    df['Tiempo_Acumulado'] = df['Tiempo_Inspeccion'].cumsum()
    return df

def calculate_statistics(df):
    """Calcula métricas clave."""
    total_piezas = len(df)
    defectuosas = df['Defecto_Flag'].sum()
    tiempo_total = df['Tiempo_Inspeccion'].sum()
    
    return {
        'total_piezas': total_piezas,
        'piezas_defectuosas': defectuosas,
        'piezas_aceptadas': total_piezas - defectuosas,
        'tasa_rechazo_real': defectuosas / total_piezas,
        'tasa_rechazo_teorica': PROB_DEFECTO,
        'tiempo_total_min': tiempo_total,
        'tiempo_promedio_real': df['Tiempo_Inspeccion'].mean(),
        'tiempo_promedio_teorico': MEDIA_TIEMPO,
        'tiempo_std_real': df['Tiempo_Inspeccion'].std(),
        'tiempo_max': df['Tiempo_Inspeccion'].max(),
        'tiempo_min': df['Tiempo_Inspeccion'].min()
    }

# ============================================================================
# VISUALIZACIÓN Y REPORTES
# ============================================================================

def create_visualizations(df, stats):
    """Genera panel de 4 gráficas."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Ejercicio 4: Simulación de Tiempos y Calidad', fontsize=16, fontweight='bold')
    
    # 1. Histograma de Tiempos
    ax1 = axes[0, 0]
    ax1.hist(df['Tiempo_Inspeccion'], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    ax1.axvline(stats['tiempo_promedio_real'], color='green', linestyle='--', linewidth=2, label=f"Promedio: {stats['tiempo_promedio_real']:.2f}")
    ax1.axvline(MEDIA_TIEMPO, color='red', linestyle=':', linewidth=2, label=f"Teórico: {MEDIA_TIEMPO}")
    ax1.set_title('Distribución de Tiempos de Inspección')
    ax1.set_xlabel('Minutos')
    ax1.set_ylabel('Frecuencia')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. Pastel de Calidad (Aceptadas vs Rechazadas)
    ax2 = axes[0, 1]
    labels = ['Aceptadas', 'Rechazadas (Defecto)']
    sizes = [stats['piezas_aceptadas'], stats['piezas_defectuosas']]
    colors = ['lightgreen', 'salmon']
    explode = (0, 0.1)  # resaltar la rebanada de defectos
    
    ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax2.set_title('Proporción de Calidad')

    # 3. Serie de Tiempo (Tiempos individuales)
    ax3 = axes[1, 0]
    colores = ['red' if x == 1 else 'blue' for x in df['Defecto_Flag']]
    ax3.scatter(df['Pieza_ID'], df['Tiempo_Inspeccion'], c=colores, alpha=0.6)
    ax3.axhline(MEDIA_TIEMPO, color='gray', linestyle='--')
    ax3.set_title('Tiempos de Inspección por Pieza')
    ax3.set_xlabel('ID de Pieza')
    ax3.set_ylabel('Tiempo (min)')
    # Truco para la leyenda personalizada
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', label='Aceptada'),
                       Line2D([0], [0], marker='o', color='w', markerfacecolor='red', label='Rechazada')]
    ax3.legend(handles=legend_elements)
    ax3.grid(True, alpha=0.3)

    # 4. Convergencia del Promedio de Defectos
    ax4 = axes[1, 1]
    df['Tasa_Acumulada'] = df['Defecto_Flag'].expanding().mean()
    ax4.plot(df['Pieza_ID'], df['Tasa_Acumulada'], color='purple', linewidth=2)
    ax4.axhline(PROB_DEFECTO, color='red', linestyle='--', label='Objetivo (15%)')
    ax4.set_title('Convergencia de la Tasa de Rechazo')
    ax4.set_xlabel('Número de Piezas Simuladas')
    ax4.set_ylabel('Porcentaje de Defectos')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def save_to_excel_with_image(df, stats, fig):
    """Guarda datos y pega la imagen en el Excel."""
    
    # 1. Escribir datos numéricos
    with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl') as writer:
        df.drop(columns=['Tasa_Acumulada']).to_excel(writer, sheet_name='Simulación', index=False)
        pd.DataFrame([stats]).to_excel(writer, sheet_name='Estadísticas', index=False)
    
    # 2. Insertar Imagen
    wb = load_workbook(EXCEL_PATH)
    ws = wb['Simulación']
    
    # Convertir figura a bytes
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
    img_buffer.seek(0)
    
    # Pegar imagen
    img = XLImage(img_buffer)
    ws.add_image(img, 'H2') # Pegar en la celda H2
    
    wb.save(EXCEL_PATH)
    print(f"✓ Excel guardado con gráficos en: {EXCEL_PATH}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    # Crear carpeta si no existe
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Ejecutar
    df = run_simulation()
    stats = calculate_statistics(df)
    
    # Visualizar
    fig = create_visualizations(df, stats)
    
    # Guardar
    df.drop(columns=['Tasa_Acumulada']).to_csv(CSV_PATH, index=False)
    fig.savefig(IMG_PATH, dpi=150, bbox_inches='tight')
    save_to_excel_with_image(df, stats, fig)
    
    # Reporte en consola
    print("\n" + "="*50)
    print("RESUMEN EJERCICIO 4 (CORREGIDO)")
    print("="*50)
    print(f"Total Piezas: {stats['total_piezas']}")
    print(f"Rechazadas:   {stats['piezas_defectuosas']} ({stats['tasa_rechazo_real']:.1%}) - Esperado: 15%")
    print(f"Tiempo Medio: {stats['tiempo_promedio_real']:.2f} min - Esperado: 6.00 min")
    print(f"Tiempo Total: {stats['tiempo_total_min']:.2f} min")
    print("="*50)

if __name__ == "__main__":
    main()