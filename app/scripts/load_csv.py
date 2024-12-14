import time
import sys
import os
from datetime import datetime
import pandas as pd
from dateutil import parser
from sqlalchemy import create_engine, text

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import create_app
from app.models.atendimentos import Atendimento

app = create_app()

def parse_date(data):
    formatos = [
        "%d/%m%Y %H:%M", 
        "%Y-%m-%d %H:%M:%S",
        "%d /%m /%Y %H:%M:%S",
        "%d/%m/%Y %H:%M",
        "%d/%m/%Y %H:%M:%S",
        "%d/%m/%Y",
        "%d/%m/%y",
    ]
    
    for fmt in formatos:
        try:
            return datetime.strptime(data.strip(), fmt).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    return None

def load_csv_to_db(csv_file_path, chunk_size=10000):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    
    with app.app_context():
        start_time = time.time()
        for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size, sep=';'):
            chunk.columns = ['id', 'id_cliente', 'angel', 'polo', 'data_limite', 'data_de_atendimento']
            chunk['data_de_atendimento'] = chunk['data_de_atendimento'].apply(parse_date)
            chunk['data_limite'] = chunk['data_limite'].apply(parse_date)
            chunk.to_sql(Atendimento.__tablename__, con=engine, if_exists='append', index=False)
        with engine.connect() as connection:
          connection.execute(text(f"SELECT setval(pg_get_serial_sequence('{Atendimento.__tablename__}', 'id'), (SELECT MAX(id) FROM {Atendimento.__tablename__}))"))
        
        print(f"Arquivo carregado em {time.time() - start_time} segundos")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python app/scripts/load_csv.py <path_to_csv_file>")
        sys.exit(1)
    
    csv_file_path = sys.argv[1]
    load_csv_to_db(csv_file_path)