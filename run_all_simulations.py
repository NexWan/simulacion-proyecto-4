"""
Master Script to Run All Simulation Exercises
==============================================

This script executes all 6 simulation exercises in sequence and provides
a comprehensive summary of results.
"""

import subprocess
import time
import sys
from pathlib import Path

# Get Python executable (use current interpreter)
PYTHON_EXE = sys.executable

# List of all exercise scripts
EXERCISES = [
    ('exercise_1_restaurant_simulation.py', 'Problema 1: Restaurante de Comida Rápida'),
    ('exercise_2_welding_simulation.py', 'Problema 2: Soldadura de Barras Metálicas'),
    ('exercise_3_process_simulation.py', 'Problema 3: Proceso de Dos Etapas'),
    ('exercise_4_quality_inspection_simulation.py', 'Problema 4: Inspección de Control de Calidad'),
    ('exercise_5_queue_simulation.py', 'Problema 5: Cola M/M/1 en Gasolinera'),
    ('exercise_6_box_selection_simulation.py', 'Problema 6: Selección Aleatoria en Control de Calidad'),
]

def run_exercise(script_name, description):
    """
    Run a single exercise script.
    
    Parameters:
    -----------
    script_name : str
        Name of the Python script
    description : str
        Description of the exercise
        
    Returns:
    --------
    tuple
        (success: bool, execution_time: float)
    """
    print(f"\n{'='*80}")
    print(f"Ejecutando: {description}")
    print(f"Script: {script_name}")
    print(f"{'='*80}\n")
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            [PYTHON_EXE, script_name],
            capture_output=True,
            text=True,
            check=True
        )
        
        execution_time = time.time() - start_time
        
        # Print output
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        print(f"\n✓ {description} completado en {execution_time:.2f} segundos")
        
        return True, execution_time
        
    except subprocess.CalledProcessError as e:
        execution_time = time.time() - start_time
        print(f"\n✗ ERROR en {description}")
        print(f"Código de salida: {e.returncode}")
        print(f"STDOUT:\n{e.stdout}")
        print(f"STDERR:\n{e.stderr}")
        
        return False, execution_time


def list_output_files():
    """
    List all generated output files.
    
    Returns:
    --------
    dict
        Dictionary with file counts and sizes
    """
    output_dir = Path('output')
    
    if not output_dir.exists():
        return {}
    
    file_info = {
        'csv_files': [],
        'excel_files': [],
        'png_files': [],
    }
    
    # Scan all problema directories
    for problema_dir in output_dir.glob('problema*'):
        if problema_dir.is_dir():
            # Find files
            csv_files = list(problema_dir.glob('*.csv'))
            excel_files = list(problema_dir.glob('*.xlsx'))
            png_files = list(problema_dir.glob('*.png'))
            
            file_info['csv_files'].extend(csv_files)
            file_info['excel_files'].extend(excel_files)
            file_info['png_files'].extend(png_files)
    
    return file_info


def print_summary(results, total_time):
    """
    Print execution summary.
    
    Parameters:
    -----------
    results : list
        List of (exercise_name, success, time) tuples
    total_time : float
        Total execution time
    """
    print("\n" + "="*80)
    print("RESUMEN DE EJECUCIÓN")
    print("="*80)
    
    print(f"\nTiempo total de ejecución: {total_time:.2f} segundos\n")
    
    print("Resultados por ejercicio:")
    for i, (script, desc, success, ex_time) in enumerate(results, 1):
        status = "✓ EXITOSO" if success else "✗ FALLIDO"
        print(f"  {i}. {desc}")
        print(f"     Estado: {status} | Tiempo: {ex_time:.2f}s")
    
    # Count successes
    successful = sum(1 for _, _, success, _ in results if success)
    total = len(results)
    
    print(f"\nEjercicios completados exitosamente: {successful}/{total}")
    
    # List output files
    print("\n" + "="*80)
    print("ARCHIVOS GENERADOS")
    print("="*80)
    
    file_info = list_output_files()
    
    if file_info:
        print(f"\nArchivos CSV ({len(file_info['csv_files'])}):")
        for f in sorted(file_info['csv_files']):
            size = f.stat().st_size / 1024  # KB
            print(f"  • {f.relative_to('.')} ({size:.1f} KB)")
        
        print(f"\nArchivos Excel ({len(file_info['excel_files'])}):")
        for f in sorted(file_info['excel_files']):
            size = f.stat().st_size / 1024  # KB
            print(f"  • {f.relative_to('.')} ({size:.1f} KB)")
        
        print(f"\nArchivos PNG ({len(file_info['png_files'])}):")
        for f in sorted(file_info['png_files']):
            size = f.stat().st_size / 1024  # KB
            print(f"  • {f.relative_to('.')} ({size:.1f} KB)")
    else:
        print("\nNo se encontraron archivos de salida.")
    
    print("\n" + "="*80)
    print("ESTRUCTURA DE CARPETAS")
    print("="*80)
    
    output_dir = Path('output')
    if output_dir.exists():
        print("\noutput/")
        for item in sorted(output_dir.iterdir()):
            if item.is_dir():
                print(f"  ├── {item.name}/")
                for subitem in sorted(item.iterdir()):
                    print(f"  │   ├── {subitem.name}")
    
    print("\n" + "="*80)
    if successful == total:
        print("✓ TODOS LOS EJERCICIOS COMPLETADOS EXITOSAMENTE")
    else:
        print(f"⚠️  {total - successful} EJERCICIO(S) FALLARON")
    print("="*80 + "\n")


def main():
    """Main execution function."""
    print("="*80)
    print("PROYECTO 4: MODELOS DE SIMULACIÓN")
    print("Ejecutando los 6 ejercicios de simulación")
    print("="*80)
    
    start_time = time.time()
    results = []
    
    # Run all exercises
    for script, description in EXERCISES:
        success, ex_time = run_exercise(script, description)
        results.append((script, description, success, ex_time))
    
    total_time = time.time() - start_time
    
    # Print summary
    print_summary(results, total_time)


if __name__ == "__main__":
    main()
