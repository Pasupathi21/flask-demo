from flask import Flask

# import blueprints
from src.controllers.demo_app_one.routes import demo_app_one_bp

# Application instance
app = Flask(__name__)


# ******************* register all blueprint routes
app.register_blueprint(demo_app_one_bp)

# check is root file and run app
if __name__ == '__main__':
    app.run(port=9000,debug=True)