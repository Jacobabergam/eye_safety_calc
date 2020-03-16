#Import installed packages
from flask import Flask, Blueprint

# Import app code
app = Flask(__name__)

from core import app_setup

if __name__ == "__main__":
    app_setup.main()
