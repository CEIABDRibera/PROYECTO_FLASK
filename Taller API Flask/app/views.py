from flask import Blueprint

from .responses import response


api_v1 = Blueprint('api', __name__, url_prefix='/api/v1') # prefijo para todas las rutas

@api_v1.route('/task', methods=['GET'])
def get_tasks():
    return response({
            'mensaje': 'Nuevo mensaje'
        })

@api_v1.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    pass

@api_v1.route('/task', methods=['POST'])
def create_task():
    pass

@api_v1.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    pass

@api_v1.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    pass
