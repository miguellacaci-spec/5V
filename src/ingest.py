# Lógica de ingesta de CSVs heterogéneos
def ingest_data(input_path: str):
    pass
import pandas as pd
from pandas import DataFrame
from typing import List
from datetime import datetime, timezone

def tag_lineage(df: DataFrame, source_name: str) -> DataFrame:
    """
    Añade columnas de linaje:
    - source_file: nombre del archivo origen
    - ingested_at: timestamp UTC ISO
    """
    df = df.copy()
    df["source_file"] = source_name
    df["ingested_at"] = datetime.now(timezone.utc).isoformat()
    return df

def concat_bronze(frames: List[DataFrame]) -> DataFrame:
    """
    Concatena múltiples DataFrames al esquema estándar:
    date, partner, amount, source_file, ingested_at
    """
    if not frames:
        return pd.DataFrame(columns=["date", "partner", "amount", "source_file", "ingested_at"])
    bronze = pd.concat(frames, ignore_index=True)
    # Reordenar columnas al esquema deseado
    cols = ["date", "partner", "amount", "source_file", "ingested_at"]
    return bronze[cols]
