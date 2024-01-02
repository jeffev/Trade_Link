from sqlalchemy import create_engine, declarative_base
from sqlalchemy.orm import sessionmaker
from entities.entidade_trade import Base
from operations_trades import criar_trade, obter_trades, obter_trade_por_id, atualizar_trade, excluir_trade
from endpoints_trades import criar_trade_endpoint, obter_trades_endpoint, obter_trade_por_id_endpoint, atualizar_trade_endpoint, excluir_trade_endpoint
import dash
import dash_bootstrap_components as dbc
from flask import Flask

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

# Declarar a classe Base do SQLAlchemy
Base = declarative_base()

# Inicializar o aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = Flask(__name__)

# Adicionar os blueprints dos endpoints relacionados aos trades
app.register_blueprint(criar_trade_endpoint)
app.register_blueprint(obter_trades_endpoint)
app.register_blueprint(obter_trade_por_id_endpoint)
app.register_blueprint(atualizar_trade_endpoint)
app.register_blueprint(excluir_trade_endpoint)