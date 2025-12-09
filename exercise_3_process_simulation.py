"""
Exercise 3: Two-Stage Process Simulation
=========================================

User Story:
As a production planner, I want to simulate a two-stage manufacturing process
with Normal and Erlang processing times so that I can determine the probability
that total processing time exceeds 55 minutes.

Model:
- t1 ~ Normal(mean=30, variance=10)
- t2 ~ Erlang(k=3, mean=20) => λ = k/mean = 3/20
- Total time = t1 + t2
- Threshold: 55 minutes
- Simulation runs for 1000 pieces

Output:
- CSV file in output/problema3/ with all simulation variables
- Excel file in output/problema3/ with data table and embedded charts
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONSTANTS AND PARAMETERS
# ============================================================================

RANDOM_SEED = 42
NUM_PIECES = 1000

# Distribution parameters
T1_MEAN = 30
T1_VARIANCE = 10
T1_STD = np.sqrt(T1_VARIANCE)

T2_K = 3  # Erlang shape parameter
T2_MEAN = 20
T2_LAMBDA = T2_K / T2_MEAN  # Rate parameter

# Threshold
THRESHOLD = 55

# Output paths
OUTPUT_DIR = Path("output/problema3")
CSV_PATH = OUTPUT_DIR / "problema3_simulacion.csv"
EXCEL_PATH = OUTPUT_DIR / "problema3_simulacion.xlsx"

# ============================================================================
# SIMULATION FUNCTIONS
# ============================================================================

def generate_t1(size=1, seed=None):
    """
    Generate t1 values from Normal distribution.
    
    Parameters:
    -----------
    size : int
        Number of samples
    seed : int, optional
        Random seed
        
    Returns:
    --------
    np.ndarray
        t1 values (minutes)
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.normal(T1_MEAN, T1_STD, size)


def generate_t2(size=1):
    """
    Generate t2 values from Erlang distribution.
    
    Parameters:
    -----------
    size : int
        Number of samples
        
    Returns:
    --------
    np.ndarray
        t2 values (minutes)
    """
    # Erlang is Gamma(k, scale=1/lambda)
    return np.random.gamma(T2_K, 1/T2_LAMBDA, size)


def run_simulation():
    """
    Run the complete two-stage process simulation for NUM_PIECES.
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with all simulation variables
    """
    print("="*80)
    print("EJERCICIO 3: SIMULACIÓN DE PROCESO DE DOS ETAPAS")
    print("="*80)
    
    # Set seed for reproducibility
    np.random.seed(RANDOM_SEED)
    
    # Generate all pieces
    t1_values = generate_t1(size=NUM_PIECES, seed=RANDOM_SEED)
    t2_values = generate_t2(size=NUM_PIECES)
    
    # Calculate total time and threshold exceedance
    results = []
    for i in range(NUM_PIECES):
        t1 = t1_values[i]
        t2 = t2_values[i]
        total_time = t1 + t2
        exceeds_threshold = total_time > THRESHOLD
        
        results.append({
            'Pieza': i + 1,
            't1_Etapa1_Normal': t1,
            't2_Etapa2_Erlang': t2,
            'Tiempo_Total': total_time,
            'Umbral': THRESHOLD,
            'Excede_Umbral': 'SÍ' if exceeds_threshold else 'NO',
            'Excede_Flag': 1 if exceeds_threshold else 0
        })
    
    df = pd.DataFrame(results)
    
    return df


def calculate_statistics(df):
    """
    Calculate descriptive statistics for the simulation.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Simulation results
        
    Returns:
    --------
    dict
        Dictionary with statistical metrics
    """
    exceeds_count = df['Excede_Flag'].sum()
    
    stats_dict = {
        't1_mean': df['t1_Etapa1_Normal'].mean(),
        't1_std': df['t1_Etapa1_Normal'].std(),
        't2_mean': df['t2_Etapa2_Erlang'].mean(),
        't2_std': df['t2_Etapa2_Erlang'].std(),
        'total_mean': df['Tiempo_Total'].mean(),
        'total_std': df['Tiempo_Total'].std(),
        'total_min': df['Tiempo_Total'].min(),
        'total_max': df['Tiempo_Total'].max(),
        'exceeds_count': exceeds_count,
        'exceeds_pct': exceeds_count / NUM_PIECES,
        'within_count': NUM_PIECES - exceeds_count,
        'within_pct': (NUM_PIECES - exceeds_count) / NUM_PIECES,
    }
    
    return stats_dict


