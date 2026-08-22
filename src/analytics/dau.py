# %%

import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import Engine, Inspector

engine: Engine = create_engine("sqlite:///../../data/loyalty_system/database.db")

inspector: Inspector = inspect(engine)
tables: list[str] = inspector.get_table_names()
print(tables)

# %%

transacoes: pd.DataFrame = pd.read_sql_table(table_name="transacoes", con=engine)

# %%

print(transacoes.columns.to_list())
print(transacoes.dtypes)

# %%

transacoes["DtDia"] = transacoes["DtCriacao"].astype(str).str[:10]

transacoes["DtDia"]

# %%

dau = (
    transacoes.groupby("DtDia")["IdCliente"]
    .nunique()
    .reset_index(name="DAU")
    .sort_values("DtDia")
)

dau
