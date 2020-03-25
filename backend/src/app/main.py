# Import installed packages
from flask import Flask

# Extensions initialization
# =========================
app = Flask(__name__)

# Setup app
from .core import app_setup  # noqa

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8888)
