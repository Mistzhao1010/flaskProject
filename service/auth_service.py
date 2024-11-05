from service import token_service
def login(username, password):
    """
    用户登录信息检查
    :param username:
    :param password:
    :return:
    """
    try:
        if not username:
            raise ValueError("用户名不能为空")
        if not password:
            raise ValueError("密码不能为空")
    except ValueError as e:
        return {"code": 400, "msg": str(e)}

    encode_token = {
        "username": username,
        "password": password
    }
    if username == 'admin' and password == 'admin':
        return token_service.encode_token(encode_token)
    else:
        return {'status':False,'message':'Invalid username or password','code':401}