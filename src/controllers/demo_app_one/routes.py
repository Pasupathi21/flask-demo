from flask import Blueprint
# ********** controll class import
from .demo_app_one import DemoAppOne

print(__name__)

demo_app_one_bp = Blueprint('demo_app_one_bp', __name__)

demo_app_one_instance = DemoAppOne()
# ************* add routes

@demo_app_one_bp.route('/', methods=['GET'])
@demo_app_one_bp.route('/demo-endpoint', methods=['GET', 'POST'])
def demo_endpoint():
    return demo_app_one_instance.testFn()
    # return 'text'

@demo_app_one_bp.route('/post-data', methods=['POST'])
def demo_post():
    return demo_app_one_instance.testPost()

@demo_app_one_bp.route('/get-query', methods=['GET'])
def getQuery():
    return demo_app_one_instance.getQueryParams()

@demo_app_one_bp.route('/get-params-id/<id>', methods=['GET', 'POST'])
def getParams(id):
    return demo_app_one_instance.getPathParams(id=id)    
# @demo_app_one_bp.add_url_rule('/get-params-id/<int: id>', view_func=demo_app_one_instance.getPathParams())