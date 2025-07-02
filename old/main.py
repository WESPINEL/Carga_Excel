# main.py
import os
from dotenv import load_dotenv
from core.database import Database
from core.excel_handler import ExcelHandler
from utilities.excel import insert_excel_records

# Cargar variables de entorno
load_dotenv()

def load_config():
    return {
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_PORT": int(os.getenv("DB_PORT")),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD"),
        "DB_DATABASE": os.getenv("DB_DATABASE")
    }

def load_ssh_config():
    return {
        "SSH_HOST": os.getenv("SSH_HOST"),
        "SSH_PORT": int(os.getenv("SSH_PORT", 22)),
        "SSH_USER": os.getenv("SSH_USER"),
        "SSH_KEY_FILENAME": os.getenv("SSH_KEY_FILENAME")
    }

if __name__ == "__main__":
    file_name = "cmdr_glosas_parciales_adres.xlsx"
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))
    table_name = "cmdr_glosas_parciales_adres"
    # use_ssh = os.getenv("DB_USE_SSH", "0") == "1"
    use_ssh = os.getenv("DB_USE_SSH", "false").lower() == "true"

    # Validar Excel
    excel_handler = ExcelHandler(file_path, file_name)
    if not excel_handler.validate():
        print("❌ El archivo Excel no pasó la validación. Abortando.")
        exit(1)

    # Conexión DB
    conf = load_config()
    ssh_conf = load_ssh_config()
    db = Database(conf, ssh_conf, use_ssh)
    db.connect()

    # Cargar datos
    insert_excel_records(db.engine, table_name)

    # Cerrar conexión
    db.close()
    excel_handler.clear()
