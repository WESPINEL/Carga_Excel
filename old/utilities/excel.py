# utilities/excel.py
import pandas as pd
from pandas import DataFrame
from sqlalchemy import Engine
from utilities.database import query_last_id
from utilities.structures_datatypes import get_valid_datatypes
from utilities.structures_columns import get_valid_columns

df: DataFrame

def validate_excel(file_path: str, file_name: str) -> bool:
    global df
    try:
        df = pd.read_excel(file_path)
        valid_columns = get_valid_columns(file_name)
        valid_datatypes = get_valid_datatypes(file_name)

        if list(df.columns) != valid_columns:
            raise ValueError(f"EXCEL Error: Invalid columns. Expected: {valid_columns}, Found: {list(df.columns)}")
        print("✅ Columnas validadas correctamente.")

        for column, expected_dtype in valid_datatypes.items():
            actual_dtype = df[column].dtype.name
            if actual_dtype != expected_dtype:
                raise TypeError(f"EXCEL Error: Tipo de dato inválido en '{column}'. Esperado: {expected_dtype}, Encontrado: {actual_dtype}")
        print("✅ Tipos de datos validados correctamente.")
        return True

    except Exception as e:
        print(f"❌ Validación fallida: {e}")
        return False

def insert_excel_records(connection_engine: Engine, table_name: str, schema: str = "cargues_masivos") -> int:
    global df
    try:
        initial_count = query_last_id(connection_engine, table_name)
        df.to_sql(table_name, con=connection_engine, if_exists='append', index=False, schema=schema, chunksize=100, method='multi')
        final_count = query_last_id(connection_engine, table_name)
        inserted = final_count - initial_count
        print(f"✅ Se insertaron {inserted} registros en la tabla {schema}.{table_name}")
        return inserted
    except Exception as e:
        print(f"❌ Error al insertar datos: {e}")
        return 0

def clear_dataframe():
    global df
    df = pd.DataFrame()
