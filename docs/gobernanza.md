# Gobernanza de Datos
> Normas de calidad, linaje, roles y políticas de acceso.
# 🛡️ Gobernanza de Datos

## 1. Origen y Linaje
- **Fuentes**: múltiples CSVs de ERPs, sistemas financieros y hojas de cálculo externas.
- **Flujo**:  
  `raw` → validación → `bronze` → normalización → `silver` → KPIs/`gold`.
- Cada dataset incluye metadatos de fecha de ingesta, usuario de carga y hash de control.

## 2. Validaciones Mínimas
- Formato de fecha (`YYYY-MM-DD`) obligatorio.
- Tipado estricto (`partner` texto, `amount` float).
- Control de nulos: rechazo o imputación documentada.
- Chequeo de duplicados y valores fuera de rango (ej. `amount` negativo).

## 3. Política de Mínimos Privilegios
- Acceso **solo al nivel necesario**:
  - **Raw/Bronze**: únicamente equipo de Ingeniería de Datos.
  - **Silver/Gold**: acceso de lectura para analistas y negocio.
- Uso de **roles** y **tokens temporales** para conexiones externas.

## 4. Trazabilidad
- Registro de cada transformación en logs versionados.
- Hash de cada archivo en `raw` para verificar integridad.
- Metadatos en cada tabla/capa: fecha de carga, usuario, versión de esquema.

## 5. Roles
| Rol                       | Responsabilidad |
|----------------------------|------------------|
| **Data Engineer**          | Ingesta, validación y normalización de datos. |
| **Data Analyst / BI**      | Consumo de `silver/gold` y cálculo de KPIs. |
| **Data Steward**           | Supervisión de calidad, linaje y cumplimiento. |
| **Administrador de Plataforma** | Gestión de accesos y seguridad. |

---

## Recomendaciones
- Implementar **auditorías periódicas** para revisar accesos.
- Mantener un **catálogo de datos** actualizado.
- Automatizar pruebas de calidad antes de cada despliegue.
