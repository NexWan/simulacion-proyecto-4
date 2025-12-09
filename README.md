# Proyecto 4: Modelos de Simulación

## Descripción General

Este proyecto implementa 6 modelos de simulación estocástica siguiendo un enfoque de **Spec-Driven Development**, donde cada ejercicio se basa en una User Story formal con criterios de aceptación claramente definidos.

## Estructura del Proyecto

```
simulacion-proyecto-4/
├── output/                          # Directorio de salidas
│   ├── problema1/                   # Restaurante de comida rápida
│   │   ├── problema1_simulacion.csv
│   │   ├── problema1_simulacion.xlsx
│   │   └── problema1_graficas.png
│   ├── problema2/                   # Soldadura de barras metálicas
│   ├── problema3/                   # Proceso de dos etapas
│   ├── problema4/                   # Inspección de control de calidad
│   ├── problema5/                   # Cola M/M/1 en gasolinera
│   └── problema6/                   # Selección aleatoria en control de calidad
├── simulation_user_stories_v2/      # User stories de cada ejercicio
├── exercise_1_restaurant_simulation.py
├── exercise_2_welding_simulation.py
├── exercise_3_process_simulation.py
├── exercise_4_quality_inspection_simulation.py
├── exercise_5_queue_simulation.py
├── exercise_6_box_selection_simulation.py
├── run_all_simulations.py          # Script maestro para ejecutar todos
└── requirements.txt                # Dependencias de Python
```

## Ejercicios Implementados

### 1. Simulación de Restaurante de Comida Rápida
- **Modelo**: Demanda discreta de hamburguesas por hora
- **Distribución**: Discreta (0-6 hamburguesas) con probabilidades específicas
- **Simulaciones**: 100 horas
- **Objetivo**: Estimar utilidad promedio por hora
- **Salidas**: Análisis de ingreso, costo y utilidad

### 2. Simulación de Soldadura de Barras Metálicas
- **Modelo**: Suma de dos variables aleatorias (X1 + X2)
- **Distribuciones**: 
  - X1 ~ Normal(μ=30, σ²=0.81)
  - X2 ~ Erlang(k=2, μ=15)
- **Simulaciones**: 300 barras
- **Objetivo**: Estimar porcentaje de barras que exceden especificación (≤ 50 cm)
- **Salidas**: Análisis de conformidad y distribuciones

### 3. Simulación de Proceso de Dos Etapas
- **Modelo**: Suma de tiempos de procesamiento (t1 + t2)
- **Distribuciones**:
  - t1 ~ Normal(μ=30, σ²=10)
  - t2 ~ Erlang(k=3, μ=20)
- **Simulaciones**: 1000 piezas
- **Objetivo**: Estimar P(Tiempo total > 55 minutos)
- **Salidas**: Análisis de tiempos y convergencia de probabilidades

### 4. Simulación de Inspección de Control de Calidad
- **Modelo**: Inspección aleatoria de cajas con detección de defectos
- **Probabilidades**:
  - P(inspección) = 30%
  - Ítems inspeccionados: 1 (50%), 2 (30%), 3 (20%)
  - P(defecto) = 2%
- **Simulaciones**: 100 cajas
- **Objetivo**: Estimar número promedio de defectos detectados
- **Salidas**: Análisis de efectividad de inspección

### 5. Simulación de Cola M/M/1 en Gasolinera
- **Modelo**: Sistema de cola con un servidor
- **Distribuciones**:
  - Llegadas: Exponencial(λ=10 clientes/hora)
  - Servicio: Exponencial(μ=15 clientes/hora)
- **Simulaciones**: 300 clientes
- **Objetivo**: Calcular métricas de cola (Ls, Lq, Ws, Wq, ρ)
- **Salidas**: Comparación con valores teóricos M/M/1

### 6. Simulación de Selección Aleatoria en Control de Calidad
- **Modelo**: Selección aleatoria de cajas para inspección
- **Probabilidades**:
  - P(selección) = 30%
  - Ítems inspeccionados: 1 (50%), 2 (30%), 3 (20%)
  - P(defecto) = 2%
- **Simulaciones**: 100 cajas
- **Objetivo**: Estimar tasa de defectos encontrados
- **Salidas**: Análisis de probabilidades condicionales

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   # o
   .venv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Ejecutar Todos los Ejercicios

Para ejecutar todos los ejercicios en secuencia:

```bash
python run_all_simulations.py
```

Este script:
- Ejecuta los 6 ejercicios en orden
- Muestra el progreso en consola
- Genera un resumen completo al final
- Lista todos los archivos generados

### Ejecutar Ejercicios Individuales

Para ejecutar un ejercicio específico:

```bash
python exercise_1_restaurant_simulation.py
python exercise_2_welding_simulation.py
python exercise_3_process_simulation.py
python exercise_4_quality_inspection_simulation.py
python exercise_5_queue_simulation.py
python exercise_6_box_selection_simulation.py
```

## Archivos de Salida

Cada ejercicio genera 3 archivos en su carpeta correspondiente:

### 1. Archivo CSV (`problemaX_simulacion.csv`)
- Contiene una fila por entidad simulada (hora, barra, pieza, caja, cliente)
- Incluye todas las variables de entrada (inputs)
- Incluye todas las variables calculadas (outputs)
- Formato compatible con Excel y otras herramientas de análisis

### 2. Archivo Excel (`problemaX_simulacion.xlsx`)
- Contiene la misma tabla de datos que el CSV
- Hoja adicional con estadísticas descriptivas
- **Gráfica incrustada** dentro del libro
- Formato profesional listo para presentación

