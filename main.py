from pathlib import Path
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASET_PATH = Path(__file__).resolve().parent / "retail_store_sales.csv"

def main():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {DATASET_PATH}"
        )

    df = pd.read_csv(DATASET_PATH)

    print("=== INFORMACIÓN DEL DATASET ===")
    print(f"Ruta: {DATASET_PATH}")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

    print("\n=== NOMBRES DE LAS COLUMNAS ===")
    print(df.columns.tolist())

    print("\n=== PRIMERAS 5 FILAS ===")
    print(df.head())

    print("\n=== TIPOS DE DATOS ===")
    print(df.dtypes)

    print("\n=== VALORES NULOS ===")
    print(df.isna().sum())

    print("\n=== FILAS DUPLICADAS ===")
    print(df.duplicated().sum())


if __name__ == "__main__":
    main()