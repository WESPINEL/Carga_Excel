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

def get_table_name_from_file(file_name: str) -> str:
    # Elimina la extensión y asume que ese es el nombre de la tabla
    return os.path.splitext(file_name)[0]

if __name__ == "__main__":
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "input"))
    os.makedirs(input_dir, exist_ok=True)
    use_ssh = os.getenv("DB_USE_SSH", "false").lower() == "true"

    # Conexión DB
    conf = load_config()
    ssh_conf = load_ssh_config()
    db = Database(conf, ssh_conf, use_ssh)
    db.connect()

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".xlsx"):
            file_path = os.path.join(input_dir, file_name)
            table_name = get_table_name_from_file(file_name)

            print(f"\n📄 Procesando archivo: {file_name} → tabla: {table_name}")
            
            excel_handler = ExcelHandler(file_path, file_name)
            if not excel_handler.validate():
                print(f"❌ El archivo {file_name} no pasó la validación. Saltando.")
                continue

            insert_excel_records(db.engine, table_name)
            excel_handler.clear()

    db.close()
    print("\n✅ Proceso completado para todos los archivos.")
