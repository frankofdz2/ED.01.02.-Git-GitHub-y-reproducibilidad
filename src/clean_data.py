from pathlib import Path
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT_DIR / "retail_store_sales.csv"
REPORTS_DIR = ROOT_DIR / "reports"


def main():
    df = pd.read_csv(DATASET_PATH)

    REPORTS_DIR.mkdir(exist_ok=True)

    print("=== DIAGNÓSTICO AVANZADO ===")

    # 1. Valores nulos por columna
    print("\n=== VALORES NULOS ===")
    print(df.isna().sum())

    # 2. Combinaciones de valores nulos
    columnas_numericas = [
        "Price Per Unit",
        "Quantity",
        "Total Spent",
    ]

    combinaciones = (
        df[columnas_numericas]
        .isna()
        .value_counts()
        .reset_index(name="Cantidad")
    )

    combinaciones.to_csv(
        REPORTS_DIR / "combinaciones_nulos.csv",
        index=False,
    )

    print("\n=== COMBINACIONES DE NULOS NUMÉRICOS ===")
    print(combinaciones.to_string(index=False))

    # 3. Valores fuera de rango
    print("\n=== VALORES FUERA DE RANGO ===")

    for columna in ["Price Per Unit", "Quantity", "Total Spent"]:
        valores_invalidos = (df[columna] <= 0).sum()
        print(f"{columna}: {valores_invalidos} valores menores o iguales a cero")

    # 4. Fechas inválidas
    fechas = pd.to_datetime(
        df["Transaction Date"],
        errors="coerce",
    )

    print("\n=== FECHAS ===")
    print(f"Fechas inválidas: {fechas.isna().sum()}")
    print(f"Fecha más antigua: {fechas.min()}")
    print(f"Fecha más reciente: {fechas.max()}")

    # 5. Valores categóricos
    print("\n=== CATEGORÍAS ===")
    print(df["Category"].value_counts(dropna=False))

    print("\n=== MÉTODOS DE PAGO ===")
    print(df["Payment Method"].value_counts(dropna=False))

    print("\n=== UBICACIONES ===")
    print(df["Location"].value_counts(dropna=False))

    # 6. Guardar diagnóstico general
    diagnostico = pd.DataFrame(
        {
            "Tipo de dato": df.dtypes.astype(str),
            "Valores nulos": df.isna().sum(),
            "Porcentaje nulos": (df.isna().mean() * 100).round(2),
            "Valores únicos": df.nunique(dropna=True),
        }
    )

    diagnostico.to_csv(
        REPORTS_DIR / "diagnostico_avanzado.csv"
    )

    print("\n=== DIAGNÓSTICO GUARDADO ===")
    print("Archivos guardados en la carpeta reports.")


if __name__ == "__main__":
    main()