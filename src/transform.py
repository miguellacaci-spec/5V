# Normalización y generación de capas bronze/silver
def transform_data(df):
    pass

import pandas as pd
from pandas import DataFrame
from typing import Dict

def normalize_columns(df: DataFrame, mapping: Dict[str, str]) -> DataFrame:
    """
    Renombra columnas según mapping (origen→canónico), normaliza formatos y limpia valores.
    - date: a datetime (UTC, ISO)
    - amount: quita € y comas europeas, convierte a float
    - partner: trim espacios
    """
    # Renombrar columnas
    df = df.rename(columns=mapping)

    # Normalizar columna date
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True).dt.tz_convert(None)

    # Normalizar amount (quita símbolos y comas)
    if "amount" in df.columns:
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace(r"[€\s]", "", regex=True)
            .str.replace(".", "", regex=False)  # eliminar separador de miles
            .str.replace(",", ".", regex=False)  # cambiar coma decimal a punto
        )
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Limpiar partner
    if "partner" in df.columns:
        df["partner"] = df["partner"].astype(str).str.strip()

    return df

def to_silver(bronze: DataFrame) -> DataFrame:
    """
    Agrega amount por partner y mes.
    - month: primer día del mes en formato timestamp
    """
    if "date" not in bronze.columns:
        raise ValueError("La columna 'date' es obligatoria en bronze.")
    bronze["month"] = bronze["date"].dt.to_period("M").dt.to_timestamp()
    silver = (
        bronze.groupby(["partner", "month"], as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
    )
    return silver
