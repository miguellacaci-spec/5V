# 5V
# 🧠 Prompts de Reflexión – Respuestas del Alumno

Responde brevemente a cada pregunta en el espacio indicado.

1. **V dominante hoy y V dominante si se duplica el tráfico**  
   - Respuesta:  
     ```
    Hoy domina **Volumen**, porque el reto principal es almacenar y manejar la cantidad creciente de archivos.  
Si el tráfico se duplica, pasaría a dominar **Velocidad**, ya que la ingestión y el procesamiento en tiempo razonable se vuelven críticos.  
La justificación es que más tráfico exige tiempos de procesamiento más cortos para mantener la misma experiencia de usuario.

     ```

2. **Trade-off elegido (p.ej., más compresión vs CPU)**  
   - Respuesta:  
     ```
   Elegí mayor compresión en los datasets (Parquet) para reducir almacenamiento.  
Esto implica mayor uso de CPU en lectura/escritura, pero lo mediré comparando tiempos de carga y tamaño de archivo frente a CSV en pruebas controladas.  
El ahorro en espacio justifica el mayor costo computacional.
     ```

3. **Inmutable + linaje y veracidad**  
   - Respuesta:  
     ```
  Mantener los datos inmutables y registrar su linaje asegura que cada transformación sea trazable y verificable, aumentando la veracidad.  
El coste técnico es mayor almacenamiento (versionado) y metadatos adicionales para registrar cada paso del flujo.  
Este coste se asume para garantizar auditoría y confianza en los datos.
     ```

4. **KPI principal y SLA del dashboard**  
   - Respuesta:  
     ```
 KPI principal: monto total mensual (partner × mes).  
SLA: actualización completa en ≤5 minutos tras subir nuevos archivos.  
Permite decisiones comerciales rápidas sin requerir latencias de tiempo real, equilibrando costo y velocidad.

     ```

5. **Riesgo principal del diseño y mitigación técnica**  
   - Respuesta:  
     ```
Riesgo: archivos de origen con columnas inconsistentes que rompan la unificación.  
Mitigación: pipeline de normalización con validaciones automáticas (basic_checks) que rechace o corrija archivos antes de procesarlos.  
Esto asegura integridad y evita errores en las capas silver/gold.
     ```
