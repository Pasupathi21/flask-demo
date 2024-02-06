from flask import Blueprint
# ********** controll class import
from .demo_app_one import DemoAppOne

print(__name__)

demo_app_one_bp = Blueprint('demo_app_one_bp', __name__)

demo_app_one_instance = DemoAppOne()
# ************* add routes

@demo_app_one_bp.route('/demo-endpoint', methods=['GET', 'POST'])
def demo_endpoint():
    return demo_app_one_instance.testFn()
    # return 'text'