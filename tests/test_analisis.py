import pandas as pd
from src.analisis import analizar_dataframe

def base():
    return pd.DataFrame([{"codigo_mesa":"010101","departamento":"Cochabamba","municipio":"Cercado","inscritos":100,"emitidos":80,"validos":70,"blancos":5,"nulos":5,"votos_MAS":40,"votos_CC":30}])

def test_fila_consistente():
    _,alerts,summary=analizar_dataframe(base())
    assert alerts.empty
    assert summary["mesas_analizadas"]==1

def test_total_inconsistente():
    df=base(); df.loc[0,"nulos"]=2
    _,alerts,_=analizar_dataframe(df)
    assert "TOTAL_NO_COINCIDE" in set(alerts.regla)

def test_codigo_duplicado():
    df=pd.concat([base(),base()],ignore_index=True)
    _,alerts,_=analizar_dataframe(df)
    assert "CODIGO_DUPLICADO" in set(alerts.regla)

def test_emitidos_mayor_inscritos():
    df=base(); df.loc[0,"emitidos"]=120
    _,alerts,_=analizar_dataframe(df)
    assert "EMITIDOS_MAYOR_INSCRITOS" in set(alerts.regla)
