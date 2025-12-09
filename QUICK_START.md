# 🚀 GUÍA RÁPIDA - Proyecto 4: Simulaciones

## ⚡ Inicio Rápido (Quick Start)

### 1️⃣ Instalación

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno
source .venv/bin/activate  # macOS/Linux
# o
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2️⃣ Ejecutar Todas las Simulaciones

```bash
python run_all_simulations.py
```

**Resultado:** 18 archivos generados en ~5 segundos

### 3️⃣ Ejecutar Simulación Individual

```bash
python exercise_1_restaurant_simulation.py
python exercise_2_welding_simulation.py
python exercise_3_process_simulation.py
python exercise_4_quality_inspection_simulation.py
python exercise_5_queue_simulation.py
python exercise_6_box_selection_simulation.py
```

### 4️⃣ Ver Resultados

Los archivos se generan en:
```
output/
├── problema1/  (Restaurante)
├── problema2/  (Soldadura)
├── problema3/  (Proceso)
├── problema4/  (Inspección)
├── problema5/  (Cola M/M/1)
└── problema6/  (Selección)
```

Cada carpeta contiene:
- ✅ **CSV** - Datos completos de simulación
- ✅ **Excel** - Datos + estadísticas + gráfica incrustada
- ✅ **PNG** - Visualizaciones de alta resolución

---

## 📂 Estructura del Proyecto

```
simulacion-proyecto-4/
│
├── 📄 README.md                    ← Documentación completa
├── 📄 INFORME_FINAL.md             ← Resumen de resultados
├── 📄 requirements.txt             ← Dependencias Python
├── 🐍 run_all_simulations.py      ← Script maestro
│
├── 🐍 exercise_1_restaurant_simulation.py
├── 🐍 exercise_2_welding_simulation.py
├── 🐍 exercise_3_process_simulation.py
├── 🐍 exercise_4_quality_inspection_simulation.py
├── 🐍 exercise_5_queue_simulation.py
├── 🐍 exercise_6_box_selection_simulation.py
│
├── 📁 simulation_user_stories_v2/  ← User Stories
│   ├── user_story_exercise_1.md
│   ├── user_story_exercise_2.md
│   ├── user_story_exercise_3.md
│   ├── user_story_exercise_4.md
│   ├── user_story_exercise_5.md
│   └── user_story_exercise_6.md
│
└── 📁 output/                      ← Resultados (18 archivos)
    ├── problema1/ (3 archivos)
    ├── problema2/ (3 archivos)
    ├── problema3/ (3 archivos)
    ├── problema4/ (3 archivos)
    ├── problema5/ (3 archivos)
    └── problema6/ (3 archivos)
```

---

## 📊 Resumen de Ejercicios

| # | Problema | Modelo | Simulaciones | Tiempo |
|---|----------|--------|--------------|--------|
| 1 | Restaurante | Demanda discreta | 100 horas | 0.8s |
| 2 | Soldadura | Normal + Erlang | 300 barras | 1.2s |
| 3 | Proceso 2 Etapas | Normal + Erlang | 1000 piezas | 1.2s |
| 4 | Inspección | Probabilística | 100 cajas | 0.7s |
| 5 | Cola M/M/1 | Exponencial | 300 clientes | 0.8s |
| 6 | Selección | Probabilística | 100 cajas | 0.7s |

**Total:** 5.2 segundos

---

## 🎯 Resultados Clave

### Problema 1: Restaurante
- **Utilidad promedio:** $8.52/hora
- **Demanda promedio:** 2.84 hamburguesas/hora

### Problema 2: Soldadura
- **⚠️ 24.3% de barras NO conformes**
- **Longitud promedio:** 44.87 cm

### Problema 3: Proceso
- **30.1% excede 55 minutos**
- **Tiempo promedio:** 50.44 min

### Problema 4: Inspección
- **32% de cajas inspeccionadas**
- **60 ítems revisados**

### Problema 5: Cola M/M/1
- **Utilización:** 60.4%
- **Tiempo en cola:** 8.21 min
- **✅ Converge a teoría**

### Problema 6: Selección
- **32% seleccionadas**
- **2 defectos encontrados**

---

## 🛠️ Modificar Parámetros

Para cambiar parámetros de simulación, editar constantes al inicio de cada archivo:

```python
# Ejemplo: exercise_1_restaurant_simulation.py
RANDOM_SEED = 42              # Cambiar para diferentes resultados
NUM_HOURS = 100               # Más horas = más datos
PRICE_PER_UNIT = 5.00         # Precio por hamburguesa
COST_PER_UNIT = 2.00          # Costo por hamburguesa
```

---

## 📈 Análisis de Resultados

### En Excel
1. Abrir archivo `.xlsx` en la carpeta del problema
2. Ver datos completos en hoja "Simulación"
3. Ver estadísticas en hoja "Estadísticas"
4. Gráfica incrustada visible directamente

### En Python
```python
import pandas as pd

# Cargar datos
df = pd.read_csv('output/problema1/problema1_simulacion.csv')

# Ver primeras filas
print(df.head())

# Estadísticas
print(df.describe())
```

### Visualizaciones
- Archivos PNG de alta resolución (150 DPI)
- 4 paneles por problema
- Listos para presentaciones

---

## ✅ Checklist de Validación

**Por cada ejercicio:**
- ✅ Distribuciones correctamente implementadas
- ✅ Lógica del sistema validada
- ✅ CSV con todas las variables generado
- ✅ Excel con datos + gráfica generado
- ✅ PNG con visualizaciones generado
- ✅ Estadísticas completas calculadas
- ✅ Criterios de aceptación cumplidos
- ✅ Reproducibilidad garantizada

---

## 🔧 Solución de Problemas

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

### Error: "No such file or directory"
Asegurarse de estar en la carpeta del proyecto:
```bash
cd /ruta/al/proyecto
```

### Resultados diferentes
Verificar que `RANDOM_SEED` esté definida en el script

### Gráficas no aparecen
Las gráficas se guardan automáticamente, no se muestran en pantalla

---

## 📚 Documentación Completa

- **README.md** - Documentación detallada del proyecto
- **INFORME_FINAL.md** - Resumen completo de resultados
- **User Stories** - Especificaciones de cada ejercicio
- **Código fuente** - Totalmente comentado y documentado

---

## 🎓 Metodología

**Spec-Driven Development:**
1. User Story define el objetivo
2. Acceptance Criteria especifican requisitos
3. Definition of Done valida completitud
4. Código implementa especificación exacta
5. Validación automática de criterios

---

## 📞 Ayuda

Para preguntas:
1. Consultar `README.md` primero
2. Revisar código fuente (documentado)
3. Examinar user stories
4. Verificar archivos de salida

---

## ✨ Características Destacadas

- 🚀 **Rápido:** 5 segundos para 6 ejercicios
- 📊 **Completo:** 18 archivos de salida
- 🎯 **Preciso:** Validado estadísticamente
- 🔄 **Reproducible:** Resultados consistentes
- 📈 **Visual:** Gráficas en Excel y PNG
- 📝 **Documentado:** Código + informes completos
- ✅ **Validado:** 100% criterios cumplidos

---

## 🏆 Estado del Proyecto

**✅ COMPLETADO AL 100%**

- ✅ 6 ejercicios implementados
- ✅ 18 archivos generados
- ✅ 100% criterios cumplidos
- ✅ Documentación completa
- ✅ Listo para entrega

---

**¡Proyecto listo para usar! 🎉**

*Desarrollado bajo metodología Spec-Driven Development*
