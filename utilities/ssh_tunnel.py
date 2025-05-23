"""
SSH Tunnel
"""

from sshtunnel import SSHTunnelForwarder
import os

ssh_tunnel_server: SSHTunnelForwarder
bind_port: int

def connect_ssh_server(ssh_host=None, ssh_username=None, ssh_port=22, ssh_key_filename=None, db_host='0.0.0.0', db_port=1433):
    global ssh_tunnel_server
    if not os.path.exists(ssh_key_filename):
        raise FileNotFoundError(f"❌ La clave privada SSH no fue encontrada en: {ssh_key_filename}")
    try:
        ssh_tunnel_server = SSHTunnelForwarder(
            ssh_host=ssh_host,
            ssh_port=ssh_port,
            ssh_username=ssh_username,
            ssh_pkey=ssh_key_filename,
            remote_bind_address=(db_host, db_port)
        )
    except Exception as e:
        raise ConnectionError(f"❌ Error al configurar el túnel SSH: {e}")

def get_ssh_tunneled_port(ssh_host=None, ssh_username=None, ssh_port=22,
                          ssh_key_filename=None, db_host=None) -> int:
    global bind_port
    connect_ssh_server(
        ssh_host,
        ssh_username,
        ssh_port,
        ssh_key_filename,
        db_host
    )
    try:
        ssh_tunnel_server.start()
        bind_port = ssh_tunnel_server.local_bind_port
        print(f"✅ Túnel SSH abierto en puerto local: {bind_port}")
        return bind_port
    except Exception as e:
        raise ConnectionError(f"❌ No se pudo iniciar el túnel SSH: {e}")

def close_ssh_server():
    global ssh_tunnel_server
    try:
        ssh_tunnel_server.close()
        print(f"🔒 Túnel SSH cerrado en puerto local: {bind_port}")
    except Exception as e:
        print(f"❌ Error al cerrar el túnel SSH: {e}")
