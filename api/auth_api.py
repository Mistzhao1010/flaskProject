from flask import request, jsonify, Response

from service import auth_service


def login():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
    elif request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

    token = auth_service.login(username, password)
    return {'token': token}


