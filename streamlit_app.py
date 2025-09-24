# Placeholder para la aplicación Streamlit
import streamlit as st

st.title("Big Data Storage Lab - <apellido>")
st.write("Visualización de KPIs en tiempo real.")

import io
import pandas as pd
import streamlit as st
from src.transform import normalize_columns, to_silver
from src.validate import basic_checks
from src.ingest import tag_lineage, concat_bronze

# --- Configuración general ---
st.set_page_config(page_title="Big Data Storage Lab", layout="wide")
st.title("📂 Big Data Storage Lab – Bronze/Silver Demo")

# --- Barra lateral: configuración de columnas origen ---
st.sidebar.header("Configuración de columnas de origen")
date_col = st.sidebar.text_input("Columna origen para fecha", value="date")
partner_col = st.sidebar.text_input("Columna origen para partner", value="partner")
amount_col = st.sidebar.text_input("Columna origen para amount", value="amount")
col_mapping = {
    date_col: "date",
    partner_col: "partner",
    amount_col: "amount",
}

# --- Subida de archivos ---
uploaded_files = st.file_uploader(
    "Sube uno o varios CSV heterogéneos",
    type=["csv"],
    accept_multiple_files=True
)

bronze_frames = []

if uploaded_files:
    for f in uploaded_files:
        st.write(f"Procesando archivo: **{f.name}**")
        # Intentar leer con utf-8, fallback a latin-1
        try:
            df = pd.read_csv(f)
        except UnicodeDecodeError:
            f.seek(0)
            df = pd.read_csv(f, encoding="latin-1")

        # Normalizar y etiquetar linaje
        df_norm = normalize_columns(df, col_mapping)
        df_tag = tag_lineage(df_norm, source_name=f.name)
        bronze_frames.append(df_tag)

    # Concatenar en bronze unificado
    bronze = concat_bronze(bronze_frames)

    st.subheader("📋 Datos Bronze (unificados)")
    st.dataframe(bronze.head(50), use_container_width=True)

    # Validaciones
    errors = basic_checks(bronze)
    if errors:
        st.error("❌ Errores de validación encontrados:")
        for e in errors:
            st.write(f"- {e}")
    else:
        st.success("✅ Validaciones superadas")

        # Derivar Silver
        silver = to_silver(bronze)

        st.subheader("🥈 Datos Silver (aggregados por partner y mes)")
        st.dataframe(silver, use_container_width=True)

        # KPIs simples
        st.markdown("### 📊 KPIs")
        total_amount = silver["total_amount"].sum()
        num_partners = silver["partner"].nunique()
        num_months = silver["month"].nunique()
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Amount (EUR)", f"{total_amount:,.2f}")
        col2.metric("Partners únicos", num_partners)
        col3.metric("Meses registrados", num_months)

        # Gráfico de barras (mes vs total amount)
        chart_df = silver.groupby("month", as_index=False)["total_amount"].sum()
        st.bar_chart(chart_df.set_index("month"))

        # Botones de descarga
        st.markdown("### 💾 Descargas")
        bronze_csv = bronze.to_csv(index=False).encode("utf-8")
        silver_csv = silver.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Descargar Bronze CSV",
            bronze_csv,
            file_name="bronze.csv",
            mime="text/csv"
        )
        st.download_button(
            "Descargar Silver CSV",
            silver_csv,
            file_name="silver.csv",
            mime="text/csv"
        )
else:
    st.info("👆 Sube uno o varios archivos CSV para comenzar el procesamiento.")
