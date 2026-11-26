"""Motor estadístico: las alertas no determinan fraude."""
import numpy as np
import pandas as pd

REQUIRED_COLUMNS = ["codigo_mesa","departamento","municipio","inscritos","emitidos","validos","blancos","nulos"]
COUNT_COLUMNS = ["inscritos","emitidos","validos","blancos","nulos"]
PARTY_PREFIX = "votos_"

def preparar_datos(df):
    data=df.copy()
    data.columns=[str(c).strip().lower() for c in data.columns]
    missing=[c for c in REQUIRED_COLUMNS if c not in data.columns]
    if missing: raise ValueError("Faltan columnas obligatorias: "+", ".join(missing))
    for c in ["codigo_mesa","departamento","municipio"]:
        data[c]=data[c].astype("string").str.strip()
    for c in COUNT_COLUMNS+[c for c in data.columns if c.startswith(PARTY_PREFIX)]:
        data[c]=pd.to_numeric(data[c],errors="coerce")
    return data

def _alert(out, idx, code, severity, rule, detail):
    out.append({"fila":int(idx)+1,"codigo_mesa":str(code),"severidad":severity,"regla":rule,"detalle":detail})

def _mad_outliers(series, threshold=3.5):
    x=pd.to_numeric(series,errors="coerce")
    med=x.median(); mad=(x-med).abs().median()
    if pd.isna(mad) or mad==0: return pd.Series(False,index=series.index)
    return (0.6745*(x-med)/mad).abs()>threshold

def analizar_dataframe(raw):
    data=preparar_datos(raw); alerts=[]
    party=[c for c in data.columns if c.startswith(PARTY_PREFIX)]
    dup=data["codigo_mesa"].duplicated(keep=False)
    for idx in data.index[dup]:
        _alert(alerts,idx,data.at[idx,"codigo_mesa"],"ALTA","CODIGO_DUPLICADO","El código aparece más de una vez.")
    for idx,row in data.iterrows():
        code=row["codigo_mesa"]
        for col in COUNT_COLUMNS+party:
            v=row[col]
            if pd.isna(v): _alert(alerts,idx,code,"ALTA","DATO_FALTANTE",f"{col} está vacío o no es numérico.")
            elif v<0: _alert(alerts,idx,code,"ALTA","VALOR_NEGATIVO",f"{col} contiene un valor negativo.")
            elif not float(v).is_integer(): _alert(alerts,idx,code,"MEDIA","VALOR_NO_ENTERO",f"{col} debería ser entero.")
        vals=[row[c] for c in COUNT_COLUMNS]
        if not any(pd.isna(v) for v in vals):
            if row.emitidos>row.inscritos:
                _alert(alerts,idx,code,"ALTA","EMITIDOS_MAYOR_INSCRITOS","Emitidos supera a inscritos.")
            total=row.validos+row.blancos+row.nulos
            if total!=row.emitidos:
                _alert(alerts,idx,code,"ALTA","TOTAL_NO_COINCIDE",f"Válidos + blancos + nulos = {total}; emitidos = {row.emitidos}.")
            if party and not any(pd.isna(row[c]) for c in party):
                ptotal=sum(row[c] for c in party)
                if ptotal!=row.validos:
                    _alert(alerts,idx,code,"ALTA","PARTIDOS_NO_COINCIDEN",f"Votos por partido = {ptotal}; válidos = {row.validos}.")
    data["participacion_pct"]=np.where(data.inscritos>0,data.emitidos/data.inscritos*100,np.nan)
    data["nulos_pct"]=np.where(data.emitidos>0,data.nulos/data.emitidos*100,np.nan)
    data["blancos_pct"]=np.where(data.emitidos>0,data.blancos/data.emitidos*100,np.nan)
    if party:
        data["votos_partidos_total"]=data[party].sum(axis=1,min_count=1)
        data["partido_mas_votado_pct"]=np.where(data.validos>0,data[party].max(axis=1)/data.validos*100,np.nan)
    metrics=["participacion_pct","nulos_pct","blancos_pct"]+(["partido_mas_votado_pct"] if party else [])
    for metric in metrics:
        if data[metric].notna().sum()>=8:
            for idx in data.index[_mad_outliers(data[metric])]:
                _alert(alerts,idx,data.at[idx,"codigo_mesa"],"REVISION","VALOR_ESTADISTICO_ATIPICO",f"{metric} es atípico frente al conjunto; requiere contexto.")
    report=pd.DataFrame(alerts,columns=["fila","codigo_mesa","severidad","regla","detalle"])
    summary={"mesas_analizadas":int(len(data)),"alertas":int(len(report)),
             "alertas_altas":int((report.severidad=="ALTA").sum()) if len(report) else 0,
             "alertas_revision":int((report.severidad=="REVISION").sum()) if len(report) else 0,
             "departamentos":int(data.departamento.nunique(dropna=True)),"columnas_partidos":party}
    return data,report,summary
