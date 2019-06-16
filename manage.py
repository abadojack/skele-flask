"""Module with application entry point."""

# Third party Imports
from flask import jsonify

# Local Imports
from main import create_app
from config import AppConfig

# create application object
app = create_app(AppConfig)


@app.route('/')
def index():
    """Returns 'All systems are operational.' """
    return jsonify(dict(message='All systems are operational'))


@app.route('/status')
def health_check():
    """Check status of the application."""
    return jsonify(dict(message='Server is online ')), 200


if __name__ == '__main__':
    app.run()
