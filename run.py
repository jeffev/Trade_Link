from backend.server import app, server
from backend import callbacks

if __name__ == '__main__':
    app.run_server(debug=True)