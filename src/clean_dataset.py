from pathlib import Path
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT_DIR / "retail_store_sales.csv"
PROCESSED_DIR = ROOT_DIR / "data" / "processed"
REPORTS_DIR = ROOT_DIR / "reports"


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATASET_PATH)

    registros_originales = len(df)

    # Copia del conjunto de datos original
    limpio = df.copy()

    # Tratamiento de valores categóricos faltantes
    limpio["Item"] = limpio["Item"].fillna("Unknown")
    limpio["Discount Applied"] = limpio["Discount Applied"].fillna("Unknown")

    # Imputación de Price Per Unit usando la mediana
    mediana_precio = limpio["Price Per Unit"].median()
    limpio["Price Per Unit"] = limpio["Price Per Unit"].fillna(
        mediana_precio
    )

    # Imputación de Quantity usando la mediana
    mediana_cantidad = limpio["Quantity"].median()
    limpio["Quantity"] = limpio["Quantity"].fillna(
        mediana_cantidad
    )

    # Imputación de Total Spent usando Price Per Unit y Quantity
    limpio["Total Spent"] = limpio["Total Spent"].fillna(
        limpio["Price Per Unit"] * limpio["Quantity"]
    )

    # Conversión de fecha
    limpio["Transaction Date"] = pd.to_datetime(
        limpio["Transaction Date"],
        errors="coerce"
    )

    # Guardar dataset limpio
    output_path = PROCESSED_DIR / "retail_store_sales_clean.csv"
    limpio.to_csv(output_path, index=False)

    # Crear reporte de limpieza
    reporte = pd.DataFrame({
        "Registros originales": [registros_originales],
        "Registros finales": [len(limpio)],
        "Valores nulos originales": [df.isna().sum().sum()],
        "Valores nulos finales": [limpio.isna().sum().sum()],
        "Duplicados originales": [df.duplicated().sum()],
        "Duplicados finales": [limpio.duplicated().sum()]
    })

    reporte.to_csv(
        REPORTS_DIR / "reporte_limpieza.csv",
        index=False
    )

    print("=== LIMPIEZA COMPLETADA ===")
    print(f"Registros originales: {registros_originales}")
    print(f"Registros finales: {len(limpio)}")
    print(f"Nulos originales: {df.isna().sum().sum()}")
    print(f"Nulos finales: {limpio.isna().sum().sum()}")
    print(f"Archivo generado: {output_path}")
    print("Reporte generado: reports/reporte_limpieza.csv")


if __name__ == "__main__":
    main()