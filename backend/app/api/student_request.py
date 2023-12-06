from flask import Blueprint 

student_request = Blueprint('student_request', __name__)

@student_request.route('/test')
def test():
    return {'message': 'hello'}
    