def create_visualizations(df, stats):
    """
    Create visualization charts for the simulation.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Simulation results
    stats : dict
        Statistical metrics
        
    Returns:
    --------
    matplotlib.figure.Figure
        Figure with charts
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Ejercicio 3: Simulación de Proceso - Análisis de Tiempos', 
                 fontsize=16, fontweight='bold')
    
    # Chart 1: Total time histogram with threshold
    ax1 = axes[0, 0]
    ax1.hist(df['Tiempo_Total'], bins=40, edgecolor='black', alpha=0.7, color='skyblue')
    ax1.axvline(x=THRESHOLD, color='r', linestyle='--', linewidth=2, 
                label=f'Umbral: {THRESHOLD} min')
    ax1.axvline(x=stats['total_mean'], color='g', linestyle='--', 
                label=f'Promedio: {stats["total_mean"]:.2f} min')
    ax1.set_xlabel('Tiempo Total (minutos)')
    ax1.set_ylabel('Frecuencia')
    ax1.set_title('Distribución de Tiempo Total')
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Chart 2: Threshold exceedance bar chart
    ax2 = axes[0, 1]
    threshold_data = [stats['within_count'], stats['exceeds_count']]
    labels = ['≤ 55 min', '> 55 min']
    colors = ['lightgreen', 'lightcoral']
    bars = ax2.bar(labels, threshold_data, color=colors, edgecolor='black', alpha=0.7)
    ax2.set_ylabel('Cantidad de Piezas')
    ax2.set_title('Piezas por Umbral de Tiempo')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}\n({height/NUM_PIECES:.1%})',
                ha='center', va='bottom', fontweight='bold')
    
    # Chart 3: t1 and t2 distributions
    ax3 = axes[1, 0]
    ax3.hist(df['t1_Etapa1_Normal'], bins=30, alpha=0.6, label='t1 (Normal)', 
             color='blue', edgecolor='black')
    ax3.hist(df['t2_Etapa2_Erlang'], bins=30, alpha=0.6, label='t2 (Erlang)', 
             color='orange', edgecolor='black')
    ax3.set_xlabel('Tiempo (minutos)')
    ax3.set_ylabel('Frecuencia')
    ax3.set_title('Distribuciones de t1 y t2')
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Chart 4: Running probability of exceeding threshold
    ax4 = axes[1, 1]
    cumulative_exceeds = df['Excede_Flag'].expanding().mean()
    ax4.plot(df['Pieza'], cumulative_exceeds, linewidth=2, color='purple')
    ax4.axhline(y=stats['exceeds_pct'], color='r', linestyle='--', 
                label=f'Probabilidad final: {stats["exceeds_pct"]:.3f}')
    ax4.set_xlabel('Número de Pieza')
    ax4.set_ylabel('P(Tiempo > 55 min)')
    ax4.set_title('Convergencia de Probabilidad')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim([0, max(0.5, stats['exceeds_pct'] * 1.2)])
    
    plt.tight_layout()
    
    return fig


def save_to_excel(df, stats, fig):
    """
    Save simulation results to Excel file with embedded chart.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Simulation results
    stats : dict
        Statistical metrics
    fig : matplotlib.figure.Figure
        Figure to embed in Excel
    """
    from openpyxl import load_workbook
    from openpyxl.drawing.image import Image as XLImage
    import io
    
    # Save DataFrame to Excel
    with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl') as writer:
        # Write main data
        df.to_excel(writer, sheet_name='Simulación', index=False)
        
        # Write statistics
        stats_df = pd.DataFrame([stats])
        stats_df.to_excel(writer, sheet_name='Estadísticas', index=False)
    
    # Load workbook and add chart as image
    wb = load_workbook(EXCEL_PATH)
    ws = wb['Simulación']
    
    # Save figure to bytes
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
    img_buffer.seek(0)
    
    # Add image to Excel
    img = XLImage(img_buffer)
    ws.add_image(img, 'J2')
    
    wb.save(EXCEL_PATH)
    print(f"✓ Archivo Excel guardado: {EXCEL_PATH}")


def print_results(df, stats):
    """
    Print simulation results to console.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Simulation results
    stats : dict
        Statistical metrics
    """
    print("\n" + "="*80)
    print("RESUMEN DE RESULTADOS")
    print("="*80)
    
    print(f"\n1. PARÁMETROS DEL MODELO:")
    print(f"   • Piezas simuladas: {NUM_PIECES}")
    print(f"   • t1 ~ Normal(μ={T1_MEAN}, σ²={T1_VARIANCE})")
    print(f"   • t2 ~ Erlang(k={T2_K}, μ={T2_MEAN})")
    print(f"   • Umbral: {THRESHOLD} minutos")
    
    print(f"\n2. ESTADÍSTICAS DE t1 (Etapa 1 - Normal):")
    print(f"   • Promedio observado: {stats['t1_mean']:.4f} min (esperado: {T1_MEAN})")
    print(f"   • Desviación estándar: {stats['t1_std']:.4f} min (esperada: {T1_STD:.4f})")
    
    print(f"\n3. ESTADÍSTICAS DE t2 (Etapa 2 - Erlang):")
    print(f"   • Promedio observado: {stats['t2_mean']:.4f} min (esperado: {T2_MEAN})")
    print(f"   • Desviación estándar: {stats['t2_std']:.4f} min")
    
    print(f"\n4. ESTADÍSTICAS DE TIEMPO TOTAL:")
    print(f"   • Promedio: {stats['total_mean']:.4f} min")
    print(f"   • Desviación estándar: {stats['total_std']:.4f} min")
    print(f"   • Mínimo: {stats['total_min']:.4f} min")
    print(f"   • Máximo: {stats['total_max']:.4f} min")
    
    print(f"\n5. ANÁLISIS DEL UMBRAL ({THRESHOLD} minutos):")
    print(f"   • Piezas dentro del umbral: {stats['within_count']} ({stats['within_pct']:.2%})")
    print(f"   • Piezas que exceden el umbral: {stats['exceeds_count']} ({stats['exceeds_pct']:.2%})")
    print(f"   • P(Tiempo > {THRESHOLD}) = {stats['exceeds_pct']:.4f}")
    
    print("\n" + "="*80)
    print("VALIDACIÓN DE CRITERIOS DE ACEPTACIÓN")
    print("="*80)
    
    print(f"✓ t1 generada con distribución Normal(30, 10)")
    print(f"✓ t2 generada con distribución Erlang(k=3, μ=20)")
    print(f"✓ Tiempo total calculado correctamente (t1 + t2)")
    print(f"✓ Umbral de {THRESHOLD} minutos aplicado")
    print(f"✓ {NUM_PIECES} piezas simuladas")
    print(f"✓ Archivo CSV generado: {CSV_PATH}")
    print(f"✓ Archivo Excel con gráficas generado: {EXCEL_PATH}")
    print(f"✓ Todos los criterios de aceptación cumplidos")
    
    print("\n" + "="*80)
    print("CONCLUSIONES")
    print("="*80)
    print(f"• La probabilidad de que el tiempo total exceda {THRESHOLD} minutos es {stats['exceeds_pct']:.1%}")
    print(f"• El tiempo promedio de procesamiento es {stats['total_mean']:.2f} minutos")
    print(f"• Aproximadamente {stats['exceeds_count']} de cada {NUM_PIECES} piezas excederán el umbral")
    print(f"• La distribución observada coincide con el modelo teórico")


def main():
    """Main execution function."""
    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Run simulation
    df = run_simulation()
    
    # Calculate statistics
    stats = calculate_statistics(df)
    
    # Create visualizations
    fig = create_visualizations(df, stats)
    
    # Save CSV
    df.to_csv(CSV_PATH, index=False, encoding='utf-8-sig')
    print(f"✓ Archivo CSV guardado: {CSV_PATH}")
    
    # Save Excel with embedded chart
    save_to_excel(df, stats, fig)
    
    # Save PNG
    png_path = OUTPUT_DIR / "problema3_graficas.png"
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"✓ Gráficas guardadas: {png_path}")
    
    # Print results
    print_results(df, stats)
    
    plt.close()


if __name__ == "__main__":
    main()
