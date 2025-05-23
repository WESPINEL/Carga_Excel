from utilities.database import connect_database, close_db_connection
from utilities.ssh_tunnel import close_ssh_server, get_ssh_tunneled_port


class Database:
    def __init__(self, conf, ssh_conf, use_ssh):
        self.engine = None
        self.conf = conf
        self.ssh_conf = ssh_conf
        self.use_ssh = use_ssh

    def connect(self):
        host = self.conf['DB_HOST']
        if self.use_ssh:
            host = '127.0.0.1'
            self.conf['DB_PORT'] = self.get_tunneled_port()
        self.engine = connect_database(
            db_host=host,
            db_port=self.conf['DB_PORT'],
            db_database=self.conf['DB_DATABASE'],
            db_user=self.conf['DB_USER'],
            db_password=self.conf['DB_PASSWORD']
        )

    def get_tunneled_port(self):
        return get_ssh_tunneled_port(
            ssh_host=self.ssh_conf['SSH_HOST'],
            ssh_username=self.ssh_conf['SSH_USER'],
            ssh_port=self.ssh_conf['SSH_PORT'],
            ssh_key_filename=self.ssh_conf['SSH_KEY_FILENAME'],
            db_host=self.conf['DB_HOST']
        )

    def close(self):
        close_db_connection(self.engine)
        if self.use_ssh:
            close_ssh_server()
