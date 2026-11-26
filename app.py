import pandas as pd
import plotly.express as px
import streamlit as st
from src.analisis import analizar_dataframe, REQUIRED_COLUMNS

st.set_page_config(page_title="Análisis electoral Bolivia 2019",page_icon="📊",layout="wide")
st.title("Análisis estadístico electoral · Bolivia 2019")
st.caption("Validación de datos y alertas exploratorias por mesa.")
with st.sidebar:
    st.header("Cargar datos")
    file=st.file_uploader("Archivo CSV o Excel",type=["csv","xlsx"])
    st.markdown("Columnas obligatorias")
    st.code(", ".join(REQUIRED_COLUMNS))
    st.info("Una fila por mesa. Añade columnas opcionales con prefijo votos_, por ejemplo votos_MAS.")
if file is None:
    st.info("Carga un CSV o XLSX de resultados por mesa para comenzar.")
    st.markdown("- Detecta códigos duplicados y datos faltantes.\n- Comprueba totales de votos.\n- Revisa porcentajes y valores estadísticos atípicos.")
    st.warning("Una alerta no demuestra fraude. Contrasta cada caso con el acta original y fuentes documentales.")
    st.stop()
try:
    raw=pd.read_excel(file) if file.name.lower().endswith(".xlsx") else pd.read_csv(file)
    data,alerts,summary=analizar_dataframe(raw)
except Exception as e:
    st.error(f"No se pudo procesar el archivo: {e}")
    st.stop()
a,b,c,d=st.columns(4)
a.metric("Mesas",f"{summary['mesas_analizadas']:,}")
b.metric("Alertas",f"{summary['alertas']:,}")
c.metric("Alertas altas",f"{summary['alertas_altas']:,}")
d.metric("Atípicos",f"{summary['alertas_revision']:,}")
st.subheader("Resumen por departamento")
dept=data.groupby("departamento",dropna=False).agg(mesas=("codigo_mesa","size"),inscritos=("inscritos","sum"),emitidos=("emitidos","sum")).reset_index()
dept["participacion_pct"]=dept.emitidos.div(dept.inscritos.replace(0,pd.NA))*100
st.dataframe(dept,use_container_width=True,hide_index=True)
st.plotly_chart(px.bar(dept,x="departamento",y="participacion_pct",title="Participación calculada por departamento (%)"),use_container_width=True)
st.subheader("Alertas para revisión")
if alerts.empty: st.success("No se detectaron alertas con las reglas activas. Esto no certifica las actas.")
else:
    st.dataframe(alerts,use_container_width=True,hide_index=True)
    st.download_button("Descargar alertas CSV",alerts.to_csv(index=False).encode("utf-8-sig"),"alertas_elecciones_2019.csv","text/csv")
st.subheader("Datos procesados")
st.dataframe(data,use_container_width=True,hide_index=True)
st.download_button("Descargar datos analizados",data.to_csv(index=False).encode("utf-8-sig"),"resultados_2019_analizados.csv","text/csv")
st.caption("Conserva originales, URL, fecha de descarga, versión y hash de cada fuente.")
