# Diccionario de Datos
> Definir aquí cada columna, tipo de dato, descripción y origen.

# 📊 Diccionario de Datos – Esquema Canónico

## Esquema Canónico
| Campo   | Tipo        | Formato / Unidad | Descripción |
|---------|-------------|------------------|-------------|
| `date`  | `DATE`      | `YYYY-MM-DD`     | Fecha de la transacción. |
| `partner` | `STRING`  | texto libre      | Nombre del socio/cliente/proveedor. |
| `amount` | `FLOAT`    | Euros (EUR)      | Importe monetario de la transacción. |

---

## Mapeos de Origen → Canónico
Ejemplos de cómo distintas fuentes se estandarizan al esquema común:

| Origen | Columna Original | Transformación | Campo Canónico |
|-------|------------------|-----------------|-----------------|
| ERP A | `transaction_date` | Convertir a `YYYY-MM-DD` | `date` |
| ERP A | `vendor_name`      | Trim/Uppercase | `partner` |
| ERP A | `total_eur`        | Cast a float   | `amount` |
| CSV B | `fecha`            | Parse a ISO8601 | `date` |
| CSV B | `cliente`          | Renombrar      | `partner` |
| CSV B | `importe`          | Cast a float   | `amount` |

> ⚠️ Todos los orígenes deben cumplir con la codificación UTF-8 y separador `,` antes de la normalización.

---

## Notas
- **Moneda:** siempre en EUR, sin símbolo.  
- **Nulos:** no se admiten en `date` ni `amount`.  
- **Duplicados:** las combinaciones `date + partner + amount` deben ser únicas o justificadas.
