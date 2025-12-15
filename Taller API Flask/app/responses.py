from flask import jsonify

def response():
    return jsonify(
        {
        'success': True,
        'data': data
        }
    ), 200