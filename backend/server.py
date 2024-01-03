import dash
import dash_bootstrap_components as dbc
from dash import html
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from backend.endpoints.endpoints_trades import criar_trade_endpoint, obter_trades_endpoint, obter_trade_por_id_endpoint, atualizar_trade_endpoint, excluir_trade_endpoint
from backend.database import criar_tabelas

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
Base = declarative_base(metadata=MetaData())

# Inicializar o aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Adicionar os blueprints dos endpoints relacionados aos trades
app.server.add_url_rule('/api/trades', view_func=criar_trade_endpoint, methods=['POST'])
app.server.add_url_rule('/api/trades', view_func=obter_trades_endpoint, methods=['GET'])
app.server.add_url_rule('/api/trades/<int:trade_id>', view_func=obter_trade_por_id_endpoint, methods=['GET'])
app.server.add_url_rule('/api/trades/<int:trade_id>', view_func=atualizar_trade_endpoint, methods=['PUT'])
app.server.add_url_rule('/api/trades/<int:trade_id>', view_func=excluir_trade_endpoint, methods=['DELETE'])

# Criar tabelas no banco de dados
criar_tabelas()

# Definir um layout simples (substitua isso pelo seu próprio layout)
app.layout = html.Div("Olá, Mundo!")

if __name__ == "__main__":
    app.run_server(debug=True)