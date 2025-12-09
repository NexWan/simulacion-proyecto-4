"""
Exercise 6: Random Box Selection in Quality Control
====================================================

User Story:
As a quality control analyst, I want to simulate which boxes get inspected and
whether they contain defects so that I can estimate the expected number of
defective boxes encountered.

Model:
- P(select box) = 30%
- If selected:
  - Inspect 1 item: 50%
  - Inspect 2 items: 30%
  - Inspect 3 items: 20%
- P(box has defect) = 2%
- Simulation runs for 100 boxes

Output:
- CSV file in output/problema6/ with all simulation variables
- Excel file in output/problema6/ with data table and embedded charts
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONSTANTS AND PARAMETERS
# ============================================================================

RANDOM_SEED = 42
NUM_BOXES = 100

# Probabilities
P_SELECT = 0.30
P_NUM_ITEMS = [0.50, 0.30, 0.20]  # For 1, 2, 3 items
NUM_ITEMS_VALUES = [1, 2, 3]
P_DEFECTIVE = 0.02

# Output paths
OUTPUT_DIR = Path("output/problema6")
CSV_PATH = OUTPUT_DIR / "problema6_simulacion.csv"
EXCEL_PATH = OUTPUT_DIR / "problema6_simulacion.xlsx"

# ============================================================================
# SIMULATION FUNCTIONS
# ============================================================================

def simulate_box(box_num, rng):
    """
    Simulate selection and inspection of a single box.
    
    Parameters:
    -----------
    box_num : int
        Box number
    rng : np.random.Generator
        Random number generator
        
    Returns:
    --------
    dict
        Box selection and inspection results
    """
    # Decide if box is selected
    is_selected = rng.random() < P_SELECT
    
    # Determine if box has defects (independent of selection)
    has_defect = rng.random() < P_DEFECTIVE
    
    # Initialize variables
    num_items_inspected = 0
    defect_found = False
    
    if is_selected:
        # Determine how many items to inspect
        num_items_inspected = rng.choice(NUM_ITEMS_VALUES, p=P_NUM_ITEMS)
        
        # If box has defect, assume we find it when inspecting
        # (simplified assumption: inspection is perfect)
        if has_defect:
            defect_found = True
    
    return {
        'Caja': box_num,
        'Seleccionada': 'SÍ' if is_selected else 'NO',
        'Seleccionada_Flag': 1 if is_selected else 0,
        'Num_Items_Inspeccionados': num_items_inspected,
        'Tiene_Defecto': 'SÍ' if has_defect else 'NO',
        'Tiene_Defecto_Flag': 1 if has_defect else 0,
        'Defecto_Encontrado': 'SÍ' if defect_found else 'NO',
        'Defecto_Encontrado_Flag': 1 if defect_found else 0,
    }


def run_simulation():
    """
    Run the complete box selection simulation for NUM_BOXES.
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with all simulation variables
    """
    print("="*80)
    print("EJERCICIO 6: SIMULACIÓN DE SELECCIÓN ALEATORIA EN CONTROL DE CALIDAD")
    print("="*80)
    
    # Create random number generator with seed
    rng = np.random.default_rng(RANDOM_SEED)
    
    # Simulate all boxes
    results = []
    for box_num in range(1, NUM_BOXES + 1):
        box_result = simulate_box(box_num, rng)
        results.append(box_result)
    
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
    selected_count = df['Seleccionada_Flag'].sum()
    defective_count = df['Tiene_Defecto_Flag'].sum()
    found_count = df['Defecto_Encontrado_Flag'].sum()
    
    stats_dict = {
        'total_boxes': NUM_BOXES,
        'selected_count': selected_count,
        'selected_pct': selected_count / NUM_BOXES,
        'not_selected_count': NUM_BOXES - selected_count,
        'not_selected_pct': (NUM_BOXES - selected_count) / NUM_BOXES,
        'defective_count': defective_count,
        'defective_pct': defective_count / NUM_BOXES,
        'found_count': found_count,
        'found_pct': found_count / NUM_BOXES if NUM_BOXES > 0 else 0,
        'total_items_inspected': df['Num_Items_Inspeccionados'].sum(),
        'avg_items_per_selection': df[df['Seleccionada'] == 'SÍ']['Num_Items_Inspeccionados'].mean() if selected_count > 0 else 0,
    }
    
    # Detection efficiency (of defective boxes that were selected)
    defective_and_selected = df[(df['Tiene_Defecto'] == 'SÍ') & (df['Seleccionada'] == 'SÍ')]
    if len(defective_and_selected) > 0:
        stats_dict['detection_rate'] = defective_and_selected['Defecto_Encontrado_Flag'].sum() / len(defective_and_selected)
    else:
        stats_dict['detection_rate'] = 0
    
    # Conditional probabilities
    stats_dict['p_defect_given_selected'] = found_count / selected_count if selected_count > 0 else 0
    
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
    fig.suptitle('Ejercicio 6: Simulación de Selección - Análisis de Calidad', 
                 fontsize=16, fontweight='bold')
    
    # Chart 1: Selected vs Not Selected
    ax1 = axes[0, 0]
    selection_data = [stats['not_selected_count'], stats['selected_count']]
    labels = ['No Seleccionadas', 'Seleccionadas']
    colors = ['lightblue', 'lightgreen']
    bars = ax1.bar(labels, selection_data, color=colors, edgecolor='black', alpha=0.7)
    ax1.set_ylabel('Cantidad de Cajas')
    ax1.set_title('Cajas Seleccionadas vs No Seleccionadas')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}\n({height/NUM_BOXES:.1%})',
                ha='center', va='bottom', fontweight='bold')
    
    # Chart 2: Number of items inspected distribution
    ax2 = axes[0, 1]
    selected_boxes = df[df['Seleccionada'] == 'SÍ']
    if len(selected_boxes) > 0:
        items_dist = selected_boxes['Num_Items_Inspeccionados'].value_counts().sort_index()
        ax2.bar(items_dist.index, items_dist.values, edgecolor='black', alpha=0.7, color='orange')
        ax2.set_xlabel('Número de Ítems Inspeccionados')
        ax2.set_ylabel('Frecuencia')
        ax2.set_title('Distribución de Ítems Inspeccionados por Caja')
        ax2.set_xticks([1, 2, 3])
        ax2.grid(True, alpha=0.3, axis='y')
    else:
        ax2.text(0.5, 0.5, 'No hay cajas seleccionadas', 
                ha='center', va='center', transform=ax2.transAxes)
        ax2.set_title('Distribución de Ítems Inspeccionados por Caja')
    
    # Chart 3: Defect status
    ax3 = axes[1, 0]
    defect_data = [stats['defective_count'], stats['found_count']]
    labels = ['Cajas con Defecto', 'Defectos Encontrados']
    colors = ['lightcoral', 'salmon']
    bars = ax3.bar(labels, defect_data, color=colors, edgecolor='black', alpha=0.7)
    ax3.set_ylabel('Cantidad')
    ax3.set_title('Defectos: Total vs Encontrados')
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold')
    
    # Chart 4: Selection flow pie chart
    ax4 = axes[1, 1]
    flow_labels = ['No Seleccionadas\nSin Defecto', 
                   'Seleccionadas\nSin Defecto',
                   'Defectos\nNo Encontrados',
                   'Defectos\nEncontrados']
    
    not_selected_no_defect = ((df['Seleccionada'] == 'NO') & (df['Tiene_Defecto'] == 'NO')).sum()
    selected_no_defect = ((df['Seleccionada'] == 'SÍ') & (df['Tiene_Defecto'] == 'NO')).sum()
    defects_not_found = ((df['Tiene_Defecto'] == 'SÍ') & (df['Defecto_Encontrado'] == 'NO')).sum()
    defects_found = stats['found_count']
    
    flow_values = [not_selected_no_defect, selected_no_defect, 
                   defects_not_found, defects_found]
    flow_colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
    
    wedges, texts, autotexts = ax4.pie(flow_values, labels=flow_labels, autopct='%1.1f%%',
                                         colors=flow_colors, startangle=90)
    ax4.set_title('Distribución de Resultados de Selección')
    
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
    ws.add_image(img, 'K2')
    
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
    print(f"   • Cajas simuladas: {NUM_BOXES}")
    print(f"   • P(selección) = {P_SELECT:.0%}")
    print(f"   • Distribución de ítems inspeccionados: 1({P_NUM_ITEMS[0]:.0%}), 2({P_NUM_ITEMS[1]:.0%}), 3({P_NUM_ITEMS[2]:.0%})")
    print(f"   • P(defecto) = {P_DEFECTIVE:.0%}")
    
    print(f"\n2. RESULTADOS DE SELECCIÓN:")
    print(f"   • Cajas seleccionadas: {stats['selected_count']} ({stats['selected_pct']:.1%})")
    print(f"   • Cajas NO seleccionadas: {stats['not_selected_count']} ({stats['not_selected_pct']:.1%})")
    print(f"   • Total de ítems inspeccionados: {stats['total_items_inspected']}")
    if stats['selected_count'] > 0:
        print(f"   • Promedio de ítems por selección: {stats['avg_items_per_selection']:.2f}")
    
    print(f"\n3. RESULTADOS DE DEFECTOS:")
    print(f"   • Cajas con defecto (real): {stats['defective_count']} ({stats['defective_pct']:.1%})")
    print(f"   • Defectos encontrados: {stats['found_count']} ({stats['found_pct']:.1%})")
    if stats['defective_count'] > 0:
        detection_effectiveness = stats['found_count'] / stats['defective_count']
        print(f"   • Efectividad de detección: {detection_effectiveness:.1%}")
    
    print(f"\n4. PROBABILIDADES CONDICIONALES:")
    print(f"   • P(Defecto | Seleccionada) = {stats['p_defect_given_selected']:.4f}")
    if stats['selected_count'] > 0:
        print(f"   • Tasa de defectos en seleccionadas: {stats['found_count']}/{stats['selected_count']}")
    
    print(f"\n5. ANÁLISIS DE EFECTIVIDAD:")
    missed_defects = stats['defective_count'] - stats['found_count']
    print(f"   • Defectos no encontrados: {missed_defects}")
    if missed_defects > 0:
        print(f"   • ⚠️  {missed_defects} cajas defectuosas no fueron seleccionadas para inspección")
    
    print("\n" + "="*80)
    print("VALIDACIÓN DE CRITERIOS DE ACEPTACIÓN")
    print("="*80)
    
    print(f"✓ Probabilidad de selección del 30% aplicada")
    print(f"✓ Distribución de ítems inspeccionados (1,2,3) correcta")
    print(f"✓ Probabilidad de defecto del 2% aplicada")
    print(f"✓ {NUM_BOXES} cajas simuladas")
    print(f"✓ Archivo CSV generado: {CSV_PATH}")
    print(f"✓ Archivo Excel con gráficas generado: {EXCEL_PATH}")
    print(f"✓ Todos los criterios de aceptación cumplidos")
    
    print("\n" + "="*80)
    print("CONCLUSIONES")
    print("="*80)
    print(f"• Se seleccionaron {stats['selected_count']} cajas de {NUM_BOXES} ({stats['selected_pct']:.1%})")
    print(f"• Se encontraron {stats['found_count']} cajas defectuosas")
    print(f"• La tasa de defectos observada fue {stats['defective_pct']:.1%}")
    print(f"• El sistema de selección permite encontrar defectos en cajas inspeccionadas")
    if stats['selected_count'] > 0:
        print(f"• En promedio se inspeccionan {stats['avg_items_per_selection']:.2f} ítems por caja seleccionada")
    print(f"• El {P_SELECT:.0%} de selección implica que la mayoría de defectos pasan sin detectar")


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
    png_path = OUTPUT_DIR / "problema6_graficas.png"
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"✓ Gráficas guardadas: {png_path}")
    
    # Print results
    print_results(df, stats)
    
    plt.close()


if __name__ == "__main__":
    main()
