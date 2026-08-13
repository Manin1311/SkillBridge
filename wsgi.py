"""
WSGI Entry Point for Production Deployment (Render / Gunicorn)
"""
import os
from app import create_app
from extensions import socketio

# Load environment ('production' by default on Render)
config_name = os.environ.get('FLASK_ENV', 'production')

# Create the application instance
app = create_app(config_name)

if __name__ == "__main__":
    socketio.run(app)
