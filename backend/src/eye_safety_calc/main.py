# Import installed packages
from flask import Flask, Blueprint

# Import app code
app = Flask(__name__)  # noqa

from core import app_setup  # noqa

if __name__ == "__main__":
    app_setup.main()
