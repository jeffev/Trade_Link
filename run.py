from backend.server import app
from backend import callbacks

if __name__ == '__main__':
    app.run_server(debug=True)