#Flask Project Structure & Design Patterns
#app.py    - application factory (create_app), registers blueprints, dev server entry point
#models.py - Flask Database Handling (SQLite)
#blueprints/views.py - Templates, Forms, Views, Redirects
#blueprints/api.py   - Flask API
#templates/, static/ - Jinja2 templates (Bootstrap via CDN) and static assets
#
#run this file directly: python app.py, then open http://127.0.0.1:5000
from flask import Flask
import models
from blueprints.views import views_bp
from blueprints.api import api_bp


#application factory - builds and configures the app instead of a bare module-level Flask()
#lets you create multiple configured instances (e.g. for tests) instead of one global app
def create_app():
    app = Flask(__name__)
    models.init_db()

    #Blueprints - keep the web views and the JSON API in separate, independently registered modules
    app.register_blueprint(views_bp)
    app.register_blueprint(api_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
