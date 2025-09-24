# Validación de calidad de datos
def validate_data(df):
    pass
import pandas as pd
from pandas import DataFrame
from typing import List

def basic_checks(df: DataFrame) -> List[str]:
    """
    Devuelve lista de errores básicos:
    - columnas canónicas presentes
    - amount numérico y >= 0
    - date en datetime
    """
    errors: List[str] = []
    required_cols = {"date", "partner", "amount"}

    # Verificar columnas presentes
    missing = required_cols - set(df.columns)
    if missing:
        errors.append(f"Faltan columnas: {', '.join(missing)}")

    # Verificar tipos
    if "amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            errors.append("amount no es numérico")
        elif (df["amount"] < 0).any():
            errors.append("amount contiene valores negativos")

    if "date" in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df["date"]):
            errors.append("date no es datetime")

    return errors
