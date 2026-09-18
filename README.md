# ED.01.02. Git, GitHub y reproducibilidad

## Descripción

Este proyecto realiza un proceso de exploración, diagnóstico y limpieza
de un conjunto de datos de ventas de una tienda.

El objetivo es aplicar buenas prácticas de análisis de datos, organización
de archivos, reproducibilidad y control de versiones mediante Git y GitHub.

## Dataset

El conjunto de datos contiene información sobre:

- Identificación de transacciones.
- Clientes.
- Categorías de productos.
- Precios.
- Cantidades.
- Total de compra.
- Métodos de pago.
- Ubicación de la venta.
- Fecha de transacción.
- Descuentos aplicados.

## Análisis inicial

El dataset contiene:

- 12,575 registros.
- 11 columnas.
- 0 registros duplicados.
- Valores faltantes en Item.
- Valores faltantes en Price Per Unit.
- Valores faltantes en Quantity.
- Valores faltantes en Total Spent.
- Valores faltantes en Discount Applied.

No se encontraron valores menores o iguales a cero en las columnas numéricas
revisadas y tampoco se encontraron fechas inválidas.

## Limpieza de datos

Se aplicaron los siguientes procedimientos:

1. Reemplazo de valores faltantes en Item por `Unknown`.
2. Reemplazo de valores faltantes en Discount Applied por `Unknown`.
3. Imputación de precios faltantes utilizando la mediana.
4. Imputación de cantidades faltantes utilizando la mediana.
5. Cálculo de Total Spent cuando faltaba utilizando el precio y la cantidad.
6. Conversión de la columna Transaction Date a formato de fecha.
7. Exportación del dataset limpio.

## Estructura del proyecto

```text
ED.01.02.-Git-GitHub-y-reproducibilidad/
│
├── data/
│   └── processed/
│       └── retail_store_sales_clean.csv
│
├── reports/
│   ├── calidad_datos.csv
│   ├── combinaciones_nulos.csv
│   ├── diagnostico_avanzado.csv
│   └── reporte_limpieza.csv
│
├── src/
│   ├── main.py
│   ├── clean_data.py
│   └── clean_dataset.py
│
├── retail_store_sales.csv
├── analisis_inicial.txt
├── resumen_estadistico.txt
├── reporte_nulos.csv
├── requirements.txt
├── .gitignore
└── README.md