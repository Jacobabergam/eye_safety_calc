"""Installation script for flask-api-tutorial application."""
from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = (
    "Eye_Safety_Calc backend API setup to calculate safety"
    "for a laser system according to ANSI/IEC Standards"
)
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Jacob Bergam"
AUTHOR_EMAIL = "Jabergam@gmail.com"
PROJECT_URLS = {
    "Documentation": "None",
    "Bug Tracker": "https://github.com/Jacobabergam/Eye_Safety_Calc/issues",
    "Source Code": "https://github.com/Jacobabergam/Eye_Safety_Calc",
}
INSTALL_REQUIRES = [
    "Flask",
    "Flask-Bcrypt",
    "Flask-Cors",
    "Flask-Migrate",
    "flask-restx",
    "Flask-SQLAlchemy",
    "PyJWT",
    "python-dateutil",
    "python-dotenv",
    "requests",
    "urllib3",
    "marshmallow==2.18.0",
    "werkzeug==0.16.1",
]
EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "flake8",
        "pre-commit",
        "pydocstyle",
        "pytest",
        "pytest-black",
        "pytest-clarity",
        "pytest-dotenv",
        "pytest-flake8",
        "pytest-flask",
        "tox",
    ]
}

setup(
    name="eye_safety_calc",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url="https://github.com/Jacobabergam/Eye_Safety_Calc",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
