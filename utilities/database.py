"""
# utilities/database.py
"""

from sqlalchemy import create_engine, Engine, text, URL, select, CursorResult
from sqlalchemy.engine.url import URL
from sqlalchemy.sql import Select

hostname: str


def connect_database(db_host=None, db_port=None, db_database=None, db_user=None, db_password=None) -> Engine:
    try:
        global hostname
        connection_string: str = (f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_host},{db_port};'
                                  f'DATABASE={db_database};UID={db_user};PWD={db_password};Encrypt=no;')
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        connection_engine: Engine = create_engine(connection_url, echo=False)
        with connection_engine.connect() as connection:
            sql_query: Select = select(text('@@SERVERNAME'))
            cursor: CursorResult = connection.execute(sql_query)
            hostname = cursor.fetchone()[0]
            if hostname:
                print(f'SQL Server connection opened in {hostname}.')
                return connection_engine
    except Exception as e:
        print(f'SQL Server Error: {e}')

def close_db_connection(connection_engine: Engine):
    try:
        connection_engine.dispose()
        print(f'SQL Server connection closed in {hostname}.')
    except Exception as e:
        print(f'SQL Server Error: {e}')

def query_last_id(connection_engine: Engine, table_name: str) -> int:
    try:
        with connection_engine.connect() as connection:
            sql_query: Select = text(f'SELECT MAX(id) FROM cargues_masivos.{table_name}')
            cursor: CursorResult = connection.execute(sql_query)
            row = cursor.fetchone()
            last_id = int(row[0]) if row[0] is not None else 0
            print(f'SQL Server: Last insert Id: {last_id} from {table_name}.')
            return last_id
    except Exception as e:
        print(f'SQL Server Error: {e}')
        return 0

