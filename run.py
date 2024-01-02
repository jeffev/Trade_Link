from backend.server import app, server, conn
from backend import callbacks

# Inicializar tabelas do banco de dados, se necessário
Base.metadata.create_all(bind=conn)

if __name__ == '__main__':
    # Iniciar o servidor Flask e Dash
    server.run(debug=True, use_reloader=False)