import os
from waitress import serve
from app import app

if __name__ == "__main__":
    # Get port from environment or default to 5000
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"
    
    print(f"============================================================")
    print(f" Starting Production WSGI Server (Waitress) for Windows")
    print(f" Local Address: http://localhost:{port}")
    print(f" Network Address: http://{host}:{port}")
    print(f"============================================================")
    
    # Run the production server
    serve(app, host=host, port=port)
