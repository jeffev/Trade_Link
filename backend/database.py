from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.entities.entidade_trade import Base
import os
from dotenv import load_dotenv

# Configurações de conexão com o banco de dados PostgreSQL
db_config = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
}

# Conectar ao banco de dados
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def criar_tabelas():
    Base.metadata.create_all(bind=engine)