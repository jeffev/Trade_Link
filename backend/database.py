from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from backend.entities.entidade_trade import Base, Trade

# Configurações de conexão com o banco de dados PostgreSQL
db_config = {
    'dbname': 'TradeLink',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432',
}

# Conectar ao banco de dados
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def criar_tabelas():
    Base.metadata.create_all(bind=engine)