### 3. Archivo PNG (`problemaX_graficas.png`)
- Imagen de alta resolución (150 DPI)
- Múltiples paneles con análisis visual:
  - Histogramas de distribuciones
  - Gráficas de series de tiempo
  - Comparaciones observado vs teórico
  - Análisis de convergencia

## Salida de Consola

Cada ejercicio imprime en consola:

1. **Parámetros del Modelo**: Distribuciones, probabilidades, constantes
2. **Estadísticas Descriptivas**: Media, desviación estándar, percentiles
3. **Resultados Clave**: Métricas principales según el problema
4. **Validación de Criterios**: Confirmación de cumplimiento de user story
5. **Conclusiones**: Interpretación de resultados y recomendaciones

## Metodología: Spec-Driven Development

Cada ejercicio sigue estrictamente su User Story:

### Componentes de cada User Story:
- **Story**: Descripción del objetivo desde la perspectiva del usuario
- **Acceptance Criteria**: Lista de requisitos verificables
- **Definition of Done**: Criterios para considerar completado el ejercicio

### Validación Automática:
Cada script valida automáticamente que:
- ✓ Las distribuciones sean correctas
- ✓ Los cálculos sigan la lógica especificada
- ✓ Se generen todos los archivos requeridos
- ✓ Los resultados tengan sentido estadístico

## Distribuciones Implementadas

### Discreta Personalizada
- Valores finitos con probabilidades especificadas
- Uso: Demanda de hamburguesas (Ejercicio 1)

### Normal (Gaussiana)
- Parámetros: μ (media), σ² (varianza)
- Uso: Longitudes de barras, tiempos de procesamiento

### Erlang (caso especial de Gamma)
- Parámetros: k (forma), μ (media) → λ = k/μ
- Uso: Tiempos de servicio, procesos en etapas

### Exponencial
- Parámetros: λ (tasa)
- Uso: Tiempos entre llegadas, tiempos de servicio en colas

## Análisis Estadístico

Cada simulación incluye:

### Estadística Descriptiva:
- Media, mediana, moda
- Desviación estándar, varianza
- Mínimo, máximo, rango
- Cuartiles y percentiles

### Estadística Inferencial:
- Intervalos de confianza (cuando aplique)
- Comparación con valores teóricos
- Análisis de convergencia
- Validación de distribuciones

### Visualizaciones:
- Histogramas de frecuencias
- Gráficas de series de tiempo
- Diagramas de dispersión
- Gráficas de barras y pastel
- Análisis de convergencia

## Configuración

### Semillas Aleatorias:
Todos los ejercicios usan `RANDOM_SEED = 42` para reproducibilidad.

### Modificar Parámetros:
Para cambiar parámetros de simulación, edite las constantes al inicio de cada script:

```python
# Ejemplo: exercise_1_restaurant_simulation.py
RANDOM_SEED = 42
NUM_HOURS = 100  # Cambiar para más/menos simulaciones
PRICE_PER_UNIT = 5.00
COST_PER_UNIT = 2.00
```

## Dependencias

```
numpy>=1.24.0       # Generación de números aleatorios y arrays
pandas>=2.0.0       # Manejo de datos tabulares
matplotlib>=3.7.0   # Visualizaciones
scipy>=1.10.0       # Distribuciones estadísticas
statsmodels>=0.14.0 # Análisis estadístico avanzado
openpyxl>=3.1.0     # Lectura/escritura de archivos Excel
```

## Resultados Esperados

### Ejercicio 1:
- Utilidad promedio: ~$9.00 por hora
- Demanda promedio: ~3 hamburguesas/hora
- Distribución observada cercana a la teórica

### Ejercicio 2:
- ~30% de barras no conformes (exceden 50 cm)
- Longitud promedio: ~45 cm
- Alta variabilidad debido a Erlang

### Ejercicio 3:
- ~30% de piezas exceden 55 minutos
- Tiempo promedio: ~50 minutos
- Convergencia estable después de 1000 simulaciones

### Ejercicio 4:
- ~30 cajas inspeccionadas de 100
- Tasa de defectos: ~2%
- Efectividad de detección depende de selección

### Ejercicio 5:
- Utilización del servidor: ~67%
- Tiempo promedio en cola: ~8 minutos
- Métricas convergen a valores teóricos M/M/1

### Ejercicio 6:
- ~30 cajas seleccionadas de 100
- Defectos encontrados dependen de selección aleatoria
- Mayoría de defectos pasan sin detectar

## Solución de Problemas

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: "Permission denied" al crear archivos
Asegúrese de tener permisos de escritura en el directorio del proyecto.

### Gráficas no se muestran
Las gráficas se guardan automáticamente como archivos PNG y en Excel. No se muestran interactivamente.

### Resultados diferentes en cada ejecución
Verifique que `RANDOM_SEED` esté establecida en cada script para reproducibilidad.

## Contacto y Soporte

Para preguntas sobre la implementación:
- Revise el código fuente (totalmente comentado)
- Consulte las User Stories en `simulation_user_stories_v2/`
- Examine los archivos de salida generados

## Licencia

Este proyecto es material educativo para el curso de Simulación.

## Notas Técnicas

- **Reproducibilidad**: Todos los scripts usan semillas aleatorias fijas
- **Eficiencia**: Simulaciones optimizadas con NumPy vectorizado
- **Compatibilidad**: Compatible con Python 3.8+
- **Encoding**: Archivos CSV con UTF-8-SIG para compatibilidad con Excel
- **Calidad**: Código documentado con docstrings en todas las funciones

---

**Desarrollado bajo metodología Spec-Driven Development**  
*Cada ejercicio cumple exactamente con su User Story y criterios de aceptación*
