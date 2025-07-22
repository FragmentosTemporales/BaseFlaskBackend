import pandas as pd
from rich import print
from sqlalchemy import create_engine, text
from ..settings import settings as s


class MyEngine():

    def __init__(self):
        """Iniciamos conexiones con el servidor"""

        POSTGRES_USER = s.dbuser
        POSTGRES_PASSWORD = s.dbpassword
        POSTGRES_HOST = s.dbhost
        POSTGRES_SCHEMA = s.dbschema

        self.engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_SCHEMA}',
                                        pool_reset_on_return=None)
        
        print(f"[bold green]Conexión a la base de datos establecida con éxito.[/bold green]")

    def execute(self,query):
        print(query)
        with self.engine.connect() as conn:
            conn.execute(text(query))
            conn.commit()
            return 

    def query(self, query):
        return pd.read_sql_query(query, con=self.engine)
