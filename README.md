# Cursos

Repositorio de materiales para formación en analítica de datos e inteligencia artificial.
Incluye cursos, notebooks, datasets, modelos entrenados y artefactos de apoyo.

## Estructura general del repositorio

```text
Cursos/
├── 00 - Data/                                        # datasets de práctica por temática
│   ├── 00 - Basicos/
│   ├── 01 - RRHH/
│   ├── 02 - SC/
│   ├── 03 - NLP/
│   └── 04 - Time series/
├── 01 - Análisis predictivo para toma de decisiones RRHH/
├── 02 - IA4SC/
├── 03 - NLP/
├── 04 - Gen-AI/
├── LICENSE
└── README.md
```

## Inventario de recursos (resumen)

| Carpeta | Tipo de contenido | Cantidad aprox. |
|---|---|---:|
| `00 - Data` | Datasets base (CSV/XLSX/JPEG) | 34 archivos |
| `01 - Análisis predictivo para toma de decisiones RRHH` | Notebooks de analítica predictiva en RRHH | 4 archivos |
| `02 - IA4SC` | Curso principal de IA aplicada, modelos y resultados | 72 archivos |
| `03 - NLP` | Notebooks complementarios de NLP | 2 archivos |
| `04 - Gen-AI` | Apps y notebook de IA generativa | 3 archivos |

---

## Inventario detallado de `00 - Data`

### 00 - Basicos (9 archivos)
**Objetivo:** práctica inicial de manipulación y visualización de datos.

- `Dataset_Proyectos_Visualizacion_300_Registros.csv`
- `apartamentos.csv`
- `dataset_operaciones.csv`
- `ventas.csv`
- `global_superstore_2016.xlsx`
- `Space_Titanic/train.csv`
- `Space_Titanic/test.csv`
- `ciclorruta-avenida-boyaca_0.jpeg`
- `ejemplo_caja.jpeg`

### 01 - RRHH (4 archivos)
**Objetivo:** clasificación/predicción en personas y talento humano.

- `HR-Employee-Attrition.csv`
- `iris_human_resources.csv`
- `HR Analytics Classification/train_promotion.csv`
- `HR Analytics Classification/test_promotion.csv`

### 02 - SC (Supply Chain) (12 archivos)
**Objetivo:** casos de logística, inventarios y pronóstico de demanda.

- `iris_evaluacion_proveedores.csv`
- `Casos1.csv`
- `Beautty SC/supply_chain_data.csv`
- `Simple_product_demand/Historical Product Demand.csv`
- `Demand forecasting/train.csv`
- `Demand forecasting/test.csv`
- `Demand forecasting/sample_submission.csv`
- `Optimizacion Inventarios/Data_demanda.csv`
- `Optimizacion Inventarios/Data_pedidos.csv`
- `Inventory OPtimziation for Retail/demand_forecasting.csv`
- `Inventory OPtimziation for Retail/inventory_monitoring.csv`
- `Inventory OPtimziation for Retail/pricing_optimization.csv`

### 03 - NLP (5 archivos)
**Objetivo:** clasificación de texto y análisis de sentimiento.

- `amazon_reviews.csv`
- `sample_amazon_reviews.csv`
- `IMDB_Dataset.csv`
- `twitter.csv`
- `reportes_logisticos_200.csv`

### 04 - Time series (4 archivos)
**Objetivo:** ejercicios de series temporales y forecasting.

- `Electric_Production.csv`
- `daily-minimum-temperatures-in-me.csv`
- `monthly-beer-production-in-austr.csv`
- `sales-of-shampoo-over-a-three-ye.csv`

---

## Descripción de cursos y recursos por carpeta

### 01 - Análisis predictivo para toma de decisiones RRHH
Curso enfocado en análisis exploratorio, clasificación y modelos de regresión aplicados a RRHH.

**Contenido principal (4 notebooks):**
1. `Notebook 1 AED y clasificación.ipynb`
2. `Notebook 2 Regresion Lineal.ipynb`
3. `Notebook 3 Comparación y Optimización de Modelos de Regresión.ipynb`
4. `Notebook 4 Aplicación de IA para promocion de cargos en una compañia.ipynb`

### 02 - IA4SC
Curso de IA aplicada a supply chain / operaciones, con notebooks de ML, NLP, CV, inventarios y ruteo.

**Incluye:**
- Ruta de aprendizaje en notebooks (`Notebook 01` a `Notebook 08`, incluyendo 5A y 5B).
- Carpeta `Ejercicios/` con versiones prácticas de notebooks y artefactos (`.pkl`, `yolov8n.pt`).
- Carpeta `Models/` con modelos serializados para NLP.
- Carpetas `runs/` y `cache/` con salidas de entrenamiento y ejecución.
- Recursos auxiliares (`.html` de mapas/rutas, `.pt` de visión por computador, `.csv` de predicciones).

### 03 - NLP
Módulo complementario de procesamiento de lenguaje natural.

**Contenido principal:**
- `Notebook 01 Clasificación de reseñars.ipynb`
- `HF-SQUAD.ipynb`

### 04 - Gen-AI
Materiales introductorios de IA generativa y aplicaciones.

**Contenido principal:**
- `Amazon_bedrock.ipynb`
- `app.py`
- `app_imagen.py`

---

## Cómo usar este repositorio

1. Inicia por los datasets de `00 - Data` según el tema del curso.
2. Sigue los notebooks de cada curso en orden numérico.
3. Reutiliza modelos y salidas ya entrenadas cuando aplique (`02 - IA4SC/Models`, `02 - IA4SC/runs`).

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta [`LICENSE`](LICENSE).
